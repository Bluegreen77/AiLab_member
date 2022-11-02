from os import walk
import os
import pandas as pd

def FileList(TPath, RPath, RName):
    FName = []

    for (dirpath, dirnames, filenames) in walk(TPath):
        for file in filenames:
            FName.append(file)
        break

    dict = {'Image_No': FName}
    df = pd.DataFrame(dict)
    df.to_excel(RPath + "/" + "{}.xlsx".format(RName))

TPath = "./image"     # 파일이 들어있는 폴더
RPath = "./result"  # xlsx을 저장할 폴더
RName = "fish_list" # xlsx 파일의 이름
try:
    if not os.path.exists(RPath):
        os.makedirs(RPath)
except OSError:
    print("Error: Cannot create the directory {}".format(RPath))

FileList(TPath, RPath, RName)