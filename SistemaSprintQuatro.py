# Funções

# Função de Menu Pré Login
def menu():
    try:
        opc = int(input(
            f'{20 * "="}\n[1] Cadastro Usuário\n[2] Login Usuário\n[0] Sair\nDigite a opção: '))
        print(20 * '=')
        return opc
    except:
        return 3


# Função de Cadastro
def cadastro():
    while True:
        nome = input('Digite o seu nome completo: ')
        while True:
            email = input('Digite seu e-mail: ')
            if '@' not in email:
                print('Digite um email válido!')
            elif email in usuarios_cadastrados:
                print('Esse email já está cadastrado.')
            else:
                break
        senha = input('Digite sua senha: ')
        while True:
            if len(senha) < 6:
                print('Sua senha deve conter no mínimo 6 caracteres.')
                senha = input('Digite sua senha: ')
            else:
                confirmarSenha = input('Confirme sua senha: ')
                if confirmarSenha == senha:
                    usuarios_cadastrados[email] = [senha, nome]
                    return f'Cadastro concluido, seja bem vindo {nome}!'
                else:
                    print(f'A confirmação da senha não corresponde.')


# Função de login
def login():
    if len(usuarios_cadastrados) == 0:
        return 'Nenhum usuário cadastrado.'
    else:
        while True:
            emailLogin = input('Digite seu email: ')
            if '@' not in emailLogin:
                print('Digite um email válido!')
            elif emailLogin not in usuarios_cadastrados:
                print('E-mail não cadastrado.')
            else:
                break
        while True:
            senhaLogin = input('Digite sua senha: ')
            for k, v in usuarios_cadastrados.items():
                while k == emailLogin:
                    if v[0] == senhaLogin:
                        return f'Olá {v[1]}, login efetuado.'
                    else:
                        print(f'Senha incorreta!')
                        senhaLogin = input('Digite sua senha: ')

# Função de excluir cadastro
def excluirCadastro():
    if len(usuarios_cadastrados) == 0:
        return 'Nenhum usuário cadastrado.'
    else:
        while True:
            emailExcluir = input('Digite o seu email da sua conta que deseja excluir: ')
            if '@' not in emailExcluir:
                print('Digite um email válido!')
            elif emailExcluir not in usuarios_cadastrados:
                print('E-mail não cadastrado.')
            else:
                break
        while True:
            senhaExcluir = input('Digite sua senha: ')
            for k, v in usuarios_cadastrados.items():
                while True:
                    if k == emailExcluir:
                        if v[0] == senhaExcluir:
                            confirmacao = input(
                                'Para excluir o cadastro digite "CONFIRMAR": ')
                            while confirmacao != 'CONFIRMAR':
                                print('Confirmação negada, conta não excluida.')
                                confirmacao = input('Digite "CONFIRMAR" correamente: ')
                            usuarios_cadastrados.pop(emailExcluir)
                            return f'Cadastro Excluido.\nÉ uma pena te perder {v[1]}'
                        else:
                            print(f'Senha incorreta.')
                            senhaExcluir = input('Digite sua senha: ')

# Função de Menu escolhas após logar
def menuCodify():
    try:
        opcMenu = int(input(
            f'{20 * "="}\n[1] Fazer teste teôrico de Python\n[2] Configuração\n[0] Sair\nDigite a opção: '))
        print(20 * '=')
        return opcMenu
    except:
        return 4


# Função de Menu de configurações
def menuConfiguracao():
    try:
        opcConfig = int(input(
            f'[1] Alterar Email\n[2] Alterar Senha\n[3] Excluir Conta\nDigite a opção: '))
        print(20 * '=')
        return opcConfig
    except:
        return 4


# Função de Alterar Senha
def alterarSenha():
    while True:
        emailAlterar = input('Digite o seu email da sua conta: ')
        if '@' not in emailAlterar:
            print('Digite um email válido!')
        elif emailAlterar not in usuarios_cadastrados:
            print('E-mail não cadastrado.')
        else:
            break
    while True:
        senhaAlterar = input('Digite sua senha: ')
        for k, v in usuarios_cadastrados.items():
            while True:
                if k == emailAlterar:
                    if v[0] == senhaAlterar:
                        while True:
                            novaSenha = input('Digite sua nova senha: ')
                            if len(novaSenha) < 6:
                                print('Sua senha deve conter no mínimo 6 caracteres.')
                            else:
                                confirmarSenha = input('Confirme sua senha: ')
                                if confirmarSenha == novaSenha:
                                    usuarios_cadastrados[emailAlterar][0] = novaSenha
                                    return f'Sua senha foi alterada com sucesso!'
                                else:
                                    print(f'A confirmação da senha não corresponde.')
                    else:
                        print(f'Senha incorreta.')
                        senhaAlterar = input('Digite sua senha: ')

# Função de Alterar Email
def alterarEmail():
    while True:
        emailAlterar = input('Digite o seu email da sua conta: ')
        if '@' not in emailAlterar:
            print('Digite um email válido!')
        elif emailAlterar not in usuarios_cadastrados:
            print('E-mail não cadastrado.')
        else:
            break
    while True:
        senhaAlterar = input('Digite sua senha: ')
        for k, v in usuarios_cadastrados.items():
            while True:
                if k == emailAlterar:
                    if v[0] == senhaAlterar:
                        while True:
                            NovoEmail = input('Digite seu novo e-mail: ')
                            if '@' not in NovoEmail:
                                print('Digite um email válido!')
                            elif NovoEmail in usuarios_cadastrados:
                                print('Esse email já está cadastrado.')
                            else:
                                confirmarEmail = input('Confirme seu Email: ')
                                if confirmarEmail == NovoEmail:
                                    usuarios_cadastrados[NovoEmail] = usuarios_cadastrados.pop(emailAlterar)
                                    return f'Seu email foi alterado com sucesso!'
                                else:
                                    print('Os email não correspondem')


