from livro.livro_fisico import LivroFisico
from membro.membro import Membro

class Biblioteca:
    def __init__(self):
        self.__livro = []
        self.__membro = []

    def cadastrarMembro(self, membro: Membro):
        self.__membro.append(membro)
        print("Novo membro adicionado a biblioteca")

    def deletarMembro(self, membro_id):
        for membro in self.__membro:
            if membro.membro_id == membro_id:
                self.__membro.remove(membro)
                print("Membro deletado com sucesso")

    def cadastrarLivro(self,livro:LivroFisico):
        self.__livro.append(livro)
        print("Novo livro adicionado a biblioteca")

    def deletarLivro(self,id):
        for livro in self.__livro:
            if livro.livro_id == id:
                self.__livro.remove(livro)
                print("Livro deletado com Sucesso")

    def listarLivros(self):
        print("-----Livros Cadastrados-----\n")
        for livro in self.__livro:
            print("Dados do Livro:")
            print(f"Id:{livro.livro_id}")
            print(f"Título:{livro.titulo}")
            print(f"Autor:{livro.autor}")
            print(f"Ano:{livro.ano_publi}")
            print(f"Nº de Paginas:{livro.numero_paginas}\n")

    def listarMembros(self):
        print("----Membros Cadastrados----\n")
        for membro in self.__membro:
            print("------Dados do Membro----\n")
            print(f"Id:{membro.membro_id}")
            print(f"Nome:{membro.nome}")
            print(f"Endereço:{membro.endereco}")
            print(f"Telefone:{membro.telefone}\n")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    m1 = Membro(1, "Luis", "Rua A", "88 9999 7777")
    m2 = Membro(2, "Carmem", "Rua B","55 0909 8888")
    liv1 = LivroFisico(1,"Tolkien","LOR",1970,700)
    biblioteca.cadastrarMembro(m1)
    biblioteca.cadastrarMembro(m2)
    biblioteca.cadastrarLivro(liv1)
    biblioteca.listarMembros()
    biblioteca.listarLivros()