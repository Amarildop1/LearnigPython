## Projeto Final da Disciplina de Algoritmos e Programação Estruturada.


### 1 DESCRIÇÃO

Uma empresa provedora de internet, cujo domínio é “ifnet.com.br”, deseja manter os dados dos seus clientes salvos em um arquivo de texto. Cada linha do arquivo armazena os dados de um cliente que são CPF, nome e e-mail, ambos separados por “;” (ponto-e-vírgula).

O programa deverá exibir um menu, repetidamente, com as seguintes opções a ser escolhida pelo usuário:
	* [1] Cadastrar usuário
	* [2] Pesquisar usuário
	* [3] Alterar usuário
	* [4] Excluir usuário
	* [5] Listar usuários
	* [0] Sair

A descrição para cada opção encontra-se a seguir:

#### [1] Cadastrar usuário

Permite inserir os dados do usuário no arquivo. Tanto o CPF quanto o nome serão fornecidos via teclado. Em seguida, o sistema gerará e exibirá três opções de e-mail (baseados nos dados de entrada), cabendo ao usuário escolher uma delas. As opções de e-mail deverão seguir as seguintes regras:

	- Opção 1: número do CPF (sem digitos e pontos)+ @ + domínio da empresa
	- Opção 2: primeiro nome+.+ ultimo nome + @ + domínio da empresa
	- Opção 3: primeiro nome + três primeiros numeros do CPF + @ + domínio da empresa

Por exemplo, para o nome “Jose Antonio Filho”, de CPF: 123.456.789-01, as opções geradas são:

	1. 12345678901@ifnet.com.br
	2. jose.filho@ifnet.com.br
	3. jose123@ifnet.com.br

Após a escolha do e-mail, pelo usuário, todos os seus dados serão gravados no arquivo.
Observação: não deverá ser permitida a inserção de CPF e e-mail repetidos.

### [2] Pesquisar usuário

Permite realizar a busca de um usuário, através do CPF, mostrando na tela todos os dados dele. O sistema deverá informar caso o CPF não exista no arquivo.

[3] Alterar usuário
Permite alterar o nome do usuário, localizando-o através do CPF. O novo nome será fornecido pelo
usuário. O sistema deverá informar CPF não exista no arquivo.

[4] Excluir usuário
Permite excluir um usuário, através do CPF. Deverá ser mostrado na tela os dados do usuário e
solicitado uma confirmação para a exclusão. O sistema deverá informar caso o CPF não exista no
arquivo.

[5] Listar usuários
Permite listar na tela todos os usuários, sendo um por linha. Ao final da listagem deve ser mostrada
a quantidade de usuários listados.

[0] Sair
Encerra a execução do programa.

2 REQUISITOS NÃO FUNCIONAIS
Os seguintes requisitos não funcionais deverão pautar todo o projeto e desenvolvimento:
 Inclua comentários contendo a identificação dos programadores.
 Utilize modularização, documentando as funções através de comentários.
 Interface simples, porém, amigável.