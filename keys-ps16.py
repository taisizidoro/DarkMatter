import uproot as up

parsed_events = []
dataset = up.open("C:\\Users\\Taís Izidoro\\Documents\\UERJ\\IC\\PrivateSignal16\\PrivateSignal16\\MH400_Ma100_MChi45\\bbH_Za_LLChiChi-RunIISummer20UL16NanoAOD_0.root")
tree = dataset.get("Events")
a = tree.keys()

arquivo = open("C:\\Users\\Taís Izidoro\\Documents\\UERJ\\IC\\Higgs-to-tautau\\keys-ps16.txt", "w")
for i in a:
    print(i, file=arquivo)