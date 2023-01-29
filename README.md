
This is an experiment with using the JTD Jekyll template as a bibliography tracker.
The search widget at the top should automatically index all the pages on this subsite. 

To replicate this functionality:

1. Create a Github repo and enable github pages.
2. Switch to the JTD theme by creating a file called `_config.yaml` with the following contents:

```
title: "Bibliography"
remote_theme: just-the-docs/just-the-docs
search_enabled: true
```

(I actually use `remote_theme: RMWinslow/JTD-RMW`, which is my fork of Just-the-docs with tweaked styling. Either works.)

3. Create a page for each referenced work. Structure it however you like. [See here for the JTD documentation on how to organize the heirarchical navbar.](https://just-the-docs.github.io/just-the-docs/docs/navigation-structure/#pages-with-children)

The trick here is that JTD uses a version of lunr to create a search index page. When Github builds the site, it combine the text content of every page into a single file, which the search widget then accesses. 
So indirectly, I'm keeping a bibliography with embedded notes in a giant json file and accessing individual entries as needed with a spiffy html wrapper around the content.


