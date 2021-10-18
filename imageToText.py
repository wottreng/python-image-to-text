# https://github.com/JaidedAI/EasyOCR
# https://pytorch.org/

import os
from easyocr import Reader
import torch
import fileTools
ft = fileTools.fileTools()

debug = False

print(f"GPU available: {torch.cuda.is_available()}")

# pathToImage = f"{os.getcwd()}/receipt.png"
pathToImage = f"{os.getcwd()}/pics/a.png"

# need to run only once to load model into memory
# if you dont have the pretrained models easyOCR will fetch them with 'download_enabled'
reader = Reader(['en'], gpu=True, model_storage_directory=f"{os.getcwd()}/.EasyOCR/",download_enabled=True)
# here is where the work is done:
result = reader.readtext(pathToImage)

print("-------------")
textFound = []
for x in result:
    textFound.append(x[1])
    if debug:
        print(f"box:{x[0]}")
        print(f"text:{x[1]}")
        print(f"confidence:{round(x[2],2)}")

print('OCR finished')
ft.writeListToFile(textFound, filename="output.txt")
