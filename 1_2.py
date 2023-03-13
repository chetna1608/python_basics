import pickle 

def storeData():
    
    student1 = {
        "name" : "ABC",
        "roll" : 1001,
        "marks" : {
            "python_mark" : 99,
            "TOC_mark" : 89,
            "OS_mark" : 78
        }
    }

    student2={
        "name" : "EFG",
        "roll" : 1002,
        "marks" : {
            "python_mark" : 69,
            "TOC_mark" : 59,
            "OS_mark" : 48
        }
    }

    student3={
        "name" : "HIJ",
        "roll" : 1003,
        "marks" : {
            "python_mark" : 91,
            "TOC_mark" : 69,
            "OS_mark" : 71
        }
    }

    student4={
        "name" : "LMN",
        "roll" : 1004,
        "marks" : {
            "python_mark" : 89,
            "TOC_mark" : 78,
            "OS_mark" : 67
        }
    }
    
    Studentdata={}
    Studentdata[1001]=student1
    Studentdata[1002]=student2
    Studentdata[1003]=student3
    Studentdata[1004]=student4
    
    dbfile=open('StudentPickle','wb')
    pickle.dump(Studentdata,dbfile)
    dbfile.close()

def loadData():
    dbfile=open('StudentPickle','rb')
    Studentdata=pickle.load(dbfile)
    for keys in Studentdata:
        print(keys,'=>',Studentdata[keys])
    dbfile.close()

if __name__=='__main__':
    storeData()
    loadData()