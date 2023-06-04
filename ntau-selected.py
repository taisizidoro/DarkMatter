import pandas as pd
import matplotlib.pyplot as plt
import csv

f = open('trash but save/skim2.csv', 'r')
reader = csv.DictReader(f)
lista = list(reader)

df = pd.DataFrame(lista)
plt.plot(df['nTau'])
plt.show()