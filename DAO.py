from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Vendas):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendidos.nome + "|" + venda.itensVendidos.preco + "|" 
                           + venda.itensVendidos.categoria + "|" + venda.vendedor + "|" + venda.comprador + "|" 
                           + str(venda.quantidadeVendida) + "|" + venda.data)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
        
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        vend = []
        for i in cls.venda:
            vend.append(Vendas(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))

        return vend
    
class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|" + produto.preco + "|" + 
                           produto.categoria + "|" + str(quantidade))
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
        
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2], i[3])))
        
        return est
    
class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.telefone
                           + "|" + fornecedor.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()
        
        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))
        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        
        return forn

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoa.nome + "|" + pessoa.cpf + "|" + pessoa.telefone 
                           + "|" + pessoa.email + "|" + pessoa.endereco)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('clientes.txt', 'r') as arq:
            cls.clientes = arq.readlines()
        
        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        clientes = []
        for i in cls.clientes:
            clientes.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))
        
        return clientes

class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionario.clt + "|" + funcionario.nome + "|" + funcionario.cpf + "|" + funcionario.telefone 
                           + "|" + funcionario.email + "|" + funcionario.endereco + "|" + funcionario.cargo + "|" + funcionario.salario)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()
        
        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        funcionario = []
        for i in cls.funcionarios:
            funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        
        return funcionario