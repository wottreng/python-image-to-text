#!/usr/bin/python3

# https://github.com/JaidedAI/EasyOCR
# https://pytorch.org/

import os
from easyocr import Reader

pathToImage = f"{os.getcwd()}/someImage.png"

# need to run only once to load model into memory
# if you dont have the pretrained models easyOCR will fetch them with 'download_enabled'
reader = Reader(['en'], gpu=False, model_storage_directory=f"{os.getcwd()}/.EasyOCR/",download_enabled=True)
result = reader.readtext(pathToImage)
print(result)
print("-------------")
textFound = []
for x in result:
    print(f"box:{x[0]}") #bounding box, text, confidence
    print(f"text:{x[1]}")
    print(f"confidence:{round(x[2],2)}")

print('done')
