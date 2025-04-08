def update(id):
    with open(arquivo_nome, "r") as arquivo:
        data = json.load(arquivo)
                
    item = [element for element in data if element.get("id") == int(id)]
    campos = ['id: ','Nome: ','Cpf: ','Endereço: ','Telefone: ','Email: ','Preferencia de contato: ']
    i = 0;     

    with open(arquivo_nome, "r") as arquivo:
        data2 = json.load(arquivo)
        for dado in data2:
            if dado['id'] == int(id):
                for json_cada in item[0]:
                    valor = input("Digite o " + campos[i])
                    dado[json_cada] = valor
                    i += 1
    
    with open(arquivo_nome, "w", encoding="utf-8") as arquivo:
            json.dump(data2, arquivo, indent=4, ensure_ascii=False)