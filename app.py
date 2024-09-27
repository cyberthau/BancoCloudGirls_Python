import os
import json

clientes = [{'id': 1, 'nome':'Ada Lovelace', 'email': 'ada@lovelace', 'telefone': '123456789', 'status': True},
            {'id': 2, 'nome':'Alan Turing', 'email': 'alan@turing', 'telefone': '987654321', 'status': False},
            {'id': 3, 'nome':'Grace Hopper', 'email': 'grace@hopper', 'telefone': '543216987', 'status': True}]

# função para carregar os dados do banco de dados
def carregar_dados():
    global clientes
    try:
        with open('clientes.json', 'r') as arquivo:
            clientes = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo de clientes não encontrado. Iniciando com dados vazios.")
        clientes = [{'id': 1, 'nome':'Ada Lovelace', 'email': 'ada@lovelace', 'telefone': '123456789', 'status': True},
                   {'id': 2, 'nome':'Alan Turing', 'email': 'alan@turing', 'telefone': '987654321', 'status': False},
                   {'id': 3, 'nome':'Grace Hopper', 'email': 'grace@hopper', 'telefone': '543216987', 'status': True}]

# função salvar - utilizada para gravar os dados no banco de dados 
def salvar_dados():
    with open('clientes.json', 'w') as arquivo:
        json.dump(clientes, arquivo, indent=4)

# função cadastrar cliente
def cadastrar_cliente():
    limpar_tela()
    print('Cadastar Cliente')
    nome = input('Digite o nome do cliente: ')
    email = input('Digite o email do cliente: ')
    telefone = input('Digite do telefone do cliente: ')
    clientes.append({'id' : len(clientes) +1, 'nome' : nome, 'email' : email, 'telefone' : telefone, 'status': True})
    print('Cliente cadastrado com sucesso!')
    salvar_dados()
    main()

# função listar clientes
def listar_cliente():
    limpar_tela()
    print('Listar Cliente')
    if clientes:  # Verifica se a lista não está vazia
        for cliente in clientes:
            status = 'Ativo' if cliente['status'] else 'Inativo'
            print(f'ID: {cliente["id"]} | Nome: {cliente["nome"]} | Email: {cliente["email"]} | Telefone: {cliente["telefone"]} | Status: {status}')
    else:
        print("Não há clientes cadastrados.")
    main()

# função atualizar clientes
def atualizar_cliente():
    limpar_tela()
    print('Atualizar Dados do Cliente')

    # como buscar o cliente que será alterado
    id_cliente = int(input('Digite o id do cliente:'))
    
    # campos que serão atualizados
    nome = input('Digite o nome do cliente: ')
    email = input('Digite o email do cliente: ')
    telefone = input('Digite o telefone do cliente: ')

    # logica para buscar o cliente que será alterado
    cliente = clientes[id_cliente - 1]

    # como é realizado a atualização do cliente no banco
    cliente['nome'] = nome
    cliente['email'] = email
    cliente['telefone'] = telefone
    print('Dados Atualizados')
    status = 'Ativo' if cliente['status'] else 'Inativo'
    print(f'ID: {cliente['id']} | Nome: {cliente['nome']} | Email: {cliente['email']} | Telefone{cliente['telefone']} | Status: {status}')
    salvar_dados()
    print('Cliente atualizado com sucesso!')
    main()

# função inativar cliente
def inativar_cliente():
    limpar_tela()
    print('Inativar Cliente')

    # como buscar o cliente que será inativado
    id_cliente = int(input('Digite o id do cliente:'))

    # logica para buscar o cliente que será alterado
    cliente = clientes[id_cliente - 1]

    # logica de alteração do status
    cliente['status'] = False
    salvar_dados()
    print('Cliente inativado com sucesso!')
    main()

# função sair
def sair():
    print('Programa finalizado!')
    

# função opção inválida
def opcao_invalida():
    print('Opção inválida')
    main()

# função exibir nome programa
def exibir_nome_programa():
    print("""
██████╗░░█████╗░███╗░░██╗░█████╗░░█████╗░  ░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗██║░░░██║██╔══██╗
██████╦╝███████║██╔██╗██║██║░░╚═╝██║░░██║  ██║░░╚═╝██║░░░░░██║░░██║██║░░░██║██║░░██║
██╔══██╗██╔══██║██║╚████║██║░░██╗██║░░██║  ██║░░██╗██║░░░░░██║░░██║██║░░░██║██║░░██║
██████╦╝██║░░██║██║░╚███║╚█████╔╝╚█████╔╝  ╚█████╔╝███████╗╚█████╔╝╚██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░  ░╚════╝░╚══════╝░╚════╝░░╚═════╝░╚═════╝░

░██████╗░██╗██████╗░██╗░░░░░░██████╗
██╔════╝░██║██╔══██╗██║░░░░░██╔════╝
██║░░██╗░██║██████╔╝██║░░░░░╚█████╗░
██║░░╚██╗██║██╔══██╗██║░░░░░░╚═══██╗
╚██████╔╝██║██║░░██║███████╗██████╔╝
░╚═════╝░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░""")

# função par exibir as opções
def exibir_opcoes_clientes():
    print('1. Cadastrar Cliente')
    print('2. Listar Clientes')
    print('3. Atualizar Dados do Cliente')
    print('4. Inativar Cliente')
    print('5. Sair\n')

# função para selecionar a opção desejada
def escolher_opcao():
    opcao_selecionada = input('Digite a opção desejada:')

    if opcao_selecionada == '1':
        cadastrar_cliente()
    elif opcao_selecionada == '2':
        listar_cliente()
    elif opcao_selecionada == '3':
        atualizar_cliente()
    elif opcao_selecionada == '4':
        inativar_cliente()
    elif opcao_selecionada == '5':
        sair()
    else:
        opcao_invalida()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

carregar_dados()

# função main para poder rodar o sistema
def main():
    exibir_nome_programa()
    exibir_opcoes_clientes()
    escolher_opcao()

if __name__ == '__main__':
    main()