import time
start = time.time()
liste_1 = [i**2 for i in range(10000000)] # Liste comprehension
end = time.time()
print(end-start)


liste_3 = [[ i+j for i in range(3)] for j in range(2)]
print(liste_3)

# Dict Comprehension
dictionnaire = {
    '0' : 'Pierre',
    '1' : 'Jean',
    '2' : 'Julie',
    '3' : 'Sophie'
}

prenoms = ['Pierre', 'Jean', 'Julie', 'Sophie']

dico = {k:v for k,v in enumerate(prenoms)}
print(dico)
print(dico.keys())
print(dico.values())

ages = [24, 62, 10, 23]
dico_2 = {prenoms:ages for prenoms,ages in zip(prenoms,ages) if ages > 30 }
print(dico_2)

# Tuples comprehension
tuple_1 = tuple(i**2 for i in range(10))
print(tuple_1)

dico_nombre = {i:i**2 for i in range(20)}
print(dico_nombre)