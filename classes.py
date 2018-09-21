# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:39:20 2018

@author: gydwo
"""

def gcd(a,b):
    r = a%b
    if r==0:
        return b
    else:
        return gcd(b,r)


class Rational:
    
    def __init__(self,a,b):
        
        hcf = gcd(a,b)
        self.__n = a/hcf
        self.__d = b/hcf
        
    def getNumerator(self):
        return self.__n
    
    def getDenominator(self):
        return self.__d
    
    def __mul__(self,rhs):
        
        a = self.__n * rhs.getNumerator()
        b = self.__d * rhs.getDenominator()
        return Rational(a,b)
    
    def __repr__(self):
        str = '%d' % self.__n
        str = str + '/'
        str = str + '%d' % self.__d
        return str
    
    def __neg__(self):
        a = self.__n
        b = -self.__d
        return Rational(a,b)
    