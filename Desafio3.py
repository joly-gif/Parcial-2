# Cria uma lista vazia pra guardar os nomes
nomes = []
# Faz um loop que roda exatamente 5 vezes
for i in range(5):
# Pede o nome e já joga direto pro final da lista
    nomes.append(input(f"Nome {i+1}: "))
# Mostra a lista pronta com todos os nomes na tela
print("Nomes digitados:", nomes)