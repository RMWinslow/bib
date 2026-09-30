"""Tests for the September 2026 one-paper Zotero import pilot.

Uses small in-memory examples plus the saved pilot source, when available.
Does not modify Zotero, create test files, or remove files.
"""

import copy
import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import import_zotero_papers as importer
import standardize_papers as audit
from standardize_papers import ReviewNeeded, split_frontmatter


def row(key, kind, **fields):
    return {"key": key, "data": {"key": key, "itemType": kind, **fields}}


def bundle():
    return {
        "item": row("ABCDEFGH", "journalArticle", citationKey="garcia2020example",
                    title="Example", DOI="10.1234/example", tags=[{"tag": "manual"}]),
        "children": [], "annotations": [],
        "bibtex": r"""@article{garcia2020example,
            title={Example}, author={Garc{\'i}a, Ana}, year={2020},
            journal={Journal}, file={C:\private\paper.pdf}, abstract={Long abstract},
            doi={10.1234/example}}
        """,
    }


class ImportTests(unittest.TestCase):
    def test_zotero_editor_wrapper_and_note_heading(self):
        text = importer.nested_note('<div data-schema-version="9"><h1>My example</h1><p>Exact words.</p></div>')
        self.assertEqual(text, '#### My example\n\nExact words.')

    def test_duplicate_identical_doi_from_zotero_extra(self):
        source = '@article{x,\n title={Test}, author={Smith, A}, year={2020},\n doi={10.1/test},\n doi={10.1/test},\n}'
        _, _, cleaned = importer.clean_bibtex(source)
        self.assertEqual(cleaned.count('doi ='), 1)
        with self.assertRaises(ReviewNeeded):
            importer.clean_bibtex(source.replace('doi={10.1/test},\n}', 'doi={10.1/other},\n}'))

    def test_bibtex_keeps_accents_and_drops_non_citation_fields(self):
        _, text = importer.render(bundle(), "2026-09-29")
        front, _ = split_frontmatter(text)
        self.assertEqual(front["pub_authors"], ["Ana García"])
        self.assertEqual(front["tags"], ["manual"])
        self.assertEqual(str(front["date"]), "2026-09-29")
        self.assertEqual(front["pub_year"], 2020)
        self.assertNotIn("private", text)
        self.assertNotIn("Long abstract", text)
        self.assertIn("```bibtex", text)

    def test_empty_sections_are_commented(self):
        _, text = importer.render(bundle(), "2026-09-29")
        self.assertIn("<!--\n## Notes and Excerpts\n-->", text)
        self.assertIn("<!--\n## Abstract\n-->", text)

    def test_new_page_with_dates_needs_no_git_history(self):
        _, text = importer.render(bundle(), "2026-09-29")
        path = Mock()
        path.relative_to.return_value.as_posix.return_value = "paper/garcia2020example.md"
        path.read_bytes.return_value = text.encode("utf-8")
        with patch.object(audit, "git_dates") as dates:
            result = audit.examine(path, {}, {})
        dates.assert_not_called()
        self.assertEqual(result.issues, [])
        self.assertEqual(result.after, text)

    def test_highlight_order_and_comment_provenance(self):
        b = bundle()
        b["annotations"] = [
            row("ZZZZZZZZ", "annotation", parentItem="PDFABCDE", annotationType="highlight",
                annotationSortIndex="00002", annotationText="Second quotation.",
                annotationPageLabel="iii", annotationComment="My exact words — unchanged."),
            row("YYYYYYYY", "annotation", parentItem="PDFABCDE", annotationType="highlight",
                annotationSortIndex="00001", annotationText="First quotation.\nSecond line.",
                annotationPageLabel="ii", annotationComment=""),
        ]
        _, text = importer.render(b, "2026-09-29")
        self.assertLess(text.index("First quotation."), text.index("Second quotation."))
        self.assertIn("> First quotation.\n> Second line.", text)
        self.assertIn("*p. iii*", text)
        self.assertIn("My exact words — unchanged.", text)
        self.assertNotIn("**My comment:**", text)
        self.assertIn("Zotero annotation ZZZZZZZZ; attachment PDFABCDE", text)
        self.assertNotIn("<!--\n## Notes and Excerpts", text)

    def test_comment_without_highlight(self):
        b = bundle()
        b["annotations"] = [row("ZZZZZZZZ", "annotation", parentItem="PDFABCDE",
                                annotationType="note", annotationComment="An independent comment.")]
        _, text = importer.render(b, "2026-09-29")
        self.assertIn("An independent comment.", text)

    def test_colors_keep_every_excerpt_visible(self):
        b = bundle()
        b["annotations"] = [
            row("GREENAAA", "annotation", parentItem="PDFABCDE", annotationType="highlight",
                annotationColor="#5fb236", annotationText="Future paper", annotationPageLabel="3",
                annotationComment="   "),
            row("GREENBBB", "annotation", parentItem="PDFABCDE", annotationType="highlight",
                annotationColor="#5fb236", annotationText="Discussed paper", annotationPageLabel="4",
                annotationComment="Follow this up."),
            row("REDAAAAA", "annotation", parentItem="PDFABCDE", annotationType="highlight",
                annotationColor="#ff6666", annotationText="Visible red excerpt"),
        ]
        _, text = importer.render(b, "2026-09-29")
        self.assertNotIn("GREEN COMMENTS", text)
        self.assertIn("color #ff6666 -->", text)
        self.assertIn("color green #5fb236 -->\n> Future paper\n>\n> *p. 3*\n{: .zotero-green}", text)
        self.assertIn("{: .zotero-red}", text)
        self.assertEqual(text.count("{: .zotero-green}"), 2)
        self.assertIn("\n\nFollow this up.", text)

    def test_images_and_duplicate_annotations_require_review(self):
        b = bundle()
        image = row("ZZZZZZZZ", "annotation", parentItem="PDFABCDE", annotationType="image")
        b["annotations"] = [image]
        with self.assertRaises(ReviewNeeded):
            importer.render(b, "2026-09-29")
        image["data"].update(annotationType="highlight", annotationText="A quote")
        b["annotations"] = [image, copy.deepcopy(image)]
        with self.assertRaises(ReviewNeeded):
            importer.render(b, "2026-09-29")

    def test_rich_text_note_conversion(self):
        b = bundle()
        b["children"] = [row("NOTEABCD", "note", note="<p>My <strong>important</strong> note &amp; its context.</p><ul><li>First point</li></ul>")]
        _, text = importer.render(b, "2026-09-29")
        self.assertIn("My **important** note & its context.", text)
        self.assertIn("First point", text)
        self.assertIn("Zotero note NOTEABCD", text)

    def test_generated_annotation_notes_are_not_silently_duplicated(self):
        with self.assertRaises(ReviewNeeded):
            importer.note_markdown('<p><span data-annotation="something">Quote</span></p>')

    def test_private_links_are_not_published(self):
        with self.assertRaises(ReviewNeeded):
            importer.web_link("PDF", "file:///C:/private/paper.pdf")

    def test_annotation_fetch_is_explicit(self):
        api = Mock()
        api.base = "http://example.invalid"
        api.all.side_effect = [[row("PDFABCDE", "attachment")], []]
        api.text.return_value = bundle()["bibtex"]
        importer.collect_bundle(api, bundle()["item"])
        api.all.assert_any_call("/items/PDFABCDE/children?itemType=annotation")

    def test_pagination_reads_past_first_hundred(self):
        api = importer.Zotero()
        api.get = Mock(side_effect=[[{"key": str(i)} for i in range(100)], [{"key": "last"}]])
        self.assertEqual(len(api.all("/items?itemType=note")), 101)
        api.get.assert_called_with("/items?itemType=note&limit=100&start=100")

    def test_existing_key_skips_before_any_network_request(self):
        with patch.object(importer, "saved_links", return_value={"ABCDEFGH": ["paper/existing.md"]}), \
             patch.object(importer, "Zotero") as api, \
             patch.object(sys, "argv", ["import", "draft", "ABCDEFGH"]), redirect_stdout(io.StringIO()):
            self.assertEqual(importer.main(), 0)
            api.return_value.read_collection.assert_not_called()
            api.return_value.text.assert_not_called()

    def test_item_outside_read_collection_is_rejected(self):
        with patch.object(importer, "saved_links", return_value={}), \
             patch.object(importer, "Zotero") as api, \
             patch.object(sys, "argv", ["import", "draft", "ABCDEFGH", "--out", "unused.md"]):
            api.return_value.read_collection.return_value = []
            with self.assertRaises(ReviewNeeded):
                importer.main()

    def test_existing_output_is_not_overwritten(self):
        path = Mock()
        path.open.side_effect = FileExistsError
        with self.assertRaises(FileExistsError):
            importer.write_new(path, "replacement")
        path.open.assert_called_once_with("x", encoding="utf-8", newline="\n")

    def test_saved_pilot_reproduces_draft_and_every_annotation(self):
        directory = importer.ROOT / "_planning" / "zotero-import-pilot"
        snapshot = directory / "frischmann2015retrospectives-source.json"
        if not snapshot.exists():
            self.skipTest("pilot source snapshot is not present")
        b = json.loads(snapshot.read_text(encoding="utf-8"))
        _, generated = importer.render(b, b["draft_date"], b["extra_links"], b["verified_against"])
        actual = (directory / "frischmann2015retrospectives.md").read_text(encoding="utf-8")
        self.assertEqual(generated, actual)
        self.assertEqual(len(b["annotations"]), 11)
        self.assertEqual(sum(bool(r["data"].get("annotationComment")) for r in b["annotations"]), 1)
        for row_ in b["annotations"]:
            d = row_["data"]
            self.assertIn(importer.quote(d["annotationText"]), actual)
            self.assertEqual(actual.count("Zotero annotation " + d["key"] + ";"), 1)
            if d.get("annotationComment"):
                self.assertIn(d["annotationComment"], actual)


if __name__ == "__main__":
    unittest.main()
