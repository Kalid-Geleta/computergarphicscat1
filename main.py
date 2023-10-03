
import pandas as pd
import os

def returntemp(file,path):
    filename = (os.fsdecode(file))
    temp = pd.read_json(path + filename, lines=True)
    return temp
def returnoutname(temp,delimiter):
    outname = str.join(temp['locale'].iloc[0]).split(delimiter)
    outname = "C:/Users/User/PycharmProjects/pythonProject1/venv/xlsxfiles/" + "en" + "-" + outname[0] + ".xlsx"
    return outname

def funlogic():
        str=""


        dfp = pd.read_json("C:/Users/User/PycharmProjects/pythonProject1/venv/data/en-US.jsonl", lines=True)

        directory = os.fsencode("C:/Users/User/PycharmProjects/pythonProject1/venv/data/")
        logic =True
        for file in os.listdir(directory):
            if(logic):
                logic=False
                continue
            else:

                filename = (os.fsdecode(file))
                temp=pd.read_json("C:/Users/User/PycharmProjects/pythonProject1/venv/data/"+ filename, lines=True)
                outname = str. join(temp['locale'].iloc[0]).split('-')
                outname="C:/Users/User/PycharmProjects/pythonProject1/venv/xlsxfiles/"+"en"+"-"+outname[0]+".xlsx"
                temp['utt']=dfp['utt']

                temp[['id','utt','annot_utt']].to_excel(outname)

                print(outname)







if __name__ == '__main__':
    funlogic()

