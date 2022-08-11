# Funções
def menu():
    opc = int(input(
        f'{20*"="}\n[1] Cadastro Usuário\n[2] Login Usuário\n[3] Excluir Cadastro\n[0] Sair\nDigite a opção: '))
    print(20*'=')
    return opc


def cadastro():
    while True:
        nome = input('Digite o seu nome completo: ')  # PEGAR NOME
        while True:
            email = input('Digite seu e-mail: ')  # PEGAR EMAIL
            if '@' not in email:
                print('Digite um email válido!')  # NÃO TEM @ NO EMAIL
            elif email in usuarios_cadastrados:
                print('Esse email já está cadastrado.')  # EMAIL JA CADASTRADO
            else:
                break
        senha = input('Digite sua senha: ')  # PEGAR SENHA
        while True:
            if len(senha) < 6:
                print('Sua senha deve conter no mínimo 6 caracteres.') # NÃO TEM 6 CARACTERES A SENHA
                senha = input('Digite sua senha: ')
            else: 
                confirmarSenha = input('Confirme sua senha: ') # CONFIRMAR SENHA
                if confirmarSenha == senha:
                    print(f'Cadastro concluido, seja bem vindo {nome}!') # CONFIRMOU A SENHA
                    break
                else:
                    print(f'A confirmação da senha não corresponde.') # SENHAS NAO COMPATIVEIS
        usuarios_cadastrados[email] = [senha, nome] # COLOCAR CADASTRO NO DICIONARIO { EMAIL : [SENHA, NOME]}
        break


def login():
    if len(usuarios_cadastrados) == 0: # NENHUM USUARIO CADASTRADO ( LISTA VAZIA )
        print('Nenhum usuário cadastrado.')
    else:
        while True:
            emailLogin = input('Digite seu email: ')  # PEGAR EMAIL
            if '@' not in emailLogin:
                print('Digite um email válido!')  # NÃO TEM @ NO EMAIL
            elif emailLogin not in usuarios_cadastrados:
                print('E-mail não cadastrado.')  # NÃO TEM EMAIL CADASTRADO
            else:
                break   
        while True:
            senhaLogin = input('Digite sua senha: ')  # PEGAR SENHA LOGIN
            for k, v in usuarios_cadastrados.items():
                while k == emailLogin:  # ACHAR EMAIL NO DICIONARIO
                    if v[0] == senhaLogin:  # COMPARAR EMAIL E SENHA
                        print(f'Olá {v[1]}, login efetuado.') # DAR OLA COM O NOME DO EMAIL CADASTRADO
                        break
                    else:
                        print(f'Senha incorreta!')  # SENHA INCORRETA
                        senhaLogin = input('Digite sua senha: ')  # PEGAR SENHA LOGIN
            break


def excluir():
    if len(usuarios_cadastrados) == 0: # NENHUM USUARIO CADASTRADO ( LISTA VAZIA )
        print('Nenhum usuário cadastrado.')
    else:
        while True:
            emailExcluir = input('Digite o email do cadastro que deseja excluir: ')  # PEGAR EMAIL
            if '@' not in emailExcluir:
                print('Digite um email válido!')  # NÃO TEM @ NO EMAIL
            elif emailExcluir not in usuarios_cadastrados:
                print('E-mail não cadastrado.')  # NÃO TEM EMAIL CADASTRADO
            else:
                break
        while True: # PEGAR SENHA EXCLUIR
            senhaExcluir = input('Digite sua senha: ') #PEGAR SENHA EXCLUIR
            for k, v in usuarios_cadastrados.items():
                while True:
                    if k == emailExcluir: #ACHAR EMAIL NO DICIONARIO
                        if v[0] == senhaExcluir: # COMPARAR EMAIL E SENHA
                            confirmacao = input('Para excluir o cadastro digite "CONFIRMAR": ') # CONFIRMAÇÃO PARA EXCLUIR
                            while confirmacao != 'CONFIRMAR':
                                print('Confirmação negada, conta não excluida.') # CONFIRMAÇAO DIGITADA ERRADA
                                confirmacao = input('Digite "CONFIRMAR" correamente: ') # CONFIRMAÇÃO PARA EXCLUIR
                            print(f'Cadastro Excluido.\nÉ uma pena te perder {v[1]}')
                            usuarios_cadastrados.pop(emailExcluir) # EXCLUIR O CADASTRO
                            break
                        else:
                            print(f'Senha incorreta.') #SENHA INCORRETA
                            senhaExcluir = input('Digite sua senha: ') #PEGAR SENHA EXCLUIR
                break
            break

# Dicionario
usuarios_cadastrados = dict()

# Sistema
print('BEM VINDO A CODIFY')
while True:
    x = menu()
    if x == 0:  # SAIR DO PROGRAMA
        print('Obrigado por usar nossa plataforma, volte sempre!')
        break
    elif x == 1:  # CADASTRO DE USUÁRIO
        cadastro()
    elif x == 2:  # LOGIN USUÁRIO
        login()
    elif x == 3:  # EXCLUIR CADASTRO
        excluir()
    else:  # OPCAO NAO ESTA ENTRE 0 E 3
        print('Digite uma opção válida.')
