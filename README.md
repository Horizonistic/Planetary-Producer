I wanted to create randomized yet similar planets-ish images.

I originally attempted to use Python and Pillow, but that turned out to be incredibly limited and hardly fitting for what I was trying to accomplish.  The script lineDrawTest.py is this experiment and it still generates an interesting visual.  The default values currently generate 10 images and 10 corresponding log files for each image.

My second and more educated attempt uses script-fu from GIMP, which gives me access the the full abilities GIMP offers.  Currently my process involves creating solid noise in an ellipse and bluring that, giving a gas planet effect.  Right now it's as refined as I want it to be.

Examples of the GIMP plugin:

![Example 1](https://raw.githubusercontent.com/Horizonistic/Planetary-Producer/master/examples/example1.png)

![Example 2](https://raw.githubusercontent.com/Horizonistic/Planetary-Producer/master/examples/example2.png)