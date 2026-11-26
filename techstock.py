# ===================================================== 

# TechStock - Controle de estoque TechPoint 
# Aluna: Gabriela da Silva Souza 

# ===================================================== 


print("=====================================================") 
print("   TECHSTOCK - TECHPOINT") 
print("=====================================================") 

# cadastro de produto 
codigo = input("Código do produto: ") 
nome = input("Nome do produto: ") 
preco = float(input("Preço de venda (R$): ")) 
quantidade = int(input("Quantidade em estoque: ")) 
estoque_minimo = int(input("Estoque mínimo: ")) 

# Validação do cadastro 
if preco <= 0: 
    print("ERRO: O preço de venda deve ser maior que zero.") 
else: 

    # menu de operações 
    print() 
    print("O que deseja fazer?") 
    print("[1] - Registrar entrada (chegou mercadoria)") 
    print("[2] - Registrar saída (venda de mercadoria)") 
    print("[3] - Apenas consultar estoque") 
    opcao = input("Escolha uma opção: ") 

    if opcao == "1": 
        entrada = int(input("Quantas unidades chegaram? ")) 
        if entrada > 0: 
            quantidade = quantidade + entrada 
            print("Entrada registrada:", entrada, "unidade(s) em estoque:", quantidade) 
        else: 
            print("ERRO: a quantidade de entrada precisa ser maior que zero.") 

 
    elif opcao == "2": 
        saida = int(input("Quantas unidades foram vendidas? ")) 
        if saida <= 0: 
            print("ERRO: a quantidade de saída precisa ser maior que zero.") 
        elif saida > quantidade: 
            print("ERRO: estoque insuficiente. Disponível:", quantidade) 
        else: 
            quantidade = quantidade - saida 
            print("Saída registrada:", saida, "unidade(s) em estoque:", quantidade) 


    elif opcao == "3": 
        print("Quantidade em estoque:", quantidade) 

    else: 
        print("Opção inválida. Mostrando apenas o estoque atual.") 


    # cálculos 
    valor_total = preco * quantidade 
    valor_total = round(valor_total, 2) 


    # ficha do produto 
    print() 
    print("----------Ficha do Produto----------") 
    print("Código:", codigo) 
    print("Produto:", nome) 
    print("Preço: R$", preco) 
    print("Quantidade:", quantidade) 
    print("Estoque Mínimo:", estoque_minimo) 
    print("Valor total em estoque: R$", valor_total) 


    # verificação do estoque 
    if quantidade == 0: 
        print("Situação: SEM ESTOQUE - repor urgente!") 
    elif quantidade < estoque_minimo: 
        faltam = estoque_minimo - quantidade 
        print("Situação: ESTOQUE BAIXO - repor pelo menos", faltam, "unidade(s)") 
    elif quantidade == estoque_minimo: 
        print("Situação: ESTOQUE OK") 
    else: 
        print("Situação: ESTOQUE OK") 

print("------------------------------------") 


# ======================================================================================================================================================================
# PARE E PENSE ETAPA 04
# A MENSAGEM QUE APARECE E QUE O ESTOQUE ESTA BAIXO, MAS O ESTOQUE MINIMO E 5 E A QUANTIDADE EM ESTOQUE TAMBEM E 5, ENTÃO NAO DEVERIA APARECER A MENSAGEM DE ESTOQUE BAIXO, POIS O ESTOQUE MINIMO E IGUAL A QUANTIDADE EM ESTOQUE. NÃO FAZ SENTIDO A MENSAGEM DE ESTOQUE BAIXO APARECER, POIS O ESTOQUE MINIMO E IGUAL A QUANTIDADE EM ESTOQUE. O CERTO SERIA INSERIR MAIS UM ELIF PARA VERIFICAR SE A QUANTIDADE EM ESTOQUE E IGUAL AO ESTOQUE MINIMO, E NESSE CASO, A MENSAGEM QUE DEVERIA APARECER SERIA "ESTOQUE OK"
# =====================================================================================================================================================================
    


    

