# Pega o dinheiro inicial
c = float(input("Capital: "))
# Pega a taxa de juros
i = float(input("Taxa (%): "))
# Pega o tempo
t = float(input("Tempo: "))
# Calcula os juros simples e já imprime o valor na hora
print("Juros: R$", c * (i / 100) * t)