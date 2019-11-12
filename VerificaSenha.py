senha = 'abcd'
erro = 0 

while(erro != 3):   #Com while True também funciona 
    tentativa = input("\nInforme a Senha: ")
    if(tentativa == senha):
        print("Senha correta!")
        break
    else:
        erro += 1
        print("Senha incorreta.")
        if(erro == 3):
            break
        print("Tente novamente!")
        
'''
Solicita uma senha do usuário e verifica se acertou.
Senha correta: abcd
Três tentativas erradas encerra o programa.
'''
#@Author Amarildo
#L3-Q15 - 14.Out.2019