#!/usr/bin/python
 
from gimpfu import *
 
def plugin_main(image, drawable, planet_radius, hue, saturation, cloud_detail, mblur_distance, tilt, shift, shadow_color):

    # todo: make number of planets to generate adjustable

    image_height = planet_radius * 2
    image_width = planet_radius * 2

    ###
    #   Image and base layer initiation
    ###
    # Width, height, image-type
    image = pdb.gimp_image_new(image_width, image_height, RGB)

    # Undo grouping start
    pdb.gimp_image_undo_group_start(image)

    clouds_layer = pdb.gimp_layer_new(image, image.width, image.height, RGBA_IMAGE, "Clouds", 100, NORMAL_MODE)
    pdb.gimp_image_insert_layer(image, clouds_layer, None, -1)

    # Image, select type, origin X, origin Y, width, height
    pdb.gimp_image_select_ellipse(image, 0, 0, 0, image.width, image.height)

    pdb.gimp_context_set_foreground(shadow_color)

    pdb.gimp_edit_fill(clouds_layer, 0)

    ###
    #   Clouds layer with blur
    ###
    # Image, width, height, type, name, opacity, effect
    new_layer = pdb.gimp_layer_new(image, image.width, image.height, RGBA_IMAGE, "Background", 100, NORMAL_MODE)
    # Image, layer, parent, position
    pdb.gimp_image_insert_layer(image, new_layer, None, -1)

    # Image, drawable, tilable, turbulent, seed, detail, xsize, ysize
    pdb.plug_in_solid_noise(image, new_layer, 0, 0, 0, 1, cloud_detail, cloud_detail)

    # Image, layer, distance, direction
    pdb.plug_in_shift(image, new_layer, shift, 1)

    # Image, layer, sizeX, sizeY, mode
    pdb.plug_in_gauss(image, new_layer, 7, 7, 0)

    # Image, layer, mode, distance, angle, centerX, centerY
    pdb.plug_in_mblur(image, new_layer, 0, mblur_distance, 180 + tilt, 0, 0)

    # Layer, hue, saturation, lightness
    pdb.gimp_colorize(new_layer, hue, saturation, 0)

    ###
    #   Cleanup
    ###
    # Image, layer, type
    final_layer = pdb.gimp_image_merge_down(image, new_layer, 0)

    # Deselect
    pdb.gimp_selection_none(image)

    # Undo grouping end
    pdb.gimp_image_undo_group_end(image)

    # Display
    pdb.gimp_display_new(image)
 
register(
        "python_fu_planetary_producer",
        "Generates a randomized gas planet-esque circle",
        "Generates a randomized gas planet-esque circle",
        "Jacob Larson",
        "Jacob Larson",
        "2018",
        "<Image>/Filters/Render/Gas Planet...",
        "RGB*, GRAY*",
        [
            (PF_SPINNER, "planet_radius", "Radius:", 500, (1, 10000, 1)),  # alias PF_ADJUSTMENT
            (PF_SLIDER, "hue", "Hue:", 180, (0, 360, 10)),
            (PF_SLIDER, "saturation", "Saturation:", 50, (0, 100, 1)),
            (PF_SLIDER, "cloud_detail", "Cloud Detail:", 5.0, (2.0, 25.0, 1.0)),
            (PF_SLIDER, "mblur_distance", "Shadow Size:", 80, (50, 200, 5)),
            (PF_SLIDER, "tilt", "Tilt:", 0, (-20, 20, 1)),
            (PF_SLIDER, "shift", "Shift Amount:", 100, (0, 200, 1)),
            (PF_COLOR, "shadow_color", "Shadow Color:", (0, 0, 0)),
        ],
        [],
        plugin_main)
 
main()