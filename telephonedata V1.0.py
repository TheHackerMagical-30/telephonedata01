import openpyxl

# Função para criar uma planilha e inserir registros
def criar_planilha():
    # Cria um novo arquivo Excel (planilha)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Registros"  # Nome da planilha

    # Define os cabeçalhos
    sheet['A1'] = "ID"
    sheet['B1'] = "Nome"
    sheet['C1'] = "Idade"
    sheet['D1'] = "Email"

    # Pergunta ao usuário quantos registros ele quer adicionar
    n = int(input("Quantos registros você deseja inserir? "))

    # Adiciona os registros
    for i in range(n):
        print(f"Digite os dados para o registro {i+1}:")
        id_registro = input("ID: ")
        nome = input("Nome: ")
        idade = input("Idade: ")
        email = input("Email: ")

        # Adiciona o registro na planilha
        sheet.append([id_registro, nome, idade, email])

    # Salva o arquivo Excel
    wb.save("registros.xlsx")
    print("Planilha criada e salva como 'registros.xlsx'.")

# Chama a função para criar a planilha e inserir registros
criar_planilha()
