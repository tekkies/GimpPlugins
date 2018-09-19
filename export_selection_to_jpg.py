#!/usr/bin/python

from gimpfu import *
import datetime


def python_export_selection_to_jpg(timg, tdrawable):
    pdb.gimp_edit_copy(timg.active_layer)
    tempImage = pdb.gimp_edit_paste_as_new()
    layer = pdb.gimp_image_flatten(tempImage)
    timeText = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    outputFile = timg.filename + '.' + timeText + ".jpg"
    pdb.file_jpeg_save(tempImage, layer, outputFile, outputFile, 0.7, 0, 0, 0, "", 0, 0, 0, 0)
    pdb.gimp_image_delete(tempImage)


register(
    "python_fu_export_selection_to_jpg",
    "Exports the current selection (or whole image) as a new file",
    "Exports the current selection (or whole image) as a new file.  The exported file name is based on the original image file name and the time the export occurred.",
    "Andy Joiner",
    "Andy Joiner",
    "2018",
    "<Image>/Select/Export selection to jpg",
    "RGB*, GRAY*",
    [],
    [],
    python_export_selection_to_jpg)

main()
