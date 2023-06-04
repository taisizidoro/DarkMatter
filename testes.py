if key == "Jet_pt":
    new = list(value)
    select[i][key] = []
    for k in new:
        if k > 20.0:
            continue
        select.append(lista[i])

if key == "Jet_eta":
    new = list(value)
    select[i][key] = []
    for k in new:
        if k < 2.4:
            continue
        select.append(lista[i])

if key == "Jet_area":
    new = list(value)
    select[i][key] = []
    for k in new:
        if eval(k) > 0.4:
            continue
        select.append(lista[i])

if key == "Jet_puId":
    new = list(value)
    select[i][key] = []
    for k in new:
        if k == 7:
            continue
        select[i][key].append(k)

if key == "Jet_jetId":
    new = list(value)
    select[i][key] = []
    for k in new:
        if k == 3:
            continue
        select[i][key].append(k)
