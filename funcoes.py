class Tarefa:
    def __init__(self):
        self.tarefa = []

    def adicionar(tarefa):
        item = input("Qual tarefa voce deseja incluir?")
        tarefa.append(item)
    

    def listar(self):
        cont = 0
        for tarefa in self.listar:
            print(f"{cont} - {tarefa}")
            cont += 1
    
    def excluir(self):
        self.listar()
        tarefaexcluir = int(input("Qual item deseja excluir?"))
        self.adicionar.pop(tarefaexcluir)



        

            