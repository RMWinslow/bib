---
title: Papers
layout: post
has_children: false
has_toc: false
nav_order: 1
---

Listed by date added to this bibliography, newest first.

{% assign papers = site.pages | where: "parent", "Papers" | where: "layout", "bib" | sort: "date" | reverse %}
<ul>
{% for paper in papers %}
  <li>
    {{ paper.pub_authors | join: ", " | escape }} ({{ paper.pub_year }}).
    <a href="{{ paper.url | relative_url }}">{{ paper.title | escape }}</a>
  </li>
{% endfor %}
</ul>
