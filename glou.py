#Variables#

rep="/Users/olivierpartensky/Programs/Python/First Repository/"

BLACK  = (  0,  0,  0)
WHITE  = (255,255,255)
RED    = (255,  0,  0)
GREEN  = (  0,255,  0)
BLUE   = (  0,  0,255)
CYAN   = (  0,255,255)
PURPLE = (255,  0,255)
YELLOW = (255,255,  0)
BROWN  = (150, 75,  0)
ORANGE = (255,140,  0)
RANDOM = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#Functions#

def remove_none(list):
    if type(list) != list:
        return
    list[:] = [i for i in list if i is not None]
    for e in list:
       remove_none(e)

def remove_void(list):
    while list.count([])>0:
        list.remove([])

def remove(element,list):
    e=element
    while list.count(e)>0:
        list.remove(e)

def indexes(element,list):
    l=list[:]
    indexes=[]
    i=0
    while l.count(element)>0:
        indexs.append(l.index(element)+i)
        l.remove(element)
        i+=1
    return indexes

def after(list,content):
    l=list[:]
    c=content[:]
    after=[]
    for e in l:
        for i in range(len(c)-1):
            if e==c[i]:
                after.append(c[i+1])
    return after

def extra_dedent(object):
    o=object[:]
    m=0
    while m!=len(o):
        m=len(o)
        o=extra_dedent(o)
    return o

def list_frequency(list):
    l=list
    s=list(set(l))
    d={}
    for i,v in enumerate(s):
        s[i]=[s[i],l.count(v)]
    r=sorted(s,key=lambda a: a[1])
    r.reverse()
    return r

def display(value,b=1):
    if b:
        print(value)

def try_out(name,default=None):
    file=get(name)
    try:
        return file[0]
    except:
        return default

def cut(sublist,list):
    output=[]
    j=0
    start=0
    bool=False
    done=False
    i=0
    while i<len(sublist)-len(list[j])+1 and not done:
        if sublist[i:i+len(list[j])]==list[j]:
            if j<len(list)-1:
                if bool:
                    output.append(sublist[start:i])
                start=i+len(list[j])
                j+=1
                bool=True
            else:
                if bool and len(sublist[start:i])>0:
                    output.append(sublist[start:i])
                done=True
        i+=1
    return output

def substract_lists(list1,list2):
    n=0
    i=0
    while i<len(list1) and n<len(list2):
        if list1[i]==list2[n]:
            del list1[i]
            n+=1
            i-=1
        i+=1
    output=list1[:]
    return output

def reduct(list):
    try:
        for i in list:
            while list.count(i)>1:
                list.remove(i)
        return list
    except:
        Erreur("reduct")

def common_sequence(list1,list2):
    list1.lower()
    list2.lower()
    sequences=[]
    m=min(len(list1),len(list2))
    for t in range(0,m):
        for i in range(len(list1)-t):
            for j in range(len(list2)-t):
                if list1[i:i+t+1]==list2[j:j+t+1]:
                    sequences.append(list1[i:i+t+1])
    sequences.reverse()
    return sequences

def similarity(list1,list2):
    sequences=common_sequence(list1,list2)
    m=min(len(list1),len(list2))
    try:
        similarity=(sum([len(i) for i in sequences])-1)/len(sequences)
        return similarity
    except:
        return 0

def rsb(c,C):
    c.lower()
    C.lower()
    m=min(len(c),len(C))
    p=float(len(c)+len(C))/2
    for t in range(0,m):
        l=m-1-t
        for i in range(len(c)-l):
            for j in range(len(C)-l):
                if c[i:i+l+1]==C[j:j+l+1]:
                    return l/p
    return 0

def rsb2(c1,c2):
    l1=len(c1)
    l2=len(c2)
    m=min(l1,l2)
    list=list(range(m))
    if len(list)!=0:
        del list[0]
    list.reverse()
    for i in list:
        for f in range(l1-i+1):
            for g in range(l2-i+1):
                if c1[f:f+i+1]==c2[g:g+i+1]:
                    return rsb2(c1[:f],c2[:g])+i+1+rsb2(c1[f+i+1:],c2[g+i+1:])
    return 0



