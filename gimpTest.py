#!/usr/bin/python
 
from gimpfu import *
 
def plugin_main(image, drawable, planet_radius):
    print("Starting...")

    # todo: make number of planets to generate adjustable
    # todo: allow addition of colors, whether random or custom

    image_height = planet_radius * 2
    image_width = planet_radius * 2

    ###
    #   Image and base layer initiation
    ###
    # Width, height, image-type
    image = pdb.gimp_image_new(image_width, image_height, RGB)
    clouds_layer = pdb.gimp_layer_new(image, image.width, image.height, RGBA_IMAGE, "Clouds", 100, NORMAL_MODE)
    pdb.gimp_image_insert_layer(image, clouds_layer, None, -1)

    # Image, select type, origin X, origin Y, width, height
    pdb.gimp_image_select_ellipse(image, 0, 0, 0, image.width, image.height)
    pdb.gimp_edit_fill(clouds_layer, 0)

    ###
    #   Clouds layer with blur
    ###
    # Image, width, height, type, name, opacity, effect
    new_layer = pdb.gimp_layer_new(image, image.width, image.height, RGBA_IMAGE, "Background", 100, NORMAL_MODE)
    # Image, layer, parent, position
    pdb.gimp_image_insert_layer(image, new_layer, None, -1)

    # todo: make parameters for solid noise customizable
    # Image, drawable, tilable, turbulent, seed, detail, xsize, ysize
    pdb.plug_in_solid_noise(image, new_layer, 0, 0, 0, 1, 4.0, 4.0)

    # Image, layer, distance, direction
    pdb.plug_in_shift(image, new_layer, 100, 1)
    #Image, layer, sizeX, sizeY, mode
    pdb.plug_in_gauss(image, new_layer, 7, 7, 0)

    # Image, layer, mode, distance, angle, centerX, centerY
    pdb.plug_in_mblur(image, new_layer, 0, 80, 160, 0, 0)

    # Layer, hue, saturation, lightness
    pdb.gimp_colorize(new_layer, 0, 50, 0)
    # Image, layer, type
    final_layer = pdb.gimp_image_merge_down(image, new_layer, 0)


    pdb.gimp_selection_none(image)


    pdb.gimp_display_new(image)
    print("Ending...")
 
register(
        "python_fu_planetary_producer",
        "Generates a randomized planet-esque circle",
        "Generates a randomized planet-esque circle",
        "Jacob Larson",
        "Jacob Larson",
        "2018",

        "<Image>/Filters/Generate", # todo: for release change to: "<Image>/Filters/Render/Generate/",
        "RGB*, GRAY*",
        [
            (PF_INT, "planet_radius", "Maximum Width", 500),
        ],
        [],
        plugin_main)
 
main()