# -*- coding: utf-8 -*-
"""MiniProject5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A3c-PJn6oInxzPu65dAD8_xXALMNbzX1
"""

!sudo apt install tesseract-ocr
!pip install pytesseract
!pip install Pillow==9.0.0
!pip install gTTS

import pytesseract
from PIL import Image
import gtts

img = Image.open('/content/shakespeare.png')
print(img)

result = pytesseract.image_to_string(img)
print(result)
tts = gtts.gTTS(result)
tts.save("hello.mp3")