# Função do teste teôrico de Python
def testePython():
    cont = 0
    print('Olá seja bem vindo ao teste teôrico de Python\n'
          'Serão 5 perguntas de multiplas escolhas.\n'
          'Digite a opção de 1 a 5 se não sua resposta não será validada.\n'
          f'{20 * "="}')
    print(
        'Na disciplina de ciência de dados, Python é uma das linguagens de programação mais utilizadas. A esse respeito, é correto afirmar que a linguagem de programação Python'
        '\n[1] mostra-se ideal para desenvolvimento rápido e criação de scripts em razão de sua natureza compilada.'
        '\n[2] possui recursos para controle de fluxo, como if-else, switch-case, while e for em todas as suas versões. '
        '\n[3] classifica-se como fracamente tipada. '
        '\n[4] foi desenvolvida com o intuito de substituir a linguagem de programação C por causa de sua altíssima performance. '
        '\n[5] pode ser utilizada como uma linguagem de programação funcional.')
    while True:
        try:
            exercicioUm = int(input('Resposta: '))
            if exercicioUm == 5:
                cont += 1
            break
        except:
            print("Digite uma opção valida")
    print(167 * "=")
    print(
        'Três estruturas de dados fundamentais em Python são as listas (“list”), tuplas (“tuple”) e dicionários (“dict”). A respeito dessas estruturas, é correto afirmar que: '
        '\n[1] Dicionários não podem ser modificados depois de criados, ao passo que listas e tuplas podem.'
        '\n[2] Dicionários e tuplas são indexados por inteiros, ao passo que listas podem ser indexadas por “strings”.'
        '\n[3] Listas podem ser modificadas, mas seu tamanho não pode ser modificado após a criação, ao passo que tuplas e dicionários não têm essa limitação.'
        '\n[4] Tuplas e listas são indexadas por inteiros, ao passo que dicionários podem ser indexados por “strings”.'
        '\n[5] Listas não podem ser modificadas depois de criadas, ao passo que tuplas e dicionários podem.')
    while True:
        try:
            exercicioDois = int(input('Resposta: '))
            if exercicioDois == 4:
                cont += 1
            break
        except:
            print("Digite uma opção valida")
    print(167 * "=")
    print('Analise o script Python 3.8 exibido a seguir.'
          '\nL=["A","E","I","O","U"]'
          '\nfor k in range(0,len(L)):'
          '\n     print (L[4-k])'
          '\nAssinale a opção que indica a saída produzida pela execução desse código.'
          '\n[1] A E I O U'
          '\n[2] A E I O'
          '\n[3] E I O U'
          '\n[4] U O I E'
          '\n[5] U O I E A')
    while True:
        try:
            exercicioTres = int(input('Resposta: '))
            if exercicioTres == 5:
                cont += 1
            break
        except:
            print("Digite uma opção valida")
    print(167 * "=")
    print('Em relação à linguagem de programação Python, é INCORRETO afirmar que: '
          '\n[1] O tipo da variável pode ser inferido pelo interpretador em tempo de execução.'
          '\n[2] É necessário converter explicitamente o tipo da variável antes de uma operação entre tipos não compatíveis.'
          '\n[3] Os blocos de código são delimitados pelo uso das chaves: { e } para início e fim do bloco, respectivamente. '
          '\n[4] É uma linguagem orientada a objeto na qual os atributos e os métodos podem ser acessados usando o ponto (.).  '
          '\n[5] O interpretador Python pode ser usado de forma interativa em um prompt semelhante ao shell do sistema operacional. ')
    while True:
        try:
            exercicioQuatro = int(input('Resposta: '))
            if exercicioQuatro == 3:
                cont += 1
            break
        except:
            print("Digite uma opção valida")
    print(167 * "=")
    print('Qual será o resultado da seguinte expressão Python?'
          '\nprint(4.00/(2.0+2.0))'
          '\nAssinale a alternativa correta'
          '\n[1] Erro'
          '\n[2] 1.0 '
          '\n[3] 1.00 '
          '\n[4] 1'
          '\n[5] True')
    while True:
        try:
            exercicioCinco = int(input('Resposta: '))
            if exercicioCinco == 3:
                cont += 1
            break
        except:
            print("Digite uma opção valida")
    print(167 * "=")
    return f'Parabens você acertou {cont} questões!' if cont > 2 else f'Poxa você acertou {cont} questões!'


# Dicionario de usuario cadastrados
usuarios_cadastrados = dict()

# Sistema
print('BEM VINDO A CODIFY')
while True:
    x = menu()
    if x == 0:
        print('Obrigado por usar nossa plataforma, volte sempre!')
        break
    elif x == 1:
        print(cadastro())
    elif x == 2:
        print(login())
        if len(usuarios_cadastrados) > 0:
            while True:
                opcMenu = menuCodify()
                if opcMenu == 1:
                    print(testePython())
                elif opcMenu == 2:
                    opcConfig = menuConfiguracao()
                    if opcConfig == 1:
                        print(alterarEmail())
                    elif opcConfig == 2:
                        print(alterarSenha())
                    elif opcConfig == 3:
                        print(excluirCadastro())
                        break
                    else:
                        print('opção inválida.')
                elif opcMenu == 0:
                    print('Usuário deslogado! Volte sempre.')
                    break
                else:
                    print('Digite uma opção válida.')
    else:
        print('Digite uma opção válida.')
