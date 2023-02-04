m = []

prt = []

n = int(input("Digite o primeiro número da lista: "))

while n != 0:
   
    m.append(n)

    n = int(input("Digite o próximo número da lista: "))


tam = len(m) - 1

while tam >=0:

    prt.append(m[tam])

    #print(m[tam])

    tam = tam - 1

print(prt)



#rev = list(reversed(m))

#print(rev)
    

#ou
    

#m.reverse()

#print(m)

