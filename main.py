# IMPORTA ARQUIVOS NECESSÁRIOS
import account


# FUNÇÃO DO MENUS DO USUÁRIO
def user_interface():
    while True:
        print("=" * 10 + " SISTEMA BANCÁRIO " + "=" * 10)
        print() # Espaço para organização

        # Dicionário de opções e impressão do mesmo em tela
        account_options = {
            1: "Acessar o sistema",
            2: "Criar uma conta",
            3: "Sair do sistema"
        }

        for key, value in account_options.items():
            print(f"{key} - {value}")

        # Solicitação da entrada de dados da parte do usuário
        user_account = input("Opção selecionada: ").strip()
        print(user_account) # Retirar após finalizar código

        # Verificar a entrada e transforma em inteiro
        if not user_account:
            print("Favor preencher o campo obrigátorio!")
            continue

        try:
            user_account = int(user_account)
            
            if user_account not in account_options:
                print("Favor preencher o campo apenas com 1 até 3")
                continue

            return user_account
        except ValueError:
            print("Favor preencher o campo com números inteiros!")


# DIRECIONAR USUÁRIO AO SISTEMA DE CONTA
def menu_controller():
    user_account =  user_interface()

    # Sair do sistema ao verificar opção
    if user_account == 3:
        print("Saindo do sistema, aguarde um momento...")
        return False

    # Encaminhamento do usuário a função correta
    selected_option = {
        1: account.access_account,
        2: account.register_account
    }

    selected_option[user_account]()
    
# EXECUTAR FUNÇÃO
while True:
    if menu_controller() == False:
        break