def rsb4(c1,c2):
    l1=len(c1)
    l2=len(c2)
    m=min(l1,l2)
    list=list(range(m))
    list.reverse()
    for i in list:
        for f in range(l1-i+1):
            for g in range(l2-i+1):
                if c1[f:f+i+1]==c2[g:g+i+1]:
                    return rsb2(c1[:f],c2[:g])+i+rsb2(c1[f+i+1:],c2[g+i+1:])
    return 0

def rsb5(c1,c2):
    i=rsb4(c1,c2)
    m=(len(c1)+len(c2))/2
    return i/m

#Select#

def select(element,list):
    l=list[:]
    e=element
    r=0
    m=0
    for i in range(len(l)):
        n=rsb5(e,l[i])
        if n>r:
            r=n
            m=i
    return m

def select_list(element,list):
    l=list[:]
    e=element
    m=0
    r=0
    for i,u in enumerate(l):
        p=0
        for j,v in enumerate(l[i]):
            n=rsb3(e,v)
            p+=n
        if p>m:
            m=p
            r=i
    return r

def affiliation(element,list):
    l=list[:]
    e=element
    r=0
    m=0
    for i in range(len(l)):
        n=rsb3(e,l[i])
        if n>r:
            r=n
            m=i
    return r

def select_language(text,languages):
    a=[]
    for language in languages:
        a.append(belong(text,language))
    maxi=max(a)
    i=a.index(maxi)
    del a[i]
    relevance=maxi-max(a)
    return (i,maxi,relevance)

def belong(e,l):
    e=splitwords(e)
    s=replace(e,l)
    return 1-len(s)/len(e)

def belong(element,list):
    l=list[:]
    e=splitwords(element)
    n=0
    for v in e:
        v=v.lower()
        n+=belonging(v,l)
    return n/len(e)

def sigmoid(x):
    e=math.exp(x)
    y=1/(1+e**(-x))
    return y

def sig(x,_lambda=10):
    try:
        x=(x*2-1)
        y=1/(1+math.exp(-x*_lambda))
        return y
    except:
        return 0

def answer(string):
    sentences=get("messenger2")[0]
    return answer4(string,sentences)

def answer2(input,sentences):
    dictionnary={}
    l=len(sentences)
    for i in range(l):
        dictionnary[str(rsb(sentences[i],input))]=i
        progression(i,0,l)
    relevance=list(dictionnary)
    relevance.sort()
    relevance.reverse()
    probability=[]
    for i in range(len(list)):
        probability.append(relevance[i]/2**i)
    r=random.randfloat(0,len(sum(probability)))
    i=0
    n=0
    while i<r:
        i+=probability[n]
        n+=1
    Sortie=sentences[dictionnary[relevance[i]]+1]
    return Sortie

def answer3(input,sentences,Bool=False,relevance=0.5):
    e=input
    P=sentences
    l=len(P)
    v=0
    i=0
    p=0
    while p<l:
        n=rsb5(P[p],e)
        if n>v:
            i=p
            v=n
        p+=1
    print(v,relevance)
    try:
        if Bool:
            if v>relevance:
                return sentences[i+1]
            else:
                #return sentences[i+1]+"\n relevance: "+str(v)
                return sentences[i+1]
        if v>relevance:
            return sentences[i+1]
        else:
            return None
    except:
        return None


def answer5(input,sentences):
    e=input
    P=sentences
    v=0
    for i,a in enumerate(P):
        r=rsb5(a,e)
        if r>v:
            p=i
            v=r
    return [P[p],P[p+1],p,v]


def ChatBox2():
    structure=get("structure")
    remove_none(structure)
    #sentences=sentencer(structure)
    Historique=outVariable("Messenger")
    sentences=[]
    for Message in Historique:
        if Message[0]=="P":
            sentences.append(Message[10:])
    Bot="Bonjour"
    print(Bot)
    User=str(input(""))
    while User!=Ressemblance(User,"au revoir")<2:
        Bot=answer3(User,sentences)
        print(Bot)
        User=str(input(""))


def answer_structure(string):
    structure=outVariable("structure")
    remove_none(structure)
    sentences=sentencer(structure)
    if sentences.count(string)==0:
        return None
    else:
        answers=[]
        indexs=get_indexs(string,sentences)
        for i in indexs:
            answers.append(sentences[i+1])
        answer=answers[random.randint(0,len(answers)-1)]
        return answer

