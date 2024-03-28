from rembg import remove
import easygui
from PIL import Image

inputpath = easygui.fileopenbox(title='Select image file')
outputpath =easygui.filesavebox(title='save file to')
input = Image.open(inputpath)
output = remove(input)
output.save(outputpath)