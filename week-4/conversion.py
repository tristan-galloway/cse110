"""

file: conversion.py
author: tristan galloway
teacher: brother keers


"""
import math

# ask user for the tempurature
fahr = float(input("What is the tempurature in Fahhrenheit? "))

# convert the tempurature given by the user to celsius
cel = (fahr - 32) * 5/9

# return the tempurature given to the user
print(f"The temperature in Celsius is {cel:.1f}")