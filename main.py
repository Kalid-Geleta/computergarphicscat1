import pandas as pd
import os
import json
import pprint
def maketojsonfile(path, dataf):
    dataf.to_json(path, orient='records')


def writetojsonlfun(pathtodestination,jsonfile,typeofprocess):
    with open(pathtodestination[:-11]+pathtodestination[-11:-6].split("-")[0]+typeofprocess+".jsonl", 'w') as outfile:
        for entry in jsonfile:
            json.dump(entry, outfile)
            outfile.write('\n')
def givetheoutputdestiniationfromsource(path):
    return path[:-16]+"data1"+"/"+path[-11:-6]+".jsonl"
def returnjson(dtf):
   return json.loads(dtf.to_json(orient='records'))
def devtraintest(pathforsource):
    df = pd.read_json(pathforsource, lines=True)
    test=df.loc[(df['partition']=="test")]
    dev=df.loc[(df['partition']=="dev")]
    train=df.loc[(df['partition']=="train")]
    #print(test)
    #print(dev)
    #print(train)
    writetojsonlfun(givetheoutputdestiniationfromsource(pathforsource),returnjson(dev),"dev")
    writetojsonlfun(givetheoutputdestiniationfromsource(pathforsource), returnjson(train), "train")
    writetojsonlfun(givetheoutputdestiniationfromsource(pathforsource), returnjson(test), "test")
def devtraintestformany(baseurlwherefilesarefound,arrfordifferentlangues):
    for lang in arrfordifferentlangues :

        fullurl=baseurlwherefilesarefound+lang+".jsonl"
        devtraintest(fullurl)
        print(fullurl)

def makeonejsonlforall():
    str = ""
    concatenated_df=pd.DataFrame()
    datf=pd.DataFrame()
    dfp = pd.read_json("C:/Users/User/PycharmProjects/pythonProject1/venv/data/en-US.jsonl", lines=True)
    directory = os.fsencode("C:/Users/User/PycharmProjects/pythonProject1/venv/data/")
    logic = True
    try:
        for iter in os.listdir(directory):
            if iter:
                try:
                    for file in os.listdir(directory):
                        if (logic):
                            logic = False
                            continue
                        else:
                            if file:
                                filename = (os.fsdecode(file))
                                temp = pd.read_json("C:/Users/User/PycharmProjects/pythonProject1/venv/data/" + filename, lines=True )
                                temp['utt'] = dfp['utt']
                                concatenated_df = pd.concat([concatenated_df, temp], axis=0,ignore_index=True)
                                concatenated_df = concatenated_df.assign(id=concatenated_df.index)
                                maketojsonfile("C:/Users/User/PycharmProjects/pythonProject1/venv/alllangjson.json",concatenated_df)
                                #concatenated_df.append(temp)

                except:
                    continue

        print(concatenated_df)
    except:
        print("-----------------------------------------------------------------------------------------")










def enxxfunlogic():
        str=""
        dfp = pd.read_json("C:/Users/User/PycharmProjects/pythonProject1/venv/data/en-US.jsonl", lines=True)
        directory = os.fsencode("C:/Users/User/PycharmProjects/pythonProject1/venv/data/")
        logic =True
        try:
            for file in os.listdir(directory):
                if file:
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
        except:
            print("-----------------------------------------------------------------------------------------")





def jarvis():
    bol=True
    times=0
    while bol:
        if times==0:
            chos=input("hi i  am jarvis i am cat 1 navigator  what question you want to see enter one of this  1,2,3\n")
        else :
            chos = input("hey this is jarvis again there  are only three options namely  1,2,3 try again!\n")
        times += 1
        match chos:
            case "1":
                bol=False
                print("please check my xlsxfiles folder when i am done ")
                enxxfunlogic()
                print("Cool i am done with task")

            case "2":
                bol = False
                print("please check my data1 folder when i am done ")
                base=input("please input the base url\n")
                arr=input("enter language and country in capital separated by comma\n")
                thearr=arr.split(',')
                devtraintestformany(base, thearr)
                print("Cool i am done with task")
            case "3":
                bol = False
                print("you can see  what i have done in the console thanks! ")
                makeonejsonlforall()
                print("Cool i am done with task")
            case _:
                print("Oops!")
                continue













if __name__ == '__main__':
    #enxxfunlogic()
    #devtraintestformany("C:/Users/User/PycharmProjects/pythonProject1/venv/data/",["sw-KE","de-DE","en-US"])
   # makeonejsonlforall()
   jarvis()
