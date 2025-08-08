from manipulação import Manipulação
tarefa=[]
confere=[]
Manipulação = Manipulação
while True:
    print("""   
                                                                        
    __    _     _            _        _____ ___                         
    |  |  |_|___| |_ ___    _| |___   |  _  |  _|___ ___ ___ ___ ___ ___ 
    |  |__| |_ -|  _| .'|  | . | -_|  |     |  _| .'|- _| -_|  _| -_|_ -|
    |_____|_|___|_| |__,|  |___|___|  |__|__|_| |__,|___|___|_| |___|___|
                                                                        
    """)

    print("""  
        | 1 - Inserir Tarefa
        | 2 - Listar Tarefas
        | 3 - Marcar como concluido
        | 4 - Remover Tarefa
        | 0 - Sair""")


    lista = int(input("Escolha por qual dos números você quer começar:"))




    if lista == 1:
        print("---Inserir Tarefa!---")
        item = input("Insira as tarefas: ")
        tarefa.append(item)
        print(f"Tarefa '{item}' inserida com sucesso.")
        
    elif lista == 2:
        print("---Listar Tarefa!---")
        print("Listando...")
        
        for item in tarefa:
            print(item)
        
        for item in confere:
            print(item)
    
    elif lista == 3:
        print("---Marcar como Concluído!---")
        conferir = input("Qual tarefa você concluiu?")
        confere.append(f"[x]{conferir}")
        print(f"Tarefa '{conferir}' concluída com sucesso.")

    
    elif lista == 4:
        print("---Excluir Tarefa!---")
        pergunta = input("Qual item você quer remover?")
        tarefa.remove(pergunta)
        print(f"Tarefa {pergunta} removida.")
    
    elif lista == 0:
        print("saindo...")
        
    
        break




    
    

   
    
    

    





