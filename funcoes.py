from classe import Pessoa

listaPessoas = []

def instanciar(_nome: str, _idade: int, _trabalho: str):
    pessoa = Pessoa(len(listaPessoas)+1,_nome, _idade, _trabalho)
    listaPessoas.append(pessoa)

def editarPessoa(_nome: str, _idade: int, _trabalho: str):
    busca = int(input("Escreva o id da pessoa para editar: "))
    for i in listaPessoas:
        if i.id == busca:
            i.nome = _nome
            i.idade = _idade
            i.trabalho = _trabalho

def updateID():
    newID = 0
    for i in listaPessoas:
        i.id = newID + 1
        newID += 1

def excluirPessoa():
    busca = int(input("Escreva o id da pessoa para excluir: "))
    for i in listaPessoas:
        if i.id == busca:
            listaPessoas.pop(i.id-1)
    updateID()

def retornarLista():
    for i in listaPessoas:
        print("----------------")
        print("ID:", i.id)
        print("Nome:",i.nome)
        print("Idade:",i.idade)
        print("Trabalho:",i.trabalho)