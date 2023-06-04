import pandas as pd
import matplotlib.pyplot as plt
import csv
import awkward as ak

f = open('trash but save/skim2.csv', 'r')
reader = csv.DictReader(f)
lista = list(reader)

df = pd.DataFrame(lista)
pt = df['Tau_dz']
plt.hist(ak.flatten(pt))
plt.show()