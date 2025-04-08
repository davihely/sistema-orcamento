import os, json
arquivo_nome = "nomes.json"

def insert_cli(values):
    with open(arquivo_nome, "r") as arquivo:
        if os.stat(arquivo_nome).st_size > 0:
            try:
                nomes = json.load(arquivo)
                if not isinstance(nomes, list):
                        nomes = []
            except json.JSONDecodeError:
                    nomes = []
        else:
            nomes = []
     
        if not nomes or os.stat(arquivo_nome).st_size <= 0:
            identificacao = 1
        else:
            identificacao = nomes[-1]['id'] + 1
            
        dicionario = dict(
            id = identificacao, 
            name = values[0], 
            cpf = values[1], 
            tel = values[2], 
            email = values[3], 
            adress = values[4], 
            city = values[5], 
            state = values[6], 
            client_type = values[7] 
        )

        nomes.append(dicionario)
        
        with open(arquivo_nome, "w") as arquivo:
            json.dump(nomes, arquivo, indent=4)
    
    
