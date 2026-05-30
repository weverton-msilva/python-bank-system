# =========================
# IMPORTA ARQUIVOS NECESSÁRIOS
# =========================
import accountService


# =========================
# DADOS DO SISTEMA
# =========================
accounts = []


# =========================
# VALIDAÇÕES
# =========================
def validate_name(account_name):
    if not account_name:
        return False

    if len(account_name) < 5 or len(account_name) > 80:
        return False

    if " " not in account_name:
        return False

    return True
    
def validate_email(account_email):
    if not account_email:
        return False
    
    if len(account_email) < 5 or len(account_email) > 80:
        return False
    
    if not account_email.endswith(("@gmail.com", "@outlook.com", "@hotmail.com", "@yahoo.com")):
        return False
        
    return True

def validate_cpf(account_cpf):
    if not account_cpf:
        return False
        
    if len(account_cpf) != 11:
        return False
        
    if not account_cpf.isdigit():
        return False

    return True 

def validate_password(account_password):
    if not account_password:
        return False

    if len(account_password) < 8 or len(account_password) > 32:
        return False

    if " " in account_password:
        return False

    return True


# =========================
# CADASTRAR CONTA
# =========================
def register_account():
    while True:
        print("=" * 10 + " CADASTRAR CONTA " + "=" * 10)
        print() # Espaço para organização

        # Entrada de dados pessoais da conta 
        account_name = input("Nome completo: ").strip().title()
        account_email = input("Email: ").strip()
        account_cpf = input("CPF: ").strip()
        account_password = input("Senha: ").strip()

        # Verificar as informações usando função
        if not validate_name(account_name):
            print("Preencha o nome corretamente!")
            continue
        
        if not validate_email(account_email):
            print("Preencha o email corretamente!")
            continue

        if not validate_cpf(account_cpf):
            print("Preencha seu CPF corretamente!")
            continue

        if not validate_password(account_password):
            print("Preencha sua senha corretamente!")
            continue

        # Criar um código para a conta do usuário
        account_number = len(accounts) + 1

        # Dicionário com as informações da conta
        account = {
            "Número": account_number,
            "Nome": account_name,
            "Email": account_email,
            "CPF": account_cpf,
            "Senha": account_password,
            "Saldo": 0.0,
            "Histórico": []
        }

        # Adicionar informações na lista de contas
        accounts.append(account)

        print("Conta cadastrada com sucesso!")
        break


# =========================
# ACESSAR CONTA
# =========================
def access_account():
    while True:
        print("=" * 10 + " ACESSAR CONTA " + "=" * 10)
        print() # Espaço para organização

        # Entrada de informações para acessar
        account_email = input("Email: ").strip()
        account_password = input("Senha: ").strip()

        # Verificar do preenchimento das informações  
        if not validate_email(account_email):
            print("Preencha seu email corretamente!")
            continue

        if not validate_password(account_password):
            print("Preencha sua senha corretamente!")
            continue

        # Verificar se existe essa conta no sistema
        for account in accounts:
            if account_email == account["Email"] and account_password == account["Senha"] :
                print(f"Seja bem vindo, {account['Nome']}!")
                user_interface(account)
                return

        print("Conta não encontrada, tente novamente!")
        return
    

# =========================
# INTERFACE DO SISTEMA DO USUÁRIO
# =========================
def user_interface(account):
    while True:
        # Informações do usuário cadastrado
        print() # Organização
        print(f"Usuário: {account['Número']} - {account['Nome']}")
        print(f"Saldo atual: {account['Saldo']}")

        print() # Espaço para organização
        print("Opções disponíveis")

        # Dicionário do menu de opções
        option_map = {
            1: "Depositar",
            2: "Sacar",
            3: "Transferir",
            4: "Ver Extrato",
            5: "Sair"
        }
    
        # Imprimir dicionário
        for key, value in option_map.items():
            print(f"{key} - {value}")

        # Receber a entrada do usuário
        user_option = input("Opção: ").strip()

        # Verificar a entrada e transforma em inteiro
        try:
            user_option = int(user_option)

            if user_option not in option_map:
                print("Escolha uma opção válida do menu.")
                continue

        except ValueError:
            print("Favor preencher o campo com números inteiros!")
            continue
        
        # Sair do sistema ao verificar opção
        if user_option == 5:
            print("Saindo do sistema, aguarde um momento...")
            break

        # Encaminhamento do usuário a função correta
        option_function = {
            1: accountService.deposit,
            2: accountService.withdraw,
            3: accountService.transfer,
            4: accountService.view_statement
        }
        
        # Executar função solicitada
        option_function[user_option](account)