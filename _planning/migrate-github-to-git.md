# Migration plan: ~/Documents/GitHub/ to ~/git/

Date: 2026-03-23

## Summary

We investigated migrating `C:\Users\rober\Documents\GitHub\` to `C:\Users\rober\git\` to shorten file paths. The move is low-risk.

## Findings

- **OneDrive**: Not running and not syncing the Documents folder. No cloud-sync complications.
- **Git repos**: Fully portable; all history, branches, and remotes travel with the folder.
- **Claude Code project memory directories**: 13 directories under `~/.claude/projects/` are keyed to the old path and would need renaming. These contain conversation logs (UUID-named `.jsonl` files and session directories), not user-authored content.

## Directories to rename

After the move, rename these directories under `~/.claude/projects/`:

| Old name | New name |
|---|---|
| `C--Users-rober-Documents-GitHub-Peer-Review-Referee-Notes` | `C--Users-rober-git-Peer-Review-Referee-Notes` |
| `C--Users-rober-Documents-GitHub-Teaching-Notes` | `C--Users-rober-git-Teaching-Notes` |
| `C--Users-rober-Documents-GitHub-bib` | `C--Users-rober-git-bib` |
| `C--Users-rober-Documents-GitHub-claude-data-cleaning-test` | `C--Users-rober-git-claude-data-cleaning-test` |
| `C--Users-rober-Documents-GitHub-claude-data-cleaning-test-student-applicant-data` | `C--Users-rober-git-claude-data-cleaning-test-student-applicant-data` |
| `C--Users-rober-Documents-GitHub-papersdrafts` | `C--Users-rober-git-papersdrafts` |
| `C--Users-rober-Documents-GitHub-papersdrafts-covid-unemployment-dol-data` | `C--Users-rober-git-papersdrafts-covid-unemployment-dol-data` |
| `C--Users-rober-Documents-GitHub-papersdrafts-covid-unemployment-empirics2` | `C--Users-rober-git-papersdrafts-covid-unemployment-empirics2` |
| `C--Users-rober-Documents-GitHub-papersdrafts-covid-unemployment-empirics2-data` | `C--Users-rober-git-papersdrafts-covid-unemployment-empirics2-data` |
| `C--Users-rober-Documents-GitHub-posts` | `C--Users-rober-git-posts` |
| `C--Users-rober-Documents-GitHub-reduced-alphabet-finder` | `C--Users-rober-git-reduced-alphabet-finder` |
| `C--Users-rober-Documents-GitHub-reduced-alphabet-finder-old-files` | `C--Users-rober-git-reduced-alphabet-finder-old-files` |
| `C--Users-rober-Documents-GitHub-referee2` | `C--Users-rober-git-referee2` |

## Commands

Close all applications that reference the GitHub folder (VS Code, terminals, etc.), then run in a bash shell:

```bash
# 1. Move the folder
mv "$HOME/Documents/GitHub" "$HOME/git"

# 2. Rename Claude Code project directories
cd "$HOME/.claude/projects"
for dir in C--Users-rober-Documents-GitHub-*; do
  newdir="${dir/Documents-GitHub/git}"
  mv "$dir" "$newdir"
done
```

## Other things to check after the move

- **VS Code**: Re-open projects from `~/git/`. Workspace files with absolute paths may need updating.
- **GitHub Desktop**: If used, re-add repos from the new location.
- **Shell aliases or scripts**: Update any that reference `~/Documents/GitHub/`.
- **Windows shortcuts / pinned items**: Update any that point into the old path.
- **~/.claude/CLAUDE.md**: Update any path references in the global instructions file.
