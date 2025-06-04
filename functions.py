# # x = -3
# # print(abs(x))

# # liste = [True, True, False]
# # print(all(liste))
# # print(any(liste))

# # # conversions
# # x = 10
# # print(type(x))
# # y = "20"
# # print(int(y))
# # print(type(float(x)))

# # liste_1 = [0, 61,63,243]
# # tuple_1 = tuple(liste_1)
# # print(tuple_1)
# # s = int(input('Entrez un nombre: '))
# # print(s+10)

# # # la fonction format
# # x = 25
# # ville = 'Paris'
# # message = "la temperature est de {} ¤C à {}".format(x, ville)
# # print(message)

# # Open
# f = open('file.txt', 'w')
# f.write('Bonjour tout le monde')
# f.close()

# # Read
# r = open('file.txt', 'r')
# print(r.read())
# r.close()

# # 
# with open('file.txt', 'w') as f:
#     for i in range(10):
#         f.write('{}^2 = {} \n'.format(i, i**2))

liste = []
with open('file.txt', 'r') as f:
    # liste = [line.rstrip('\n') for line in f]
    liste = f.readlines()
print(liste)
