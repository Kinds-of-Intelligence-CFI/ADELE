# ADeLe Project Website

Website for [ADeLe v1.0: A battery for AI Evaluation with explanatory and predictive power](https://kinds-of-intelligence-cfi.github.io/ADELE/).

## How to edit the website

1. Edit the template in `templates/index.html` (this ensures that the HTML for the rubrics is included correctly)
2. Render the template by running `python render.py` (requires the `jinja2` package), which creates a fresh `index.html` in the root
3. Commit both the amended template and the rendered `index.html` (as the latter is what is used for the actual website)

The rubrics are present in `.txt` format in `templates/rubrics/txt/`. In that same folder, there is a Python script (`convert_txt_to_html.py`) that converts them to the HTML format that is then imported in the Jinja2 template.

## Acknowledgments

Parts of this project page were adopted from the [Academic Project Page Template](https://github.com/eliahuhorwitz/Academic-project-page-template) and the [Nerfies](https://nerfies.github.io/) page.

## Website License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
