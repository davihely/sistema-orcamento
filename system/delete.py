def delete(id):
    with open(arquivo_nome, "r") as arquivo:
        data = json.load(arquivo)
                
    item = [element for element in data if element.get("id") != int(id)]

    if len(data) == len(item):
        print("usuario de id " + id + " não encontrado")
        return False    
    
    with open(arquivo_nome, "w") as arquivo:
            json.dump(item, arquivo, indent=4)
    
    print("usuario " + id + " excluido com sucesso")