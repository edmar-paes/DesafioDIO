menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do Deposito? "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Valor depositado: R$ {extrato}")
        else:
            print("Operação falhou! O valor informdo é invalido.")
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque? "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUES
        if excedeu_saldo:
            print("Operação falhou! Voce não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saque:
            print("Operação falhou! Numero maximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
        else:
            print("Operação falhou! O valor informdo é invalido.")
    elif opcao == "e":
        print("\n######################## EXTRATO ######################")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print( f"Saldo: R$ {saldo}")
        print("#########################################################")
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por selecione novamente a operação desejada.")