#

def sentence(structure):
    sentences=outVariable("sentences")
    if sentences==None:
        sentences=dedent(dedent(structure))
        i=0
        while i<len(sentences):
            sentences[i]="".join(sentences[i])
            i+=1
    return sentences

def reverse_matrix(matrix):
    reversed=[[None]*len(matrix) for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            reversed[i][j]=matrix[j][i]
    return reversed



def dict(list):
    dictionnary={}
    for i in list:
        dictionnary[i]=None
    return dictionnary

def splitBalises(string):
    return extract(string,Tout,">","<")

def Comparerlanguage(string,language):
    number=0
    Intrus=[]
    for word in language:
        if string.count(word)>0:
            Intrus.append(word*string.count(word))
    return Intrus

def add_dictionnary(string,dictionnary):
    reduction=reduct(string)
    for word in reduction:
        if dictionnary.count(word)==0:
            dictionnary[word]=reduction.count(word)
        else:
            dictionnary[word]=dictionnary[word]+reduction.count(word)
    return dictionnary






def Validitélanguage(string,language):
    Exceptions=0
    for languageConsidérée in languages:
        if languageConsidérée!=language:
            Exceptions+=len(Comparerlanguage(string,languageConsidérée))
    Validité=int(len(Comparerlanguage(string,language))/len(string)*100)
    if Validité>5 and Exceptions==0:
        return True
    else:
        return False



def Erreur(Fonction):
    global AfficherErreur
    if AfficherErreur:
        print("La fonction",Fonction,"n'a pas pue être exécutée.")
    Erreurs.append(Fonction)
    stock_text(Fonction+" ","Erreurs","a")

def Numerer(word):
    try:
        word=word.lower()
        Valeur=float(0)
        for j in range(0,len(word)):
            Valeur=AlphabetComplet.index(word[j])/len(AlphabetComplet)**(j+1)+Valeur
        return Valeur
    except:
        Erreur("Numerer")

def Classer(word,list):
    try:
        MV=Numerer(word)
        l=0
        Recherche=True
        while Recherche:
            if l<len(list):
                if Numerer(list[l])>MV:
                    Recherche=False
                else:
                    l=l+1
            else:
                Recherche=False
        if l<len(list):
            if Numerer(list[l])>MV:
                Sortie=list[0:l]
                Sortie.append(word)
                Sortie.extend(list[l:len(list)])
                list=Sortie[:]
        else:
            list.append(word)
        return list
    except:
        Erreur("Classer")

def syllables(word):
    word=word.lower()
    string=[]
    Début=0
    if consonnant.count(word[0])==1:
        bool=True
    else:
        bool=False
    for i in range(len(word)-1):
        if consonnant.count(word[i])==1:
            if Voyelles.count(word[i+1])==1:
                if bool==False:
                    string.append(word[Début:i])
                    Début=i
                else:
                    bool=False
        if word[i]==" ":
            string.append(word[Début:i])
            Début=i+1
            if consonnant.count(word[i+1])==1:
                bool=True
            else:
                bool=False
    string.append(word[Début:])
    return string


def CompterSyllables(word):
    try:
        word=word.lower()
        if word[-1]=="e" or word[-2:]=="e.":
            Syllables=-1
        else:
            Syllables=0
        NouvelleVoyelle=False
        n=0
        for Lettre in word:
            AncienneVoyelle=NouvelleVoyelle
            NouvelleVoyelle=False
            for Voyelle in Voyelles:
                if Lettre==Voyelle:
                    NouvelleVoyelle=True
            if Lettre=="y":
                VoyelleSyllable=0
                for Voisin in Voisinage(n,word):
                    for VoyelleY in Voyelles:
                        if Voisin==VoyelleY:
                            VoyelleSyllable=VoyelleSyllable+1
                if VoyelleSyllable==0:
                    Syllables=Syllables+1
            if NouvelleVoyelle==True and AncienneVoyelle==False:
                Syllables=Syllables+1
            n=n+1
        return Syllables
    except:
        Erreur("CompterSyllables")

def Associer(list,string):
    try:
        Sequence=[]
        for Element in list:
            for i in range(0,len(string)):
                if string[i].count(Element)==1:
                    Sequence.append(i)
        return Sequence
    except:
        Erreur("Associer")



def RechercherUrl(search):
    try:
        url = "https://www.startpage.com"
        browser = webdriver.Chrome(executable_path="/Applications/chromedriver")
        browser.get(url)
        search_box=browser.find_element_by_id("query")
        search_box.send_keys(search)
        search_box.submit()
        try:
            links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")
        except:
            links = browser.find_elements_by_xpath("//h3//a")
        Urls = []
        for link in links:
            href = link.get_attribute("href")
            Urls.append(href)
        browser.close()
        return Urls
    except:
        Erreur("RechercherUrl")

def stock_site(Url,filetext,Mode):
    try:
        html = requests.get(Url).content
        unicode_str = html.decode("utf8")
        encoded_str = unicode_str.encode("utf8",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all('p')
        list=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        y=" ".join(list)
        print(y)
        file = open(filetext+".txt", Mode)
        file.write(str(y))
        file.close()
    except:
        Erreur("stock_site")

def get_site(Url):
    try:
        html = requests.get(Url).content
        unicode_str = html.decode("utf8")
        encoded_str = unicode_str.encode("utf8",'ignore')
        news_soup = BeautifulSoup(encoded_str, "html.parser")
        a_text = news_soup.find_all('p')
        list=[re.sub(r'<.+?>',r'',str(a)) for a in a_text]
        y=" ".join(list)
        return y
    except:
        Erreur("get_site")

def ConvertirlistEnnumber(list):
    try:
        string=""
        for i in list:
            string+=str(i)
        return int(string)
    except:
        Erreur("ConvertirlistEnnumber")

def PermuterAléatoirement(input):
    Sortie=[]
    while input!=[]:
        i=random.randint(0,len(input)-1)
        Sortie.append(input[i])
        del input[i]
    return Sortie


def dedentExcept(string):
    Sortie=[]
    for i in string:
        if type(i) is list or type(i) is string:
            for j in i:
                Sortie.append(j)
        else:
            Sortie.append(i)
    return Sortie

def dedent(string):
    Sortie=[]
    for i in string:
        for j in i:
            Sortie.append(j)
    return Sortie

def stock_text(string,Nomfile,Mode):
    try:
        with open(Nomfile+".txt", Mode, encoding="utf-8") as file:
            file.write(string)
    except:
        Erreur("stock_text")

def replace(dictionnary1,dictionnary2):
    try:
        Nouveaudictionnary=[]
        for word in dictionnary1:
            if dictionnary2.count(word)==0:
                Nouveaudictionnary.append(word)
        return Nouveaudictionnary
    except:
        Erreur("replace")

def TraduiretextEnstring(Nom,Mode):
    try:
        with open(Nom+".txt", 'r', encoding="utf-8") as filedictionnarytext:
             stringdictionnarytext=filedictionnarytext.read()
             dictionnary=stringdictionnarytext.split(" ")
        try:
            with open(Nom, Mode+'b') as filedictionnarystring:
                dictionnarystringPickler = pickle.Pickler(filedictionnarystring)
                dictionnarystringPickler.dump(dictionnary)
        except:
            print("Ecriture impossible.")
    except:
        Erreur("ConvertirtextEnstring")

def TraduiestringEntext(Nom,Mode):
    try:
        with open(Nom, 'rb') as filedictionnarystring:
            dictionnarystringDepickler = pickle.Unpickler(filedictionnarystring)
            dictionnarystring = dictionnarystringDepickler.load()
            dictionnary=" ".join(dictionnarystring)
        with open(Nom+".txt", Mode, encoding="utf-8") as filedictionnarytext:
             stringdictionnarytext=filedictionnarytext.write(dictionnary)
    except:
        Erreur("ConvertirstringEntext")

def splitParagraphes(string):
    try:
        return [string]
    except:
        Erreur("splitParagraphes")

def split_sentences(string):
    try:
        string=[]
        sentenceBool=False
        DebutBool=False
        for i in range(len(string)):
            sentenceBool=False
            if AlphabetComplet.count(string[i])==1 or Ponctuation.count(string[i])==1 or string[i]==" " or numbers.count(string[i])==1:
                sentenceBool=True
            else:
                sentenceBool=False
                DebutBool=False
            if i<len(string)-2:
                if CaractèresSpéciaux.count(string[i])==1 and CaractèresSpéciaux.count(string[i+1])==1:
                    sentenceBool=False
                    DebutBool=False
            if MajusculesComplètes.count(string[i])==1:
                DebutBool=True
                sentenceBool=True
                sentence=""
            if sentenceBool:
                sentence+=string[i]
            if DebutBool and sentenceBool and Fin.count(string[i])==1:
                if len(sentence)>=3:
                    string.append(sentence)
                DebutBool=False
                sentenceBool=False
        return string
    except:
        Erreur("split_sentences")

def AssocierCaractère(Caractère):
    if AlphabetComplet.count(Caractère)==1:
        return "AlphabetComplet"
    elif CaractèresSpéciaux.count(Caractère):
        return "CaractèresSpéciaux"
    else:
        return "Autre"

def splitelements(string):
    try:
        Début=0
        string=[]
        for i in range(len(string)-1):
            if AssocierCaractère(string[i])!=AssocierCaractère(string[i+1]):
                string.append(string[Début:i+1])
                Début=i+1
        string.append(string[-1])
        return string
    except:
        Erreur("splitelements")


def splitwordsRaté(string):
    try:
        string=string.lower()
        for i in CaractèresSpéciaux:
            string=string.replace(i," ")
        for i in numbers:
            string=string.replace(i," ")
        string=string.replace("'"," ")
        return string[0:len(string)-1].split(" ")
    except:
        Erreur("splitwordsRaté")

def splitwords(string):
    try:
        string=string.lower()
        string=[]
        wordBool=False
        DébutBool=False
        for i in range(len(string)):
            wordBool=False
            if MinusculesComplètes.count(string[i])==1:
                wordBool=True
                if DébutBool==False:
                    DébutBool=True
                    word=""
            else:
                wordBool=False
            if wordBool:
                word+=string[i]
            if DébutBool and wordBool==False:
                if len(word)>=2 and CompterSyllables(word)>0:
                    string.append(word)
                DébutBool=False
                wordBool=False
        return string
    except:
        Erreur("splitwords")

def dictionnaryDesSynos(string):
    string=[]
    wordBool=False
    for i in range(len(string)-5):
        if string[i:i+1]=="\">":
            wordBool=True
            Début=i+2
        if wordBool and AlphabetComplet.count(string[i])==0:
            wordBool=False
        if string[i:i+3]=="</a>" and wordBool:
            string.append(string[Début:i-1])
            wordBool=False
    print(string)



def GénérerConditions():
    Conditions=[]
    return Condtions


def extractRaté(string,group,Début,Fin):
    string=str(string)
    Extraits=[]
    Bool=False
    DébutBool=True
    début=0
    element=""
    group=str(group)
    for i in range(len(string)):
        if i+len(Début)<len(string):
            if string[i:i+len(Début)]==Début and Bool==False:
                début=i+len(Début)
                DébutBool=True
        if DébutBool==True and i>=début:
            Bool=True
        if Bool==True:
            if group.count(string[i])>0:
                element+=string[i]
            else:
                Bool=False
                DébutBool=False
                element=""
        if i+1+len(Fin)<len(string):
            if string[i+1:i+1+len(Fin)]==Fin and Bool==True:
                if len(element)>1:
                    Extraits.append(element)
                DébutBool=False
                Bool=False
                element=""
    return Extraits

def extract(string,group,Début,Fin):
    début=False
    string=[]
    element=""
    for i in range(len(string)-len(Fin)+1):
        if string[i:i+len(Fin)]==Fin:
            début=False
            if len(element)>0:
                string.append(element)
        if string[i:i+len(Début)]==Début:
            début=True
            element=""
            Mémoire=i
        if group.count(string[i])>0 and début:
            if i>=Mémoire+len(Début):
                element+=string[i]
        else:
            début=False
            element=""
    return string

def synonyms(word):
    synonyms=[]
    word=word.lower()
    dictionnarys=["http://www.synonyms.com/synonym.php?word="+word+"&x=0&y=0",
                   "http://www.crisco.unicaen.fr/des/synonyms/"+word,
                   "www.synonymo.fr/synonym/"+word]
    for Url in dictionnarys:
        code=get_html_code(Url)
        synonyms.extend(extract(code,MinusculesComplètes+" ","\">","</a>"))
    synonyms.sort()
    synonyms=reduct(synonyms)
    synonyms=replace(synonyms,["user","avertissement"])
    return synonyms

def definitions(word):
    definitions=[]
    word=word.lower()
    dictionnarys=["http://www.le-dictionnaire.com/definition.php?word="+word]
    for Url in dictionnarys:
        code=get_html_code(Url)
        definitions.extend(extract(code,AlphabetComplet+Ponctuation+" ","\">","</a>"))
    definitions=replace(split_sentences(" ".join(definitions)),["Conjugaison.","Calculatrice.","definition manquante ou compléter."])
    definitions=reduct(definitions)
    return definitions


def get_html_code(Url):
    uClient = uReq(Url)
    page_html = uClient.read()
    uClient.close()
    return str(BeautifulSoup(page_html, "html.parser"))



def stock(object,name,mode):
    with open(name, mode+'b') as file:
        component = pickle.Pickler(file)
        component.dump(object)

def get(name):
    with open(name, 'rb') as file:
        component = pickle.Unpickler(file)
        try:
           components=[]
           while True:
               string.append(component.load())
        except:
            return components

def get_text(name):
    with open(name+".txt", "r",encoding="utf-8") as file:
        text=file.read()
    return text

def time_left(position,start,end,starting_time,time):
    p=position
    d=start
    f=end
    td=int(starting_time)
    tp=int(time)
    return ((f-p)*(tp-td))/(p-d+1)

def progression(V,D,F,Stop=False):
    pygame.init()
    done=False
    Width=500
    Height=20
    COULEUR=GREEN
    FOND=BLACK
    size=(Width,Height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("progression")
    clock = pygame.time.Clock()
    screen.fill(FOND)
    E=(Width*V)//(F-D)
    pygame.draw.rect(screen, COULEUR, (0,0,E,Height),0)
    pygame.display.flip()
    clock.tick(1000000)
    if V>=F or done or Stop:
        pygame.quit()


#List#

def prod(list):
    number=1
    for i in list:
        number*=i
    return number

def sum(list):
    number=1
    for i in list:
        number+=i
    return number

def size(list):
    number=1
    coefficient=1
    for i in list:
        number+=i*coefficient
        coefficient*=i
    return number

#Permutation#

def add_system(progression,_system,Ajout):
    number=out_system(progression,_system)
    number=(number+Ajout)%size(_system)
    progression=enter_system(number,_system)
    return progression

def out_system(progression,_system):
    number=0
    coefficient=1
    for i in range(len(_system)):
        number+=progression[-i-1]*coefficient
        coefficient*=_system[-i-1]
    return number

def enter_system(number,_system):
    progression=[]
    coefficient=prod(_system)
    for i in range(len(_system)):
        coefficient//=_system[i]
        progression.append(number//coefficient)
        number=number%coefficient
    return progression

def statistics(list):
    list=list
    list.sort()
    index_first_quartile=len(list)//4
    indexmedian=len(list)//2
    index_third_quartile=(3*len(list))//4
    statistics={}
    average=0
    v_first_quartile=0
    median=0
    v_third_quartile=0
    for i in range(len(list)):
        average+=list[i]
        if i==index_first_quartile:
            v_first_quartile=list[i]
        if i==indexmedian:
            median=list[i]
        if i==index_third_quartile:
            v_third_quartile=list[i]
    average=average/len(list)
    reducted=reduct(list)
    maximum=0
    majority=0
    for i in reducted:
        if list.count(i)>maximum:
            maximum=list.count(i)
            majority=i
    statistics["average"]=average
    statistics["median"]=median
    statistics["majority"]=majority
    statistics["first quartile"]=v_first_quartile
    statistics["third quartile"]=v_third_quartile
    statistics["Ecart-Type"]=v_third_quartile-v_first_quartile
    statistics["minimum"]=list[0]
    statistics["maximum"]=list[-1]
    statistics["etendu"]=list[-1]-list[0]

    return statistics

def data_type_printer(data,index=1):
    t=type(data)
    try:
        a=t[0]
    except:
        return None

    print(t)
    for ti in t:
        return data_type_printer(ti)
