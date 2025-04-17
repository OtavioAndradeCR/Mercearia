from Models import Categoria, Estoque, Produtos, Fornecedor, Pessoa, Funcionario, Vendas
from DAO import DaoCategoria, DaoEstoque, DaoFornecedor, DaoVenda, DaoPessoa, DaoFuncionario
from datetime import datetime

class ControllerCategoria:

    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print(f'Categoria {novaCategoria} cadastrada com sucesso!')
        else:
            print(f'Categoria {novaCategoria} já existe!')
    
    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print(f'Categoria {categoriaRemover} não encontrada!')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print(f'Categoria {categoriaRemover} removida com sucesso!')
        
        with open('categorias.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

        estoque = DaoEstoque.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, "Sem categoria"), x.quantidade) 
                           if(x.produto.categoria == categoriaRemover) else(x), estoque))
        
        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + 
                               i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
    
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print(f'Categoria {categoriaAlterar} alterada para {categoriaAlterada} com sucesso!')
            else:
                print(f'Categoria {categoriaAlterada} já existe!')

        else:
            print(f'Categoria {categoriaAlterar} não encontrada!')
        
        estoque = DaoEstoque.ler()

        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade) 
                           if(x.produto.categoria == categoriaAlterar) else(x), estoque))       
        
        with open('categorias.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))
        
        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print(f'Produto {nome} cadastrado com sucesso!')
            else:
                print(f'Produto {nome} já existe!')
        else:
            print(f'Categoria {categoria} não existe!')

    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print(f'Produto {nome} removido com sucesso!')
        else:
            print(f'Produto {nome} não encontrado!')
        
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + 
                               i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))

        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est1 = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est1) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) if(x.produto.nome == nomeAlterar) else(x), x))
                    print(f'Produto {nomeAlterar} alterado para {novoNome} com sucesso!')
                else:
                    print(f'Produto {novoNome} já existe!')
            else:
                print(f'Produto {nomeAlterar} não encontrado!')

            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + 
                                   i.produto.categoria + "|" + str(i.quantidade))
                    arq.writelines('\n')
        else:
            print(f'Categoria {novaCategoria} não existe!')

    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            print("==========Produtos==========")
            for i in estoque:
                print(f"Nome: {i.produto.nome}\n"
                      f"Preço: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}\n")
                print("----------------------------")

class ControllerVenda:

    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Vendas(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)

                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)

            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))

        arq = open('estoque.txt', 'w')
        arq.write("")

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                    arq.writelines('\n')
        
        if existe == False:
            print(f'Produto {nomeProduto} não encontrado!')
            return None
        elif not quantidade:
            print(f'Quantidade {quantidadeVendida} vendida não contem em estoque')
            return None
        else:
            print(f'Produto {nomeProduto} vendido com sucesso!')
            return valorCompra
            
    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.produto.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) >0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)} 
                if(x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
            
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print("==========Produtos mais vendidos==========")
        a = 1
        for i in ordenado:
            print(f"==========Produto {a}==========")
            print(f"Produto: {i['produto']}\n"
                    f"Quantidade: {i['quantidade']}\n")
            a += 1

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, "%d/%m/%Y")
        dataTermino1 = datetime.strptime(dataTermino, "%d/%m/%Y")

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, "%d/%m/%Y") >= dataInicio1
                                         and datetime.strptime(x.data, "%d/%m/%Y") <= dataTermino1, vendas))
        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(f"==========Venda [{cont}]==========")
            print(f"Nome: {i.itensVendido.nome}\n"
                  f"Categoria: {i.itensVendido.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade: {i.quantidadeVendida}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}\n")
            total += int(i.itensVendido.preco) * int(i.quantidadeVendida)
            cont += 1

        print(f"Total de vendas: {total}")

class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))   
        if len(listaCnpj) >0:
            print(f'Fornecedor {nome} já existe!')
        else:
            if len(cnpj) == 14 and len(telefone) <=11 and len(telefone) >=10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print("Digite um cnpj ou telefone valido")
    
    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj , x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if(x.nome == nomeAlterar) else(x), x))
                print(f'Fornecedor {nomeAlterar} alterado para {novoNome} com sucesso!')
            else:
                print(f'Fornecedor {novoNome} já existe!')
        else:
            print(f'Fornecedor {nomeAlterar} não encontrado!')
        
        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + i.categoria)
                arq.writelines('\n')
            print(f'Fornecedor alterado com sucesso!')

    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break

        else:
            print(f'Fornecedor {nome} não encontrado!')
            return None
        
        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + i.categoria)
                arq.writelines('\n')
            print(f'Fornecedor {nome} removido com sucesso!')
    
    def mostrarFornecedores(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print('Lista de fornecedores vazia')

        for i in fornecedores:
            print("==========Fornecedores==========")
            print(f"Categoria fornecida: {i.categoria}\n"
                  f"Nome: {i.nome}\n"
                  f"CNPJ: {i.cnpj}\n"
                  f"Telefone: {i.telefone}\n")

class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) >0:
            print(f'Cliente {nome} já existe!')
        else:
            if len(cpf) == 11 and len(telefone) >=10 and len(telefone) <=11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print(f'Cliente {nome} cadastrado com sucesso!')
            else:
                print("Digite um cpf ou telefone valido")

    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.nome == nomeAlterar) else(x), x))
        else:
            print(f'Cliente {nomeAlterar} não encontrado!')
        
        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print(f'Cliente alterado com sucesso!')
    
    def removerCliente(self, nome):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print(f'Cliente {nome} não encontrado!')
            return None
        
        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print(f'Cliente removido com sucesso!')
    
    def mostrarClientes(self):
        clientes = DaoPessoa.ler()

        if len(clientes) == 0:
            print('Lista de clientes vazia')

        for i in clientes:
            print("==========Clientes==========")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"CPF: {i.cpf}\n"
                  f"E-mail: {i.email}\n"
                  f"Endereço: {i.endereco}\n")
            
class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))
        if len(listaCpf) >0:
            print(f'Funcionario {nome} já existe!')
        elif len(listaClt) >0:
            print(f'Funcionario {clt} já existe!')
        else:
            if len(cpf) == 11 and len(telefone) >=10 and len(telefone) <=11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print(f'Funcionario {nome} cadastrado com sucesso!')
            else:
                print("Digite um cpf ou telefone valido")
    
    def alterarFuncionario(self, nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.nome == nomeAlterar) else(x), x))
        else:
            print(f'Funcionario não existe!')

        
        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print(f'Funcionario alterado com sucesso!')
    
    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print(f'Funcionario não existe')
            return None
        
        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print(f'Funcionario removido com sucesso!')
    
    def mostrarFuncionarios(self):
        funcionarios = DaoFuncionario.ler()

        if len(funcionarios) == 0:
            print('Lista de funcionarios vazia')

        for i in funcionarios:
            print("==========Funcionarios==========")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"CPF: {i.cpf}\n"
                  f"CLT: {i.clt}\n"
                  f"E-mail: {i.email}\n"
                  f"Endereço: {i.endereco}\n")