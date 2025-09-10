# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 14:35:31 2025

@author: My PC
"""

a = input(" Nhap vao so a: ")
print(" Kieu du lieu cua a  :", type(a))
a = float(a)
print(" Kieu du lieu cua a  :", type(a))

b = input(" Nhap vao so b: ")
print(" Kieu du lieu cua a  :", type(a))
b= float(b)
print(" Kieu du lieu cua b  :", type(b))

print("{0}+{1}={2}".format(a , b , a+b))
print("{0}-{1}={2}".format(a , b , a-b))
print("{0}*{1}={2}".format(a , b , a*b))
print("{0}/{1}={2}".format(a , b , a/b))
print("{0}%{1}={2}".format(a , b , a%b))
print("{0}**{1}={2}".format(a , b , a**b))
print("{0}//{1}={2}".format(a , b , a//b))
