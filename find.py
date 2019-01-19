import os

class FileSearcher:
    def __init__(self):
        self.files=[]
        os.chdir("/")
        self.loadAllFiles("/")
        self.showStats()

    def showStats(self):
        print("len(self.files)=",len(self.files))

    def similarity(self,string1,string2):
        m=min(len(string1),len(string2))
        l=range(m)
        if m>2:
            l.remove(0)
            l.remove(1)
            print(l)
        l.reverse()
        for i in l:
            for c1 in range(i):
                for c2 in range(i):
                    if string1[c1:c1+i]==string2[c2:c2+i]:
                        print(string1[c1:c1+i])
                        return self.similarity(string1[:c1],string2[:c2])+i+self.similarity(string1[c1+i+1:],string2[c2+i+1:])
        return 0

    def loadAllFiles(self,directory,state=0,max_state=10):
        elements=os.listdir(directory)
        print("elements=",elements)
        print("directory=",directory)
        for element in elements:
            os.chdir(directory)
            if os.path.isfile(element):
                self.files.append(element)
            if os.path.isdir(element) and state<max_state:
                print("directory+element+/=",directory+element+"/")
                try:
                    self.loadAllFiles(directory+element+"/",state+1)
                except:
                    print("denied")

main=FileSearcher()
print("")
print(main.similarity("j'ai manger beaucoup","je veux manger les moches"))
