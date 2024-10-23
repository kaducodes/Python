with open('202301_Transferencias.csv', newline='') as File:
  reader = csv.reader(File, delimiter=';')
  for linha in reader:
    add = [
      r"{}".format(linha[0]), # Expressão regular
      [] # Resposta
    ]
    # Adiciona cada resposta na tupla "add[1]"
    for x in linha[1].split('|'): add[1].append(x)
    # Adiciona "add" em "pairs"
    pairs.append(add)