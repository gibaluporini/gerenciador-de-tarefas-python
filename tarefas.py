import json
import os

# Caminho do arquivo onde as tarefas serão salvas
caminho_arquivo = "tarefas.json"

# Carrega tarefas do arquivo, se ele existir
if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        tarefas = json.load(arquivo)
else:
    tarefas = []

# Função para salvar a lista de tarefas no arquivo
def salvar_tarefas():
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

# Início do menu
while True:
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("[1] Adicionar tarefa")
    print("[2] Listar tarefas")
    print("[3] Marcar como concluída")
    print("[4] Remover tarefa")
    print("[5] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título da tarefa: ")
        descricao = input("Descrição: ")
        
        nova_tarefa = {
            "titulo": titulo,
            "descricao": descricao,
            "status": "pendente"
        }

        tarefas.append(nova_tarefa)
        salvar_tarefas()
        print("✅ Tarefa adicionada com sucesso!")

    elif opcao == "2":
        print("\n=== GERENCIADOR DE TAREFAS ===")
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada ainda! ")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"\nTarefa {i}")
                print(f"Título: {tarefa['titulo']}")
                print(f"Descrição: {tarefa['descricao']}")
                print(f"Status: {tarefa['status']}")
                print("-" * 30)


    elif opcao == "3":       
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada para concluir.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa['titulo']} [{tarefa['status']}]")

            try:
                escolha = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
                if 1 <= escolha <= len(tarefas):
                    tarefas[escolha - 1]["status"] = "concluída"
                    salvar_tarefas()
                    print("✅ Tarefa marcada como concluída!")
                else:
                    print("❌ Número inválido.")
            except ValueError:
                print("❌ Por favor, digite um número válido.")

    elif opcao == "4":
        if len(tarefas) == 0:
            print("Nenhuma tarefa para remover.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa['titulo']} [{tarefa['status']}]")

            try:
                escolha = int(input("Digite o número da tarefa que deseja remover: "))
                if 1 <= escolha <= len(tarefas):
                    tarefa_removida = tarefas.pop(escolha - 1)
                    salvar_tarefas()
                    print(f"🗑️ Tarefa '{tarefa_removida['titulo']}' removida com sucesso!")
                else:
                    print("❌ Número inválido.")
            except ValueError:
                print("❌ Por favor, digite um número válido.") 

    elif opcao == "5":
        print("Saindo... até logo!")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
