import csv
import copy
import pandas as pd

f = open('branches-analysis.csv', 'r')
reader = csv.DictReader(f)
lista = list(reader)

selection = []
i = 0

for i in range(0,len(lista)):
    for key, value in lista[i].items():

        if key == "nTau":
            if value == "2":
                selection.append(lista[i])


while i < len(selection) - 1:
  for key, value in selection[i].items():
    if key == "Tau_pt":
            new = eval(value)
            for k in new:
                if k < 20:
                  del selection[i]
                  continue

    if key == "Tau_eta":
            new = eval(value)
            for k in new:
                if abs(k) > 2.4:
                  del selection[i]
                  continue
             
    if key == "Tau_dz":
            new = eval(value)
            for k in new:
                if abs(k) > 0.2:
                  del selection[i]
                  continue

    if key == "Tau_idDeepTau2017v2p1VSe":
            new = eval(value)
            for k in new:
                if k < 8:
                  del selection[i]
                  continue

    if key == "Tau_idDeepTau2017v2p1VSmu":
            new = eval(value)
            for k in new:
                if k < 1:  # if k << 1:
                    del selection[i]
                    continue

    if key == "Tau_idDeepTau2017v2p1VSjet":
            new = eval(value)
            for k in new:
                if k < 8:  # if k << 8:
                    del selection[i]
                    continue

    if key == "nJet":
            if int(value) < 1:
                del selection[i]
                continue

    if key == "Jet_pt":
            new = eval(value)
            for k in new:
                if k < 20:
                  del selection[i]
                  continue

    if key == "Jet_eta":
            new = eval(value)
            for k in new:
                if abs(k) > 2.4:
                    del selection[i]
                    continue

    if key == "Jet_area":
        new = eval(value)
        for k in new:
            if k < 0.4:
                del selection[i]
                continue

    if key == "Jet_puId":
        new = eval(value)
        for k in new:
            if k != 7:
                del selection[i]
                continue

    if key == "Jet_jetId":
        new = eval(value)
        for k in new:
            if k != 3:
                del selection[i]
                continue

df = pd.DataFrame(selection)
df.to_csv('higgs-analysis.csv', index=False, header=True)
