
tarefa=[]

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
        print("Inserir Tarefa!")
        item = input("Insira as tarefas: ")
        tarefa.append(item)
        


    elif lista == 2:
        print("Listando...")
        
        for item in tarefa:
            print(item)


        
    elif lista ==3:
        print("voce escolheu Marcar como Concluído!")

    
    elif lista == 4:
        print("voce escolheu Remover Tarefa!")
        pergunta = input("Qual item voce quer remover?")
        tarefa.remove(item)
    
    elif lista == 0:
        print("saindo...")
    
        break 
    
    

    





