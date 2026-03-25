# Lê o primeiro número
n1 = float(input("Digite o primeiro número para a operação: "))
# Lê o sinal da operação matemática
op = input("Defina a operação (+, -, *, /): ")
# Lê o segundo número
n2 = float(input("Digite o segundo número para a operação: "))
# Se for +, soma e já imprime com a frase
if op == '+': print("O resultado é:", n1 + n2)
# Se for -, subtrai e já imprime com a frase
elif op == '-': print("O resultado é:", n1 - n2)
# Se for *, multiplica e já imprime com a frase
elif op == '*': print("O resultado é:", n1 * n2)
# Se for /, divide e já imprime com a frase
elif op == '/': print("O resultado é:", n1 / n2)