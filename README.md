# Important!
How to edit the website: 
1. edit the template in `templates/index.html`; this ensures that the HTML for the rubrics is included correctly! 
2. render the template by running `python render.py` (this requires the `jinjia` package), which creates a fresh `index.html` in the root
3. Commit both the amended template and the rendered `index.py` (as the latter is what is used for the actual website)

The rubrics are present in `.txt` format in `templates/rubrics`. In that same folder, there is a Python script that converts all 
of them to the html format that is then imported in the jinjia template.  



# Academic Project Page Template
This is an academic paper project page template.


Example project pages built using this template are:
- https://horwitz.ai/probex
- https://vision.huji.ac.il/probegen
- https://horwitz.ai/mother
- https://horwitz.ai/spectral_detuning
- https://vision.huji.ac.il/ladeda
- https://vision.huji.ac.il/dsire
- https://horwitz.ai/podd
- https://dreamix-video-editing.github.io
- https://horwitz.ai/conffusion
- https://horwitz.ai/3d_ads/
- https://vision.huji.ac.il/ssrl_ad
- https://vision.huji.ac.il/deepsim



## Start using the template
To start using the template click on `Use this Template`.

The template uses html for controlling the content and css for controlling the style. 
To edit the websites contents edit the `index.html` file. It contains different HTML "building blocks", use whichever ones you need and comment out the rest.  

**IMPORTANT!** Make sure to replace the `favicon.ico` under `static/images/` with one of your own, otherwise your favicon is going to be a dreambooth image of me.

## Components
- Teaser video
- Images Carousel
- Youtube embedding
- Video Carousel
- PDF Poster
- Bibtex citation

## Tips:
- The `index.html` file contains comments instructing you what to replace, you should follow these comments.
- The `meta` tags in the `index.html` file are used to provide metadata about your paper 
(e.g. helping search engine index the website, showing a preview image when sharing the website, etc.)
- The resolution of images and videos can usually be around 1920-2048, there rarely a need for better resolution that take longer to load. 
- All the images and videos you use should be compressed to allow for fast loading of the website (and thus better indexing by search engines). For images, you can use [TinyPNG](https://tinypng.com), for videos you can need to find the tradeoff between size and quality.
- When using large video files (larger than 10MB), it's better to use youtube for hosting the video as serving the video from the website can take time.
- Using a tracker can help you analyze the traffic and see where users came from. [statcounter](https://statcounter.com) is a free, easy to use tracker that takes under 5 minutes to set up. 
- This project page can also be made into a github pages website.
- Replace the favicon to one of your choosing (the default one is of the Hebrew University). 
- Suggestions, improvements and comments are welcome, simply open an issue or contact me. You can find my contact information at [https://horwitz.ai](https://horwitz.ai)

## Acknowledgments
Parts of this project page were adopted from the [Nerfies](https://nerfies.github.io/) page.

## Website License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.


# Plan and TODO

- [X] Leave the top figure but with the description Jose suggested (This is a collaborative community…) on top
- [X] A section with the table describing the dimensions and showing the text of each rubric below it (what is in the paper appendix with a selector that allows you to select one at a time)
- [X] A section on the battery: I can put a link to it. I will put a table showing what datasets are in the battery and the obtained demands histograms (which are already there)
- [X] A section of profiling LLM capabilities: short description, the radial profile plot for all LLMs at once, and then another selector that allows you to visualize the characteristic curve for one LLM at a time (or the one with all of them superimposed). In a second moment, we could also add something like a leaderboard (see https://www.swebench.com/#lite) for each separate dimension.
- [X] I would probably skip the “predicting performance” section as that seems more of a thing about the paper.
- [X] Then “how to contribute”, we can improve that iteratively, but at first we can say that people can run the rubrics on new datasets or test the battery on existing LLMs and do pull requests to add the results on the website. Actually, just starting with an email will be OK
- [ ] ADD dataset link!
 