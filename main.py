# x = int(input("entrez une valeur entière:")) contraint int
# print(x)
# c1 = "L'information de la chaîne"
# c2 = 'avec des "apostrophes" !!'
# print(c1, c2)
#
# p1 = 'une chaine \nen deux lignes'
# print(len(p1))

# r1 = r'une chaine \nen mode raw'
# print(r1)
#
# c4 = "help!"
# c5 = c4 * 4
# print(c5)
#
# c6 = "une ligne à découper"
# print(c6.split(' '))

# print('-'.join(['c\'est', 'à', 'dire']))

# print('this is a title'.title())

# print('fRANK'.swapcase())

# print("    Trop d'espaces    ".strip(' '))

# print('abracadabra'.replace('a', 'i'))

# c1 = 'abcdefghijklmnop'
# print(c1[5])
# print(c1[-1])
# print(c1[1:5])
# print(c1[1:])
# print(c1[:5])
#
# x = 25
# print("%d en base 8: %o" % (x,x))
# print("%d en base 8: %x" % (x,x))

#
# couleurs = ['rouge', 'vert', 'bleu', 'jaune']
# print(couleurs)
# print(couleurs[2])
# couleurs[1] = 7
# print(couleurs)
#
# list1 = [1, 2, 3, 5.0]
# list2 = ['a', 'b', 'c']
# list3 = [list1, list2]
# print(list3)

# numbers = [5, 1, 9,30,18,55,24]
# numbers.sort()
# print(numbers)
# numbers.append(10)
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(numbers.index(30))
# numbers.remove(30)
# print(numbers)
# print(numbers[1:3])
# print(numbers[:3])
# print(numbers[:])
# print(numbers[-1])

# chose = [2] * 5
# print(chose)
# chose = [*range(2, 11, 2)]  # crée la liste [2, 4, 6,]
# print(chose)

# bois = ['chêne', 'acacia', 'peuplier']
# bois[2:2] = ['platane']
# print(bois)
# bois[4:4] = ['bouleau']
# print(bois)
# bois[2:4] = []
# print(bois)
# bois[1:3] = ['sapin']
# print(bois)
# bois[3:] = ['châtaigné', 'pommier', 'poirier']
# print(bois)
# print(len(bois))

# aTuple = ('chêne', 15, ["plaine", 1200])
# print(aTuple)

# dico = {'1': 'snake', '3': 'cats', '2': 'fish', '4': 'hamsters'}
# print(dico)
# print(dico.keys())
# print(dico.values())
# print(len(dico))
#
# for key in dico.keys():
#     print(key)
#
# for val in dico.values():
#     print(val)
#
# for keyVal in dico.items():
#     print(keyVal)

# x = set('abcd')
# y = set('bdx')
#
# print('c' in x)  # True
# print(x - y)  # {'a', 'c'}
# print(x | y)  # {'b', 'c', 'a', 'x', 'd'}
# print(x & y)  # {'b', 'd'}

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(b)  # [1, 2, 3, 4]
#
# import copy
# a = [1, 2, 3]
# b = a
# b.append(4)
# # print(a)
# c = copy.copy(a)
# c.append(5)
# print(a) # [1, 2, 3, 4]
# print(b) # [1, 2, 3, 4]
# print(c) # [1, 2, 3, 4, 5]

