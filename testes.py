# ===================================================== 
# TechStock - Controle de estoque TechPoint
# Aluna: Gabriela da Silva Souza
# =====================================================

print("=====================================================")
print("   TECHSTOCK - TECHPOINT")
print("=====================================================")

contador = 1
while contador <= 3:
    print("Volta", contador)
    contador = contador + 1
print("Fim!")

contador = 0
soma = 0
numero = int(input("Digite um número (0 para sair): "))
while numero != 0:
    contador = contador + 1
    soma = soma + numero   
    numero = int(input("Digite um número (0 para sair): "))
    print("Você digitou", contador, "números")
    print("A soma dos números digitados é:", soma)


for i in range(1, 4):
    print("Volta", i)  
print("Fim!")


for numero in range(1, 8):
    if numero ==3:
        continue
    if numero == 6:
        break  
    print(numero)
print("Fim!")   


for linha in range(1, 3):
    for coluna in range(1, 4):
        print("Linha", linha, "Coluna", coluna)


produto =  {
    "codigo": 101
    "nome" : "Teclado"
    ""
}
        