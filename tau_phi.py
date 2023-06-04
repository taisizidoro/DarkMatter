import os
import uproot as up
import pandas as pd
import matplotlib.pyplot as plt
import awkward as ak

parsed_events = []
for file in os.listdir(r"C:\\Users\\Taís Izidoro\\Documents\\PrivateSignal16\\PrivateSignal16\\MH1000_Ma100_MChi45"):
    try:
        dataset = up.open(os.path.join(r"C:\\Users\\Taís Izidoro\\Documents\\PrivateSignal16\\PrivateSignal16\\MH1000_Ma100_MChi45", file))
        tree = dataset.get("Events;1")
        objects = ["Tau_phi"]
        events = tree.arrays(objects)

        for event in events:
            event = {k: getattr(event, k) for k in objects}
            parsed_events.append(event)

    except:
        break

for file in os.listdir(r"C:\\Users\\Taís Izidoro\\Documents\\PrivateSignal16\\PrivateSignal16\\MH400_Ma100_MChi45"):
    try:
        dataset2 = up.open(os.path.join(r"C:\\Users\\Taís Izidoro\\Documents\\PrivateSignal16\\PrivateSignal16\\MH400_Ma100_MChi45", file))
        tree2 = dataset2.get("Events;1")
        objects = ["Tau_phi"]
        events2 = tree2.arrays(objects)

        for event in events2:
            event = {k: getattr(event, k) for k in objects}
            parsed_events.append(event)

    except:
        break


dts = df = pd.DataFrame(ak.flatten(parsed_events, axis=None))
df[0].hist(bins=15)
plt.xlabel('Tau_phi')
plt.ylabel('Frequência')
plt.title('Histograma para Tau_phi')
plt.show()
