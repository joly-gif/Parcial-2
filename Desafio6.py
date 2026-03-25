# Pega o total de segundos como número inteiro
total = int(input("Segundos: "))
# Acha as horas dividindo o total por 3600 (parte inteira)
h = total // 3600
# Acha os minutos dividindo o resto que sobrou por 60
m = (total % 3600) // 60
# O que sobrar dessa brincadeira toda são os segundos finais
s = total % 60
# Imprime tudo junto num texto só
print(f"{h}h {m}m {s}s")