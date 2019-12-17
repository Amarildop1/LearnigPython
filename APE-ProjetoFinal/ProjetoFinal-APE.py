arq = open("CadastroDeUsuarios", 'a')

#CADASTRO DE USUÁRIO
def cadastrarUsuario():
        arq = open("CadastroDeUsuarios", 'a')
        print("\nPreencha os dados abaixo:")
        cpf = input(" CPF: ")
        nome = input(" Nome: ")

        #CHAMA FUNÇÃO GERADOR DE EMAIL
        emailEscolhido = geradorDeEmail(cpf, nome)

        arq.write(cpf + ';' + nome + ';' + emailEscolhido + ';' + '\n')
        print("Cadastro realizado com sucesso!")
        print("\nE-mail escolhido: ", emailEscolhido)

        arq.close()
#FIM DA FUNÇÃO CADASTRO DE USUÁRIO


#GERADOR DE EMAIL
def geradorDeEmail(cpf, nome):
        dominio = "@ifnet.com.br"
        print("\nOpções de e-mail: ")

        #Limpando os pontos e dígitos do CPF
        cpfFormatado = cpf.replace('.', '')
        cpfFormatado = cpfFormatado.replace('-','')

        #Opções de e-mail para escolha do usuário
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
#FIM DA FUNÇÃO GERADOR DE EMAIL



#PESQUISAR USUÁRIO
def pesquisaUsuario(buscaCpf):
        cpfBarraN = '\n' + buscaCpf

        arq = open("CadastroDeUsuarios", 'r')
        pesquisa = arq.read().split(';')

        #Para servir na exibição dos dados
        nome = pesquisa.index(cpfBarraN)

        usuario = []
        for linha in pesquisa:
            if (linha == buscaCpf or linha == cpfBarraN):
                usuario.append(linha.split(';'))
                print("\n :) Usuário Encontrado!")
                print("\n-------------- Dados: -----------------")  
                print(f"""    CPF: {buscaCpf} 
    Nome: {pesquisa[nome+1]}
    E-mail: {pesquisa[nome+2]} """)
                print("===========================================")
                break
        else:
            print(f"\nCPF: {buscaCpf} não encontrado! :( ")
            #break
        arq.close()
#FIM DA FUNÇÃO PESQUISAR USUÁRIO



#ALTERAR USUÁRIO
def alterarUsuario(buscaCpf):
        cpfBarraN = '\n' + buscaCpf

        arq = open("CadastroDeUsuarios", 'r')
        pesquisa = arq.read().split(';')

        #ACHANDO PELO CPF E PEGANDO O NOME
        print("\n------- Usuário Encontrado ----------")
        indiceCPF = pesquisa.index(cpfBarraN)
        print("CPF:", buscaCpf)
        print("Nome:", pesquisa[indiceCPF+1])
        print("E-mail:", pesquisa[indiceCPF+2])

        novoNome = input("\nDigite um novo nome: ")
        buscaCpf = cpfBarraN
        emailEscolhido = pesquisa[indiceCPF+2]

        print("\n------- Alterado Para: --------")
        print("Nome:", novoNome)
        print("CPF:", buscaCpf)
        print("E-mail:", emailEscolhido)
        print("-------------------------------")

        usuario = []
        indice = pesquisa.index(cpfBarraN)
        for linha in pesquisa:
            if (linha == buscaCpf or linha == cpfBarraN):
                usuario.append(linha.split(';'))
                pesquisa[indice+1] = novoNome
                #arq = open("CadastroDeUsuarios", 'a') 
                #arq.write(buscaCpf + ';' + pesquisa[indice+1] + ';' + emailEscolhido + ';')
                break
        else:
            print(f"\nCPF: {buscaCpf} não encontrado! :( ")
            #break

        arq = open("CadastroDeUsuarios", 'a')    
        arq.write(buscaCpf + ';' + pesquisa[indice+1] + ';' + emailEscolhido + ';' + '\n')
        arq.close()
#FIM DA FUNÇÃO ALTERAR USUÁRIO




#EXCLUIR USUÁRIO
def excluirUsuario(buscaCpf):
        cpfBarraN = '\n' + buscaCpf

        arq = open("CadastroDeUsuarios", 'r')
        pesquisa = arq.read().split(';')

        #ACHANDO PELO CPF E PEGANDO O NOME
        print("\n------- Usuário Encontrado ----------")
        indiceCPF = pesquisa.index(cpfBarraN)
        print("CPF:", buscaCpf)
        print("Nome:", pesquisa[indiceCPF+1])
        print("E-mail:", pesquisa[indiceCPF+2])

        print("\nConfirme com [1]Sim ou [2]Não:")
        confirmacao = int(input("Deseja realmente excluir? "))
        if(confirmacao == 1):
            print("EXCLUINDO")
            usuario = []
            indice = pesquisa.index(buscaCpf)
            for linha in pesquisa:
                if (linha == buscaCpf or linha == cpfBarraN):
                    usuario.append(linha.split(';'))
                    print("DENTRO DO IF")
                    pesquisa[indice+0] = ''
                    pesquisa[indice+1] = ''
                    pesquisa[indice+2] = ''
                    print(pesquisa)
                    break
            else:
                print(f"\nCPF: {buscaCpf} não encontrado! :( ")
                #break
        elif(confirmacao == 2):
            print("NÃO VAI EXCLUIR")
        else:
            print("ALGUM ERRO")
        #arq.write(buscaCpf + ';' + pesquisa[indiceCPF+1 + ';' + emailEscolhido + ';' + '\n')
        arq.close()
#FIM DA FUNÇÃO EXCLUIR USUÁRIO



#LISTAR USUÁRIOS
def listarUsuarios():
        print("\n============ Lista de usuários cadastrados: ================\n")
        arq = open("CadastroDeUsuarios", 'r')
        qtdeUsuarios=0
        listaUsuarios = arq.read().split('\n')       
        for cont in listaUsuarios:
            print(cont)
            if cont != '':
                qtdeUsuarios += 1
        
        print(f"Quantidade de usuários: {qtdeUsuarios}")
        print("============================================================")
        arq.close()
#FIM DA FUNÇÃO LISTAR USUÁRIOS




#PROGRAMA PRINCIPAL
cond = True;
while cond != 0 :
    print("\n\n***** MENU PRINCIPAL *****")
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
        print("\n====== Pesquisa de usuário pelo CPF: ======")
        buscaCpf = input("\nInforme o CPF: ")
        pesquisaUsuario(buscaCpf)
    elif cond == 3:
        print("\n====== Alterar nome do usuário pelo CPF: ======")
        buscaCpf = input("\nInforme o CPF: ")
        alterarUsuario(buscaCpf)
    elif cond == 4:
        print("\n====== Excluir um usuário pelo CPF: ======")
        buscaCpf = input("\nInforme o CPF: ")
        excluirUsuario(buscaCpf)
    elif cond == 5:
        listarUsuarios()
    elif cond == 0:
        print("Fim do programa.")
    else:
        print("\n:/ Ops! Digite uma operação válida. ;)")


arq.close()