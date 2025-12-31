from conta import ContaBancaria
from string import ascii_letters

caracteres_validos = set(ascii_letters + ' áéíóúâêôãõçÁÉÍÓÚÂÊÔÃÕÇ') 
while True:
    nome = input("Digite o nome do titular da conta: ""\n")
    if all(c in caracteres_validos for c in nome):
        break
    else:
        print("Nome inválido. Use apenas letras, acentos e espaços.""\n")

conta = ContaBancaria(nome)
print(f"{conta.exibir_dados()}\n")

while True:
    valor_deposito = conta.ler_float("Digite o valor para depósito: ""\n")
    if valor_deposito is not None and conta.depositar(valor_deposito):
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.""\n")
        break
    elif valor_deposito is None:
        print()  # Mensagem de erro já é exibida na função ler_float
    else:
        print("Valor de depósito inválido. O valor não pode ser um número negativo ou zero.""\n")

while True:   
    valor_saque = conta.ler_float("Digite o valor para saque: ""\n")
    if valor_saque is not None and conta.sacar(valor_saque):
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso.""\n")
        break
    elif valor_saque is None:
        print() 
    elif valor_saque <=0:
        print("Valor de saque inválido. O valor não pode ser um número negativo ou zero.""\n")
    else:
        print(f"O saldo de R${conta.saldo:.2f}, é insuficiente para a realização desta transação.""\n")


print(conta.exibir_dados())

