import Controller
import os.path

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write('')

criarArquivos('estoque.txt', 'fornecedores.txt', 'clientes.txt', 'funcionarios.txt', 'vendas.txt', 'categorias.txt')

if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar ( Categorias )\n"
                          "Digite 2 para acessar ( Estoque )\n"
                          "Digite 3 para acessar ( Fornecedor )\n"
                          "Digite 4 para acessar ( Cliente )\n"
                          "Digite 5 para acessar ( Funcionario )\n"
                          "Digite 6 para acessar ( Vendas )\n"
                          "Digite 7 para ver os produtos mais vendidos\n"
                          "Digite 8 para sair\n"))
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para adicionar uma categoria\n"
                                  "Digite 2 para remover uma categoria\n"
                                  "Digite 3 para alterar as categorias\n"
                                  "Digite 4 para ver as categorias cadastradas\n"
                                  "Digite 5 para sair\n"))
                
                if decidir == 1:
                    categoria = input("Digite a categoria que dejesa cadastrar\n ")
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    categoria = input("Digite a categoria que dejesa remover\n ")
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input("Digite a categoria que dejesa alterar\n ")
                    novaCategoria = input("Digite a nova categoria\n ")
                    cat.alterarCategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break

        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                                  "Digite 2 para remover um produto\n"
                                  "Digite 3 para alterar os produtos\n"
                                  "Digite 4 para ver o estoque\n"
                                  "Digite 5 para sair\n"))
                
                if decidir == 1:
                    nomeProduto = input("Digite o nome do produto\n ")
                    categoria = input("Digite a categoria do produto\n ")
                    preco = float(input("Digite o preço do produto\n "))
                    quantidade = int(input("Digite a quantidade do produto\n "))
                    cat.cadastrarProduto(nomeProduto, categoria, preco, quantidade)
                elif decidir == 2:
                    nomeProduto = input("Digite o nome do produto que dejesa remover\n ")
                    cat.removerProduto(nomeProduto)
                elif decidir == 3:
                    nomeProduto = input("Digite o nome do produto que dejesa alterar\n ")
                    novaCategoria = input("Digite a nova categoria do produto\n ")
                    novoPreco = float(input("Digite o novo preço do produto\n "))
                    novaQuantidade = int(input("Digite a nova quantidade do produto\n "))
                    cat.alterarProduto(nomeProduto, novaCategoria, novoPreco, novaQuantidade)
                elif decidir == 4:
                    cat.mostrarEstoque()
                else:
                    break

        elif local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                  "Digite 2 para remover um fornecedor\n"
                                  "Digite 3 para alterar um fornecedor\n"
                                  "Digite 4 para ver os fornecedores\n"
                                  "Digite 5 para sair\n"))
                
                if decidir == 1:
                    nome = input("Digite o nome do fornecedor\n ")
                    cnpj = input("Digite o CNPJ do fornecedor\n ")
                    telefone = input("Digite o telefone do fornecedor\n ")
                    categoria = input("Digite a categoria do fornecedor\n ")
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    nome = input("Digite o nome do fornecedor que dejesa remover\n ")
                    cat.removerFornecedor(nome)
                elif decidir == 3:
                    nome = input("Digite o nome do fornecedor que dejesa alterar\n ")
                    novoNome = input("Digite o novo nome do fornecedor\n ")
                    novoCnpj = input("Digite o novo CNPJ do fornecedor\n ")
                    novoTelefone = input("Digite o novo telefone do fornecedor\n ")
                    novaCategoria = input("Digite a nova categoria do fornecedor\n ")
                    cat.alterarFornecedor(nome, novoNome, novoCnpj, novoTelefone, novaCategoria)
                elif decidir == 4:
                    cat.mostrarFornecedores()
                else:
                    break

        elif local == 4:
            cat = Controller.ControllerCliente()
            while True:
                decidir = int(input("Digite 1 para cadastrar um cliente\n"
                                  "Digite 2 para remover um cliente\n"
                                  "Digite 3 para alterar um cliente\n"
                                  "Digite 4 para ver os clientes\n"
                                  "Digite 5 para sair\n"))
                
                if decidir == 1:
                    nome = input("Digite o nome do cliente\n ")
                    telefone = input("Digite o telefone do cliente\n ")
                    cpf = input("Digite o CPF do cliente\n ")
                    email = input("Digite o email do cliente\n ")
                    endereco = input("Digite o endereço do cliente\n ")
                    cat.cadastrarCliente(nome, cpf, telefone, endereco)
                elif decidir == 2:
                    nome = input("Digite o nome do cliente que dejesa remover\n ")
                    cat.removerCliente(nome)
                elif decidir == 3:
                    nome = input("Digite o nome do cliente que dejesa alterar\n ")
                    novoNome = input("Digite o novo nome do cliente\n ")
                    novoTelefone = input("Digite o novo telefone do cliente\n ")
                    novoCpf = input("Digite o novo CPF do cliente\n ")
                    novoEmail = input("Digite o novo email do cliente\n ")
                    novoEndereco = input("Digite o novo endereço do cliente\n ")
                    cat.alterarCliente(nome, novoNome, novoCpf, novoTelefone, novoEndereco)
                elif decidir == 4:
                    cat.mostrarClientes()
                else:
                    break

        elif local == 5:
            cat = Controller.ControllerFuncionario()
            while True:
                decidir = int(input("Digite 1 para cadastrar um funcionario\n"
                                  "Digite 2 para remover um funcionario\n"
                                  "Digite 3 para alterar um funcionario\n"
                                  "Digite 4 para ver os funcionarios\n"
                                  "Digite 5 para sair\n"))
                
                if decidir == 1:
                    clt = input("Digite a clt do funcionario\n ")
                    nome = input("Digite o nome do funcionario\n ")
                    telefone = input("Digite o telefone do funcionario\n ")
                    cpf = input("Digite o CPF do funcionario\n ")
                    email = input("Digite o email do funcionario\n ")
                    endereco = input("Digite o endereço do funcionario\n ")
                    cat.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                elif decidir == 2:
                    clt = input("Digite a clt do funcionario que dejesa remover\n ")
                    cat.removerFuncionario(clt)
                elif decidir == 3:
                    nomeAlterar = input("Digite o nome do funcionario que dejesa alterar\n ")
                    novoClt = input("Digite a nova clt do funcionario\n ")
                    novoNome = input("Digite o novo nome do funcionario\n ")
                    novoTelefone = input("Digite o novo telefone do funcionario\n ")
                    novoCpf = input("Digite o novo CPF do funcionario\n ")
                    novoEmail = input("Digite o novo email do funcionario\n ")
                    novoEndereco = input("Digite o novo endereço do funcionario\n ")
                    cat.alterarFuncionario(nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cat.mostrarFuncionarios()
                else:
                    break

        elif local == 6:
            cat = Controller.ControllerVenda()
            while True:
                decidir = int(input("Digite 1 para realizar uma venda\n"
                                  "Digite 2 para ver as vendas\n"
                                  "Digite 3 para sair\n"))
                
                if decidir == 1:
                    nome = input("Digite o nome do produto\n ")
                    vendedor = input("Digite o nome do vendedor\n ")
                    comprador = input("Digite o nome do cliente\n ")
                    quantidade = int(input("Digite a quantidade do produto\n "))
                    cat.cadastrarVenda(nome, vendedor, comprador, quantidade)
                elif decidir == 2:
                    dataInicio = input("Digite a data de inicio (dd/mm/aaaa)\n ")
                    dataTermino = input("Digite a data de fim (dd/mm/aaaa)\n ")
                    cat.mostrarVenda(dataInicio, dataTermino)
                else:
                    break

        elif local == 7:
            a = Controller.ControllerVenda()
            a.relatorioProdutos()
        else:
            break