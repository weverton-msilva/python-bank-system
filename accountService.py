# =========================
# FUNÇÕES DO BANCO (Em andamento ainda!)
# =========================
def deposit(account):
    while True:
        # Receber o valor de entrada
        value_deposit = input("Valor de deposito: ").strip()
        
        # Verificar o valor inserido
        if not value_deposit:
            print("Informe o valor de deposito!")
            continue
        
        try:
            value_deposit = float(value_deposit)
            
            if value_deposit <= 0:
                print("Preencha com valores maiores que 0.")
                continue
            
            account['Saldo'] += value_deposit
            print("Depósito realizado com sucesso!")
            break
        
        except ValueError:
            print("Digite apenas números, tente novamente.")
            continue
    

def withdraw(account):
    pass
    
    
def transfer(account):
    pass
    
    
def view_statement(account):
    pass