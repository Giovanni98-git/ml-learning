villes = ['Paris', 'Berlin', 'Londres', 'Bruxelles']

# INDEXING
print(villes[-1]) # dernier element

# SLICING
# villes [debut:fin:pas]
print(villes[0:3]) #  Cela considère le pas 1 et prend les trois premiers elements

print(villes[::-1]) # du dernier au premier dans l'ordre décroissant

villes.append('Dublin') # ajoute a la fin
print(villes) 

villes.insert(2, 'Madrid') # ajoute à l'index 2

villes_2 = ['Amsterdam', 'Rome']
villes.extend(villes_2) # ajoute les elements de villes_2 a la fin de ceux de villes
print(villes)
print(len(villes)) # taille de villes

print(villes.count('Paris')) # conmpte le nombre de fois il y a Paris dans villes

if 'Paris' in villes:
    print('Oui')
else:
    print('Non')

for i in villes:
    print(i)

for (index, valeur) in enumerate(villes):
    print(index, valeur)

liste = [2,3,23,24,51,52,61,78]

for a,b in zip(villes, liste): # s'arrête là ou la liste la plus courte s'arrête
    print(a,b)


def fibonacci(n):
    liste = []
    a = 0
    b = 1
    while a < n:
        liste.append(a)
        a, b = b, a+b
    return liste


print(fibonacci(1000))