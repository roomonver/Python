# -*- coding: utf-8 -*-

A = [1,3,5,7,9]
B = [1,2,3,4,5]

'''
union
'''
newSet = set(A) | set(B)
print(newSet)

'''
interseccion
'''
newInter = set(A) & set(B)
print(newInter)

'''
diferencias
'''
newDif = set(A) - set(B)
print(newDif)