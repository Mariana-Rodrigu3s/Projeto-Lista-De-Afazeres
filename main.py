 
#listas 
tarefas=[]
confere=[]
pergunta=["[x]"]
while True:

#pra deixar bonito
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

    #lista né
    lista = int(input("Escolha por qual dos números você quer começar:"))



    #if para inserir tarefas 
    if lista == 1:
        print("---Inserir Tarefa!---")
        item = input("Insira as tarefas: ")
        tarefas.append(item)
        print(f"Tarefa '{item}' inserida com sucesso.")
    
    #if para listar as tarefas 
    elif lista == 2:
        print("---Listar Tarefa!---")
        print("Listando...")
        
        for item in tarefas:
            print(item)
        
        for item in confere:
            print(item)
    
    #if para marcar como concluido(deu errado o negocio do X rs)
    elif lista == 3:
        print("---Marcar como Concluído!---")
        conferir = input("Qual tarefa você concluiu?")
        confere.append(f"[x]{conferir}")
        print(f"Tarefa '{conferir}' concluída com sucesso.")

    #if para excluir as tarefas 
    elif lista == 4:
        print("---Excluir Tarefa!---")
        pergunta = input("Qual item você quer remover?")
        tarefas.remove(pergunta)
        print(f"Tarefa {pergunta} removida.")

    #if para sair 
    elif lista == 0:
        print("saindo...")
        #with open para colocar os itens na lista em um arquivo txt
        with open("main.txt", "w") as arquivos:
            for tarefa in tarefas:
                arquivos.write(tarefa +"\n")
        print("lista de tarefas salvas com sucesso")
            
        break 




    
    

   
    
    

    





