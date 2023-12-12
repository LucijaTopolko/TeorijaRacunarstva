import sys

def epsilon(p, zn):
    p=p[:]
    stanje,stog = p[-1]
    stog = stog[0]
    zastavica=False
    dict = prijelazi.get(stanje)
    if (dict):
        a = dict.get("$") 
        if (a):
            b = a.get(stog)
            if (b):
                y = p[-1].copy()
                p.append(y)
                p[-1][0]=b[0]
                if (b[1]!='$'):
                    p[-1][1]=b[1]+p[-1][1][1:]
                elif (len(p[-1][1])==1):
                    p[-1][1]=b[1]
                else:
                    p[-1][1]=p[-1][1][1:]
                zastavica=True
    if (zastavica and zn):
        p=epsilon(p, zn)
    return p

ulazi = input().split("|") 
ulazi[-1] = ulazi[-1].split("\n")[0]
for i in range(len(ulazi)):
    ulazi[i] = ulazi[i].split(",")
stanja = input().split(",")
abeceda = input().split(",")
znakovi_stoga = input().split(",")
prihvatljiva = input().split(",")
pocetno_stanje = input()
pocetno_stog = input()
prijelazi = []
for line in sys.stdin:
    prijelazi.append(line.split("\n")[0])
prijelazi1 = {}

for prijelaz in prijelazi:
    lhs, rhs = prijelaz.split("->")
    trenutnoStanje, ulazniZnak, znakStoga = lhs.split(",")
    novoStanje, nizZnakovaStoga = rhs.split(",")
    if trenutnoStanje not in prijelazi1:
        prijelazi1[trenutnoStanje] = {}
    if ulazniZnak not in prijelazi1[trenutnoStanje]:
        prijelazi1[trenutnoStanje][ulazniZnak] = {}
    prijelazi1[trenutnoStanje][ulazniZnak][znakStoga] = (novoStanje, nizZnakovaStoga)

prijelazi = prijelazi1
del prijelazi1

for ulaz in range (len(ulazi)):
    p = [[pocetno_stanje, pocetno_stog]]
    flag=False
    for simbol in ulazi[ulaz]:
        p=epsilon(p,1)
        dict = prijelazi.get(p[-1][0])
        if (dict):
            a = dict.get(simbol) 
            if (a):
                b = a.get(p[-1][1][0])
                if (b):
                    y = p[-1].copy()
                    p.append(y)
                    p[-1][0]=b[0]
                    if (b[1]!='$'):
                        p[-1][1]=b[1]+p[-1][1][1:]
                    elif (len(p[-1][1])==1):
                        p[-1][1]=b[1]
                    else:
                        p[-1][1]=p[-1][1][1:]
                else: 
                    flag=True
                    break
            else: 
                flag=True
                break
        else: 
            flag=True
            break

    for i in p:
        print(i[0]+'#'+i[1]+'|', end="")

    while True:
        if (flag):
            print("fail|0")
            break
        elif (p[-1][0] in prihvatljiva):
            print("1")
            break
        else:
            p1=epsilon(p,0)
            if (p1==p):
                print("0")
                break
            else:
                p=p1.copy()
                print(p[-1][0]+'#'+p[-1][1]+'|', end="")