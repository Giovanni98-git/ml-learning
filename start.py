f = lambda x: x**2
print(f(3))

def e_potentielle(masse, hauteur,e_limite, g=9.81):
    E = masse * hauteur * g

    if E > e_limite:
        return e_limite
    else:
        return E


print(e_potentielle(masse=80,hauteur=5, e_limite=500))