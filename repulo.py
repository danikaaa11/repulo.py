import random

lista = []

#A
for i in range (20):
    lista.append(random.randint(0, 9)) 

print("A mérési eredmények: ", ' '.join(map(str, lista))) #Zárójel nélkül irja ki

#B
print("Ez a legnagyobb helység: ",max(lista))


#C
lista = sorted(lista) #Sorrendbe rakja a lista tagokat
while lista[0] == 0:
    lista.remove(lista[0])

kivonas = max(lista) - min(lista)
print("Ennyi a külömbség: ",kivonas)

#D
viz = 0
for i in lista:
    if i == 0:
        viz += 1

szárazfold = 20 - viz

if szárazfold > 10:
    print("Több a szárazföld")
elif viz > 10:
    print("Több a viz")
else:
    print("Mindegyikből ugyanannyi van")
