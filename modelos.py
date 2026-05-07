class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente  # Agregação
        self._saldo = 0.0  # Encapsulamento: saldo protegido

    def get_saldo(self):
        """Retorna o saldo atual (Getter)."""
        return self._saldo
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor 
            print(f"Depósito de R$ {valor:.2f} efetuado.")

        else:
            print("Valor de depósito inválido!")
        

    def sacar(self, valor):

        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} autorizado.")
            return True
        else:
            print("Operação recusada! Saldo insuficiente.")
            return False

    def transferir(self, valor, conta_destino):

        print(f"Iniciando transferência de R$ {valor:.2f}...")
        if self.sacar(valor):
            conta_destino.depositar(valor)
            print("Transferência concluída!") # Parêntese corrigido aqui
            return True
        else:
            print("Falha na transferência.")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        # Usa o super() para herdar o construtor da Conta
        super().__init__(numero, cliente) 

    def sacar(self, valor):
        """Sobrescrita (Polimorfismo): cobra taxa de R$ 1,00."""
        taxa = 1.00
        valor_total = valor + taxa 
        if 0 < valor_total <= self._saldo:
            self._saldo -= valor_total
            print(f"Saque de R$ {valor:.2f} (Taxa: R$ {taxa:.2f}) autorizado.")
            return True
        else:
            print("Operação recusada! Saldo insuficiente para o saque + taxa.")
            return False

class ContaPoupanca(Conta):
    def render_juros(self):
        """Método exclusivo da Poupança: rende 1% (x 1.01)."""
        rendimento = self._saldo * 0.01
        self._saldo *= 1.01
        print(f"Rendimento de R$ {rendimento:.2f} aplicado com sucesso.")