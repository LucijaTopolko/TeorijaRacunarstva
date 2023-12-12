import sys


def epsilon(nova):
    kontrolna = set()
    kontrolna.update(nova)
    zastavica = True
    nova = set(nova)
    testna = set()
    while (zastavica):
        zastavica = False
        temp = []
        for stanje in kontrolna:
            dict = prijelazi.get(stanje)
            if dict:
                a = dict.get("$")
                if (a):
                    nova.update(a)
                    temp.extend(a)
                    zastavica = True
        testna.update(kontrolna)
        kontrolna = set(temp) - set(testna)
    return list(nova)


ulazi = input().split("|")  # ulazni nizovi
ulazi[-1] = ulazi[-1].split("\n")[0]
for i in range(len(ulazi)):
    ulazi[i] = ulazi[i].split(",")
stanja = input().split(",")
abeceda = input().split(",")
prihvatljiva = input().split(",")
pocetno = input()
prijelazi = []
for line in sys.stdin:
    prijelazi.append(line.split("\n")[0])
for i in range(len(prijelazi)):
    prijelazi[i] = prijelazi[i].split("->")
    prijelazi[i][0] = prijelazi[i][0].split(",")
    prijelazi[i][1] = prijelazi[i][1].split(",")
prijelazi1 = {}
for [kljuc, vrijednost] in prijelazi:
    kljuc1, kljuc2 = kljuc
    if kljuc1 not in prijelazi1:
        prijelazi1[kljuc1] = {}
    prijelazi1[kljuc1][kljuc2] = vrijednost
prijelazi = prijelazi1
del prijelazi1

for ulaz in range(len(ulazi)):
    prethodna = []
    nova = []
    prethodna.append(pocetno)
    prethodna = epsilon(prethodna)
    prethodna = [i for i in prethodna if i != "#"]
    print(",".join(sorted(set(prethodna))), end="")
    for simbol in ulazi[ulaz]:
        print("|", end="")
        for element in prethodna:
            dict = prijelazi.get(element)
            if dict:
                a = dict.get(simbol)
                if a:
                    nova.extend(a)
        nova = epsilon(nova)
        if (len(nova) == 0):
            nova.append("#")
        while (len(nova) > 1 and "#" in nova):
            nova = [i for i in nova if i != "#"]
        nova = set(nova)
        print(",".join(sorted(nova)), end="")
        prethodna = []
        prethodna.extend(nova)
        nova = []
    print()
