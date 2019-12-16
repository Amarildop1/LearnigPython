"""
    TO DO:
    AINDA NÃO SUPORTA USUÁRIO BURRO
"""
   
arq = open("CadastroDeUsuarios", 'a')

#CADASTRO DE USUÁRIO
def cadastrarUsuario():
        print("\nPreencha os dados abaixo:")
        cpf = input(" CPF: ")
        nome = input(" Nome: ")

        #CHAMA FUNÇÃO GERADOR DE EMAIL
        emailEscolhido = geradorDeEmail(cpf, nome)

        arq.write(cpf + ';' + nome + ';' + emailEscolhido + ';' + '\n')
        print("Cadastro realizado com sucesso!")
        print("\nE-mail escolhido: ", emailEscolhido)


#GERADOR DE EMAIL
def geradorDeEmail(cpf, nome):
        dominio = "@ifnet.com.br"
        print("\nOpções de e-mail: ")

        #Limpando os pontos e dígitos do CPF
        cpfFormatado = cpf.replace('.', '')
        cpfFormatado = cpfFormatado.replace('-','')

        print(" [1] " + cpfFormatado + dominio)
        
        vetorNome = nome.split(' ')
        print(" [2] " + vetorNome[0] + "." + vetorNome[-1] + dominio )
        
        vetorCpf = cpf.split('.')
        print(" [3] " + vetorNome[0] + vetorCpf[0] + dominio + '\n')
        
        opcao = int(input("Escolha uma opção: "))
        if(opcao == 1):
            emailEscolhido = cpfFormatado + dominio
        elif (opcao == 2):
            emailEscolhido = vetorNome[0] + '.' + vetorNome[-1] + dominio
        elif (opcao == 3):
            emailEscolhido = vetorNome[0] + vetorCpf[0] + dominio
        else:
            emailEscolhido = ' '
        
        return emailEscolhido


#PESQUISAR USUÁRIO





#PROGRAMA PRINCIPAL
cond = True;
while cond != 0 :
    print("\n***** MENU PRINCIPAL *****")
    print("\n [1] Cadastrar Usuário")
    print(" [2] Pesquisar Usuário")
    print(" [3] Alterar Usuário")
    print(" [4] Excluir Usuário")
    print(" [5] Listar Usuários")
    print(" [0] Sair")
    cond = int(input("\nInforme o número da operação: "))
    if cond == 1:
        cadastrarUsuario()
    elif cond == 2:
        pesquisar = input("Pesquisando ... ")
    elif cond == 3:
        alterar = input("Alterar ... ")
    elif cond == 4:
        excluir = input("Excluir ... ")
    elif cond == 5:
        listar = input("Listando ...")
    elif cond == 0:
        print("Fim do programa")
    else:
        print("\n:/ Ops! Digite uma operação válida. ;)")


arq.close()