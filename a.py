import csv
import copy
import pandas as pd

f = open('branches-analysis.csv', 'r')
reader = csv.DictReader(f)
lista = list(reader)

print(len(lista))