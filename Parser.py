class rjesenje:
    def __init__(self):
        self.brojac=0

    def start(self):
        print("S", end="")
        if (self.brojac < len(ulazni_niz)):
            if(ulazni_niz[self.brojac]=='a'):
                self.brojac+=1
                self.a()
                self.b()
            elif (ulazni_niz[self.brojac]=='b'):
                self.brojac+=1
                self.b()
                self.a()
            else:
                print("\nNE")
                exit()
        else:
            print("\nNE")
            exit()
    
    def a(self):
        print("A", end="") 
        if (self.brojac < len(ulazni_niz)):
            if(ulazni_niz[self.brojac]=='a'):
                self.brojac+=1

            elif (ulazni_niz[self.brojac]=='b'):
                self.brojac+=1
                self.c()
            else:
                print("\nNE")
                exit()
        else:
            print("\nNE")
            exit()

    def b(self):
        print("B", end="") 
        if (self.brojac+1<len(ulazni_niz)):
            if(ulazni_niz[self.brojac]=='c' and ulazni_niz[self.brojac+1]=='c'):
                self.brojac+=2
                self.start()
        if (self.brojac+1<len(ulazni_niz)):
            if (ulazni_niz[self.brojac]=='b' and ulazni_niz[self.brojac+1]=='c'):
                self.brojac+=2
        
    def c(self):
        print("C", end="") 
        self.a()
        self.a()

ulazni_niz = input().split("\n")[0]
rj = rjesenje()
rj.start()
if (rj.brojac==len(ulazni_niz)):
    print("\nDA")
else:
    print("\nNE")