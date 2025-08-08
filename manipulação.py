class Manipulação:
    def salvar(self, lista):
        with open("manipulação.txt", "w") as arquivos:
            for tarefa in lista:
                arquivos.write(tarefa + "\n")
        print("lista de tarefa salva com sucesso")


        