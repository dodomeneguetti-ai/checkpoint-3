from modelos import Cliente, ContaCorrente, ContaPoupanca

def terminal_bank():
    print("--- Bem-vindo ao Terminal Bank ---")
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    
    
    user = Cliente(nome, cpf)
    minha_conta = ContaCorrente("1001-5", user)

    
    while True:
        print(f"\nOlá, {minha_conta.cliente.nome} | Conta: {minha_conta.numero}")
        print("1. Ver Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        
        opcao = input("Escolha uma operação: ")

        match opcao:
            case "1":
                print(f"Saldo Disponível: R$ {minha_conta.get_saldo():.2f}") 
            
            case "2":
                valor = float(input("Quanto deseja depositar? R$ "))
                minha_conta.depositar(valor)
            
            case "3":
                valor = float(input("Quanto deseja sacar? R$ "))
                minha_conta.sacar(valor)
            
            case "4":
                print("Encerrando sessão. Tenha um bom dia!")
                break
            
            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    terminal_bank()