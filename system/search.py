def search(id):
    with open(arquivo_nome, "r") as arquivo:
        data = json.load(arquivo)
                
    item = [element for element in data if element.get("id") == int(id)]
    
    print("Id: " + str(item[0]['id']))
    print("Nome: " + item[0]['name'])
    print("Cpf: " + item[0]['cpf'])
    print("Endereço: " + item[0]['adress'])
    print("Telefone: " + item[0]['tel'])
    print("Email: " + item[0]['email'])
    print("Preferencia de contato: " + item[0]['contact_pref'])
    
    action = input("digite deletar para deletar cliente e alterar para alterar cliente: ")
    
    if action == "deletar":
        delete(id)
    elif action == "alterar":
        update(id)
    else:
        print("comando invalido")
    