import os
import uproot as up

parsed_events = []
for file in os.listdir(r"C:\\Users\\Taís Izidoro\\Documents\\PrivateSignal16\\PrivateSignal16\\MH1000_Ma100_MChi45"):
    try:
        dataset = up.open(os.path.join(r"C:\\Users\\Taís Izidoro\\Documents\\PrivateSignal16\\PrivateSignal16\\MH1000_Ma100_MChi45", file))
        tree = dataset.get("Events;1")

        for event in tree:
            parsed_events.append(event)

    except:
        break

for file in os.listdir(r"C:\\Users\\Taís Izidoro\\Documents\\PrivateSignal16\\PrivateSignal16\\MH400_Ma100_MChi45"):
    try:
        dataset2 = up.open(os.path.join(r"C:\\Users\\Taís Izidoro\\Documents\\PrivateSignal16\\PrivateSignal16\\MH400_Ma100_MChi45", file))
        tree2 = dataset2.get("Events;1")

        for event in tree2:
            parsed_events.append(event)

    except:
        break

lista = parsed_events
print(lista)
