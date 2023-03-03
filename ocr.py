import os
import sys
import pyocr
import pyocr.builders
import cv2 as cv
from PIL import Image

def img_ocr():
    pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    tools = pyocr.get_available_tools()
    print(tools)
    tool = tools[0]

    img_path = 'image/name.png'
    img = Image.open(img_path)
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    text = tool.image_to_string(img,lang="jpn",builder=builder)

    print(text)