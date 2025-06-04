inventaires = {
    "bananes":5000,
    "pommes": 2094,
    "poires": 412809,
    "cerises": 2893
}

print(inventaires.values())
print(inventaires.keys())
print(len(inventaires))

inventaires["abricots"] = 4902

print(inventaires)

print(inventaires.get('cerises',1)) # retourne 1 si cerises n'est pas dans le dictionnaire

for (key, value) in inventaires.items():
    print(key, value)


classeur = {
    "positif": [],
    "negatif": []
}

def trier(classeur, nombre):
    if nombre == 0:
        print(nombre, "est nul")
        return
    elif nombre > 0:
        classeur["positif"].append(nombre)
    else:
        classeur["positif"].append(nombre)
    return classeur

nouveau = trier(classeur, 5)
print(nouveau)