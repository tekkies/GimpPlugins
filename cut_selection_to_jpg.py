#!/usr/bin/python

from gimpfu import *
import datetime


def python_cut_selection_to_jpg(timg, tdrawable):
    pdb.gimp_edit_cut(timg.active_layer)
    tempImage = pdb.gimp_edit_paste_as_new()
    layer = pdb.gimp_image_flatten(tempImage)
    timeText = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    outputFile = timg.filename + '.' + timeText + ".jpg"
    pdb.file_jpeg_save(tempImage, layer, outputFile, outputFile, 0.8, 0, 0, 0, "", 0, 0, 0, 0)
    pdb.gimp_image_delete(tempImage)


register(
    "python_fu_cut_selection_to_jpg",
    "Cuts the current selection (or whole image) and saves as a new jpg file",
    "Cuts the current selection (or whole image) and saves as a new jpg file.  The exported file name is based on the original image file name and the time the export occurred.",
    "Andy Joiner",
    "Andy Joiner",
    "2018",
    "<Image>/Select/Cut selection to jpg",
    "RGB*, GRAY*",
    [],
    [],
    python_cut_selection_to_jpg)

main()
