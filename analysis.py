import csv
import copy
import pandas as pd

f = open('branches-analysis.csv', 'r')
reader = csv.DictReader(f)
lista = list(reader)

select = copy.deepcopy(lista)

for i in range(0, len(lista)):
    for key, value in lista[i].items():

        if key == "nTau":
            if value == "2":
                select.append(lista[i])

        if key == "Tau_pt":
            new = eval(value)
            select[i][key] = []
            for k in new:
                if k < 20:
                    continue
                select[i][key].append(k)

        if key == "Tau_eta":
            new = eval(value)
            select[i][key] = []
            for k in new:
                if abs(k) > 2.4:
                    continue
                select[i][key].append(k)

        if key == "Tau_dz":
            new = eval(value)
            select[i][key] = []
            for k in new:
                if abs(k) > 0.2:
                    continue
                select[i][key].append(k)

        if key == "Tau_idDeepTau2017v2p1VSe":
            new = eval(value)
            select[i][key] = []
            for k in new:
                if k < 8:  # if k << 8:
                    continue
                select[i][key].append(k)

        if key == "Tau_idDeepTau2017v2p1VSmu":
            new = eval(value)
            select[i][key] = []
            for k in new:
                if k < 1:  # if k << 1:
                    continue
                select[i][key].append(k)

        if key == "Tau_idDeepTau2017v2p1VSjet":
            new = eval(value)
            select[i][key] = []
            for k in new:
                if k < 8:  # if k << 8:
                    continue
                select[i][key].append(k)


        if key == "nJet":
            select[i][key] = []
            if int(value) >= 1:
                select[i][key].append(lista[i])

        if key == "Jet_pt":
            new = eval(value)
            select[i][key] = []
            for k in new:
                if int(k) < 20:
                    continue
                select[i][key].append(k)


df = pd.DataFrame(select)
df.to_csv('analysis.csv', index=False, header=True)

