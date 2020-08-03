import random
import requests
import bs4

def pret_imper(verbo):
    if verbo[-2:] == 'ar':
        sufixos = ["ava", "avas", "ava", "ávamos", "áveis", "avam"]
    elif verbo[-2:] == 'er':
        sufixos = ["ia", "ias", "ia", "íamos", "íeis", "iam"]
    elif verbo[-2:] == 'ir':
        sufixos = ["ia", "ias", "ia", "íamos", "íeis", "iam"]

    return sufixos

def pret_maisque(verbo):
    if verbo[-2:] == 'ar':
        sufixos = ["ara", "aras", "ara", "áramos", "áreis", "aram"]
    elif verbo[-2:] == 'er':
        sufixos = ["era", "eras", "era", "êramos", "êreis", "eram"]
    elif verbo[-2:] == 'ir':
        sufixos = ["ira", "iras", "ira", "íramos", "íreis", "iram"]

    return sufixos

def futuro_pres(verbo):
    if verbo[-2:] == 'ar':
        sufixos = ["arei", "arás", "ará", "aremos", "areis", "arão"]
    elif verbo[-2:] == 'er':
        sufixos = ["erei", "erás", "erá", "eremos", "ereis", "erão"]
    elif verbo[-2:] == 'ir':
        sufixos = ["irei", "irás", "irá", "iremos", "ireis", "irão"]

    return sufixos

def futuro_pret(verbo):
    if verbo[-2:] == 'ar':
        sufixos = ["aria", "arias", "aria", "aríamos", "aríeis", "ariam"]
    elif verbo[-2:] == 'er':
        sufixos = ["eria", "erias", "eria", "eríamos", "eríeis", "eriam"]
    elif verbo[-2:] == 'ir':
        sufixos = ["iria", "irias", "iria", "iríamos", "iríeis", "iriam"]

    return sufixos


def art_sub(plural):
    
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v" ]
    letra = letras[random.randint(0,19)]
    num = random.randint(0,29)
    url_sub = 'https://dicionario.aizeta.com/verbetes/substantivo/'+ letra +"/" + str(random.randint(0,3))
    request_sub = requests.get(url_sub, headers={"User-Agent": "XY"})
    soup_sub = bs4.BeautifulSoup(request_sub.text, 'lxml')
    mascs = soup_sub.find_all('a')
    subs = soup_sub.find_all('b')
    sub = subs[num].get_text()
    masc = mascs[num + 42].get_text()
    masculino = masc[-2] == 'm'
    
    '''artigos'''
    ams = ["o", "um"]
    amp = ["os", "uns" ]
    afp = ["as", "umas"]
    afs = ["a", "uma"]

    if(plural):
        if(masculino):
            artigo = amp[random.randint(0,1)]
        else :
            artigo = afp[random.randint(0,1)]

    else :
        if(masculino):
            artigo = ams[random.randint(0,1)]
        else :
            artigo = afs[random.randint(0,1)]

    if (plural):
        return(artigo + " " + sub + "s")
    else:
        return(artigo + " " + sub)
    
def frase(): 
    plural = random.randint(0,1) == 0                                            
    letras = ["a", "b", "c", "d", "e", "f", "g", "i", "l", "m", "n", "o", "p", "r", "s", "t", "v" ]
    letra = letras[random.randint(0,16)]
    num = random.randint(0,29)
    url_vrb = 'https://dicionario.aizeta.com/verbetes/verbo/' + letra + '/' +str(random.randint(0,2))
    request_vrb = requests.get(url_vrb, headers={"User-Agent": "XY"})
    soup_vrb = bs4.BeautifulSoup(request_vrb.text, 'lxml')
    transitividades = soup_vrb.find_all('a')
    vrbs = soup_vrb.find_all('b')
    vrb = vrbs[num].get_text()
    transitividade_merda = transitividades[num + 42].get_text()
    transitividade = transitividade_merda[ len(transitividade_merda) - 5:  len(transitividade_merda):1]
    
    x = random.randint(0,3)

    if(x == 0):
        sufixo = pret_imper(vrb)
    elif(x == 1):
        sufixo = pret_maisque(vrb)
    elif(x == 2):
        sufixo = futuro_pres(vrb)
    else:
        sufixo = futuro_pret(vrb)

    if(plural):
        vrb = vrb[0: len(vrb) - 2: 1] + sufixo[5]
    else:
        vrb =  vrb[0: len(vrb) - 2: 1] + sufixo[2]
    
    if(transitividade == '.t.d.'):
        return((art_sub(plural) + " " + vrb + " " + art_sub(random.randint(0,1) == 0)).lower())
    elif(transitividade == 'intr.'):
        return((art_sub(plural) + " " + vrb).lower())
    else:
        frase()

    
        

    


    


