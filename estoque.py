# ===================================================== 
# TechStock - Controle de estoque TechPoint
# Aluna: Gabriela da Silva Souza
# =====================================================

print("=====================================================")
print("   TECHSTOCK - TECHPOINT")
print("=====================================================")

produtos = [
    {'nome': "Mouse", 'quantidade': 10, 'preco': 25.00},
    {'nome': "Teclado", 'quantidade': 5, 'preco': 80.00},
    {'nome': "Monitor", 'quantidade': 3, 'preco': 500.00},
    {'nome': "Webcam", 'quantidade': 2 }
]
def listar():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    print("\n=====Produtos cadastrados=====")
    for indice in range(len(produtos)):
        produto = produtos[indice]
        print(f'{indice + 1}. {produto["nome"]} - Quantidade: {produto["quantidade"]} - Preço: R$ {produto["preco"]:.2f}')
    print(f"Tipos de produtos: {len(produtos)}")
    
def consultar_numero():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    listar()
    texto = input("Digite o número do produto: ")
    if not texto.isdigit():
        print("Erro: Digite um número inteiro válido.")
        return
    numero = int(texto)
    if numero < 1 or numero > len(produtos):
        print("Produto fora da lista.")
        return
    produto = produtos[numero - 1]
    print(f'Produto: {produto["nome"]}')
    print(f'Quantidade: {produto["quantidade"]}')
    print(f'Preço: R$ {produto["preco"]:.2f}')
    

while True:
    codigo = input("Código do produto: ")
    if codigo != "":
        break
    print("O código não pode ser vazio.")

while True:
    nome = input("Nome do produto: ")
    if nome != "":
        break
    print("Nome inválido! Não pode ser vazio.")

while True:
    preco = float(input("Preço unitário: "))
    if preco > 0:
        break
    print("Erro: O preço deve ser maior que zero.")

while True:
    quantidade = int(input("Quantidade inicial em estoque: "))
    if quantidade >= 0:
        break
    print("Erro: A quantidade não pode ser negativa.")

while True:
    estoque_minimo = int(input("Estoque mínimo desejado: "))
    if estoque_minimo >= 0:
        break
    print("Erro: O estoque mínimo não pode ser negativo.")

# Etapa 4: Variáveis de Contadores e Acumuladores
qtd_entradas = 0
qtd_vendas = 0
unidades_vendidas = 0
fat_total = 0.0

# Etapa 2: Menu Principal
opcao = ""
while opcao != "0":
    print()
    print("============== MENU ==============")
    print("[1] - Registrar entrada")
    print("[2] - Registrar saída")
    print("[3] - Vendas em sequência")
    print("[4] - Ficha do produto")
    print("[5] - Gráfico do estoque")
    print("[6] - Inventário por prateleira")
    print("[7] - Relatório do dia")
    print("[10] - ")
    print("[0] - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Etapa 3: Validação da entrada
        while True:
            entrada = int(input("Quantas unidades chegaram? "))
            if entrada > 0:
                quantidade = quantidade + entrada
                qtd_entradas = qtd_entradas + 1
                print("Entrada registrada. Estoque atual:", quantidade)
                break
            print("Erro: digite um valor maior que zero.")

    elif opcao == "2":
        # Etapa 3: Validação da saída
        if quantidade <= 0:
            print("Produto SEM ESTOQUE. Não é possível vender.")
        else:
            while True:
                saida = int(input("Quantas unidades foram vendidas? "))
                if saida > 0:
                    if saida <= quantidade:
                        quantidade -= saida
                        unidades_vendidas += saida
                        fat_total += saida * preco
                        qtd_vendas = qtd_vendas + 1
                        print("Venda registrada. Estoque atual:", quantidade)
                        break
                    else:
                        print("Erro: Quantidade insuficiente. Disponível:", quantidade)
                else:
                    print("Erro: digite um valor maior que zero.")

    elif opcao == "3":
        # Etapa 6: Venda em sequência
        print("--- Vendas em sequência ---")
        total = int(input("Quantas vendas você quer registrar? "))
        for i in range(1, total + 1):
            if quantidade == 0:
                print("O estoque acabou! Encerrando as vendas.")
                break
            print("Venda", i)
            saida = int(input("Unidades vendidas: "))
            if saida <= 0 or saida > quantidade:
                print("Venda ignorada. Digite um valor válido.")
            else:
                quantidade = quantidade - saida
                unidades_vendidas = unidades_vendidas + saida
                fat_total = fat_total + (saida * preco)
                print("Venda", i, "registrada. Estoque atual:", quantidade)

    elif opcao == "4":
        # Ficha do produto
        print()
        print("----------Ficha do Produto----------")
        print("Código:", codigo)
        print("Produto:", nome)
        print("Preço: R$", preco)
        print("Quantidade:", quantidade)
        print("Estoque Mínimo:", estoque_minimo)
        valor_total = round(preco * quantidade, 2)
        print("Valor total em estoque: R$", valor_total)

        if quantidade == 0:
            print("Situação: SEM ESTOQUE - repor urgente!")
        elif quantidade < estoque_minimo:
            faltam = estoque_minimo - quantidade
            print("Situação: ESTOQUE BAIXO - repor pelo menos", faltam, "unidades")
        else:
            print("Situação: ESTOQUE OK")

    elif opcao == "5":
        # Etapa 5: Gráfico do estoque
        print("--- Gráfico de Estoque ---")
        barra = "#" * quantidade
        for i in range(quantidade):
            barra = barra + "#" 
        marca = "#" * estoque_minimo
        print("Estoque:", barra, quantidade)
        print("Mínimo:", marca, estoque_minimo)

    elif opcao == "6":
        # Etapa 7: Inventário por prateleira
        print("--- Inventário por prateleira ---")
        prateleiras = int(input("Quantas prateleiras guardam o produto? "))
        caixas = int(input("Quantas caixas tem cada prateleira? "))
        total_contado = 0
        for p in range(1, prateleiras + 1):
            soma_prateleira = 0
            for c in range(1, caixas + 1):
                print("Prateleira", p, "- caixa", c)
                unidades = int(input("Unidades na caixa: "))
                soma_prateleira = unidades
            print("Total da prateleira", p, "=", soma_prateleira)
            total_contado = total_contado + soma_prateleira

        print("Total contado:", total_contado, "| No sistema:", quantidade)
        if total_contado == quantidade:
            print("Contagem confere com o sistema!")
        else:
            diferenca = total_contado - quantidade
            print("Diferença de", diferenca, "unidade(s). Estoque ajustado.")
            quantidade = total_contado

    elif opcao == "7":
        # Etapa 4: Relatório do dia
        print()
        print("--- Relatório do Dia ---")
        print("Entradas registradas:", qtd_entradas)
        print("Vendas registradas:", qtd_vendas)
        print("Unidades vendidas:", unidades_vendidas)
        print("Faturamento: R$", round(fat_total, 2))
        if qtd_vendas > 0:
            media = unidades_vendidas / qtd_vendas
            print("Média por venda: R$", round(media, 1), "unidades")
            print("----------------------------------")


    elif opcao == "0":
        print("Encerrando o TechStock... Até logo!")
    else:
        print("Opção inválida. Tente novamente.")


