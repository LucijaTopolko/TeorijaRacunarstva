import sys

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
abc = prijelazi
prijelazi = prijelazi1
del prijelazi1

# nedohvatljiva

dohvatljiva = set()
dohvatljiva.add(pocetno)
zastavica = True
while (zastavica):
    zastavica = False
    testna = []
    for stanje in dohvatljiva:
        dict = prijelazi.get(stanje)
        if dict:
            for key in dict.keys():
                for p in prijelazi.get(stanje).get(key):
                    if p not in dohvatljiva:
                        testna.extend(prijelazi.get(stanje).get(key))
                        zastavica = True
    dohvatljiva.update(testna)

dohvatljiva = sorted(dohvatljiva)

for stanje in stanja:
    if stanje not in dohvatljiva:
        del prijelazi[stanje]
        if stanje in prihvatljiva:
            prihvatljiva.remove(stanje)

# istovjetna
istovjetna = []
neprihvatljiva = []
if prihvatljiva != ['']:
    istovjetna.append(prihvatljiva)
    for i in dohvatljiva:
        if i not in prihvatljiva:
            neprihvatljiva.append(i)
    istovjetna.append(neprihvatljiva)
else:
    istovjetna.append(dohvatljiva)
zastavica = True
while (zastavica):
    temp = []
    zastavica = False
    for grupa in range(len(istovjetna)):
        if isinstance(grupa, str):
            temp.extend(istovjetna[grupa][0])
        else:
            grupa1 = []
            grupa2 = []
            grupa1.extend(istovjetna[grupa])
            for s1 in range(len(istovjetna[grupa])):
                for s2 in range(s1+1, len(istovjetna[grupa])):
                    for znak in abeceda:
                        z1 = prijelazi.get(istovjetna[grupa][s1])
                        if z1:
                            z1 = z1.get(znak)[0]
                        z2 = prijelazi.get(istovjetna[grupa][s2])
                        if z2:
                            z2 = z2.get(znak)[0]
                        for g in istovjetna:
                            if (not z1 and not z2):
                                continue
                            if (z1 in g and z2 not in g) or (z1 not in g and z2 in g):
                                zastavica = True
                                if (istovjetna[grupa][s2] in grupa1):
                                    grupa1.remove(istovjetna[grupa][s2])
                                    grupa2.append(istovjetna[grupa][s2])
                                    break
                                    print("!" + grupa1, grupa2)

            temp.append([el for el in grupa1])
            if (len(grupa2) > 0):
                temp.append([el for el in grupa2])

    istovjetna = temp
    temp = []

print(istovjetna)
konacna = []
# 1,3,5,7
for a in range(len(istovjetna)):
    if len(istovjetna[a]) > 1:
        istovjetna[a].sort()
        konacna.append(istovjetna[a][0])
        for t in range(1, len(istovjetna[a])):
            if istovjetna[a][t] in prihvatljiva:
                prihvatljiva.remove(istovjetna[a][t])
    elif len(istovjetna[a]) > 0:
        konacna.append(istovjetna[a][0])
prijelazi1 = prijelazi.copy()
for key in prijelazi1:
    if key not in konacna:
        del prijelazi[key]
    else:
        for key1 in prijelazi1.get(key):
            if prijelazi[key][key1][0] not in konacna:
                for g in istovjetna:
                    if prijelazi[key][key1][0] in g:
                        prijelazi[key][key1][0] = g[0]

konacna = sorted(konacna)
print(",".join(konacna))
print(",".join(abeceda))
print(",".join(prihvatljiva))
if pocetno not in konacna:
    for g in istovjetna:
        if pocetno in g:
            pocetno = g[0]
print(pocetno)
for kljuc1, pp in prijelazi.items():
    for kljuc2, vrijednost in pp.items():
        print(kljuc1 + "," + kljuc2 + "->" + ",".join(vrijednost))
