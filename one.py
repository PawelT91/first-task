#!/usr/bin/python3
# coding: utf-8

__author__ = 'Тупиков Павел'        
__version__ = 1.0

from time import clock

def deley(integer):
    for s in sim:
        if integer%s == 0:
            i1 = s
            i2 = integer//s
    return i1,i2

def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res
    return wrappe


if __name__ == '__main__':

    R = True
    while R:
        n = input('Введите число: ')
        try:
            t = int(n)
            R = False
        except ValueError:
            print('Не корректное число')
    i = 0
    sim = list(range(2,t+1))
    while i<t:
        for x in sim[i+1:]:
            if x%sim[i] == 0:
                sim.remove(x)
        i+=1
    for num in range(2,t+1):
        if num in sim:
            print(num,'- простое число')
        else:
            num1 = num
            com = True
            c = []
            while com:
                i1,i2 = deley(num1)
                c.append(i1)
                c.append('*')
                if i2 in sim:
                    c.append(i2)
                    com = False
                else:
                    num1 = i2
            print(num,'=',*c)
                
