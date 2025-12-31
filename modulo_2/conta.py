class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
         
    def exibir_dados(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}"

    def depositar(self,valor):
        if valor is not None and valor>0:
            self.saldo+=valor
            return True
        return False
    
    def sacar(self,valor):
        if valor <= self.saldo and valor>0:
            self.saldo -=valor
            return True
        return False

    def ler_float(self, mensagem):
        try:
            return float(input(mensagem).replace(",","."))
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")
            return None

   