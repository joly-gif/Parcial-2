# Solicita um número inteiro ao usuário e armazena na variável 'numero'
numero = int(input("Digite um número inteiro: "))
# Utiliza o operador módulo (%) para verificar se o resto da divisão do número por 2 é igual a zero
if numero % 2 == 0:
# Caso a condição acima seja verdadeira (resto zero), imprime que o número é par
    print("O número é par.")
# Caso a condição do 'if' seja falsa (resto diferente de zero), entra no bloco 'else'
else:
# Imprime na tela que o número é ímpar
    print("O número é ímpar.")