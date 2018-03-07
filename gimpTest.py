#!/usr/bin/python
 
from gimpfu import *
 
def plugin_main(image, drawable, planet_radius):
    print("Starting...")

    # todo: make number of planets to generate adjustable

    image_height = planet_radius * 2
    image_width = planet_radius * 2

    ###
    #   Image and base layer initiation
    ###
    # Width, height, image-type
    image = pdb.gimp_image_new(image_width, image_height, RGB)
    # Image, width, height, type, name, opacity, effect
    new_layer = pdb.gimp_layer_new(image, image.width, image.height, RGBA_IMAGE, "Background", 100, NORMAL_MODE)
    # Image, layer, parent, position
    pdb.gimp_image_insert_layer(image, new_layer, None, 0)

    ###
    #   Implementing script-fu-difference-clouds,
    #   because apparently the function doesn't work
    ###
    diff_clouds = pdb.gimp_layer_new(image, image.width, image.height, RGBA_IMAGE, "Clouds", 100, DIFFERENCE_MODE)
    pdb.gimp_image_insert_layer(image, diff_clouds, None, 1)
    pdb.gimp_drawable_fill(diff_clouds, TRANSPARENT_FILL)

    # todo: make parameters for solid noise tweakable
    # Image, drawable, tilable, turbulent, seed, detail, xsize, ysize
    pdb.plug_in_solid_noise(image, diff_clouds, 0, 0, 0, 1, 4.0, 4.0)
    # pdb.gimp_image_merge_down(image, diff_clouds, EXPAND_AS_NECESSARY)
    
    ###
    #   Forming the ellipse
    ###
    # Image, select type, origin X, origin Y, width, height
    # pdb.gimp_image_select_ellipse(image, 0, 0, 0, image.width, image.height)
    # Fill mode, paint mode, opacity, threshold, sample merged, x, y
    # pdb.gimp_edit_fill(new_layer, 0)


    pdb.gimp_display_new(image)
    print("Ending...")
 
register(
        "python_fu_planetary_producer",
        "Generates a randomized planet-esque circle",
        "Generates a randomized planet-esque circle",
        "Jacob Larson",
        "Jacob Larson",
        "2018",
        "<Image>/Filters/Generate",
        "RGB*, GRAY*",
        [
            (PF_INT, "planet_radius", "Maximum Width", 500),
        ],
        [],
        plugin_main)
 
main()