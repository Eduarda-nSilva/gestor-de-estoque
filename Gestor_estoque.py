# GESTOR DE ESTOQUE
# Permite cadastrar produtos, consultar saldo e histórico, e registrar
# entradas e saídas de estoque, sempre com data e responsável.

from datetime import date, datetime #Biblioteca para manipular data e horário
estoque_atual = {} # Dicionário de dicionários: a chave é o nome do item e o valor guarda saldo e data. Exemplo: {'lampada': {'saldo': 10, 'data': '15/11/2026'}}
movimentacoes = [] # Lista de dicionários: cada movimentação (cadastro, entrada ou saída) é um registro. Obs: o campo 'saldo' guarda a QUANTIDADE movimentada, não o saldo do item.

def consulta(): # Mostra todos os itens do estoque com saldo e data. Não devolve nada, só imprime.
    for chave, valor in estoque_atual.items(): 
        print(f'Item: {chave} | Saldo: {valor["saldo"]}\nData de cadastro: {valor["data"]}')

def valida_data(data): # Recebe a data digitada (texto dd/mm/aaaa).
    data_atual = date.today() 
    try:
        data = datetime.strptime(data, '%d/%m/%Y') # strptime converte texto em data; levanta ValueError se o formato/data for inválido
        data_informada = data.date() 
        if data_informada > data_atual:
            print('A data de cadastro de um item não pode ser maior que a data atual') # Não faz sentido registrar a entrada de algo que ainda não aconteceu
            return False
        else:
            return True # Devolve True se o formato é válido e a data não é futura; caso contrário, False.
    except ValueError:
        print('Data inválida')
        return False

def historico(): # Mostra o histórico geral de movimentações, na ordem em que foram registradas
    if not movimentacoes:
        print('Nenhuma movimentação registrada')
    for valor in movimentacoes:
        print(f'Item: {valor["item"]} | Ação executada: {valor["tipo_acao"]} | Saldo: {valor["saldo"]} | Responsável: {valor["responsavel"]} | Data: {valor["data"]}')
   

# ======= PROGRAMA PRINCIPAL =======

responsavel = input('Digite seu nome de usuário: ').lower().strip() # O responsável é pedido uma única vez, antes do menu, e vale para todas as movimentações da sessão

while True: # Loop principal: mostra o menu até o usuário escolher 'e' (sair).
    print("=== Gestor de Estoque ===")
    print('       MENU       ')
    print(' a) Cadastrar produto \n b) Consultar estoque \n c) Informar entrada no estoque \n d) Informar baixa no estoque \n e) Sair')
    opcao_selecionada = input('Escolha uma opção acima: ').lower().strip()
    opcoes_validas = ['a', 'b', 'c', 'd', 'e'] # Lista usada no final do loop para detectar opção inexistente

# ---------- a) Cadastrar produto ----------
    if opcao_selecionada == 'a':
        while True: # Loop externo: repete enquanto o usuário quiser cadastrar outro item
            while True: # Repete até o nome ser válido: não vazio e ainda não cadastrado
                item = input('Digite o nome do item: ').lower().strip()
                if item == '':
                    print('Para continuar digite o nome do item')
                elif item in estoque_atual: # Impede sobrescrever um item que já existe
                    print('Cadastro duplicado. O item infomado ja esta cadastrado no estoque')
                else:
                    break

            while True: # Repete até a data ser válida (formato correto e não futura)
                data_entrada = input('Digite a data de entrada: ')
                validacao = valida_data(data_entrada)
                if validacao != False:
                    break

            while True: # Repete até o saldo ser um número inteiro maior que zero.
                saldo_cadastro = input('Digite o saldo inicial do item: ').strip()
                if saldo_cadastro == '':
                    print('O saldo não pode ficar vazio')
                else:
                    try:
                        saldo_cadastro = int(saldo_cadastro) # ValueError se não for número
                        if saldo_cadastro > 0: # Grava o item: o valor é um dicionário com saldo e data
                            estoque_atual[item] = {'saldo':saldo_cadastro, 'data':data_entrada} # O item só é gravado depois que nome, data e saldo estão validados.
                            break
                        else:
                            print('O saldo inicial deve ser maior que zero')
                            continue
                    except ValueError: 
                        print('Digite somente números')

            decisao = input('Deseja cadastrar um novo item? ').lower().strip()
            consulta() # Mostra o estoque atualizado
            movimentacoes.append({"item":item,"tipo_acao": "entrada", "saldo":saldo_cadastro,"responsavel":responsavel, "data": data_entrada}) # Registra o cadastro no histórico como uma entrada, com o responsável da sessão

            if decisao == 's' or decisao == 'sim':
                continue # Volta ao topo do loop externo para cadastrar outro item
            else:
                break # Sai do cadastro e volta ao menu principal
            
# ---------- b) Consultar estoque ----------
    elif opcao_selecionada == 'b':
        while True: # Submenu: repete até o usuário digitar 4 (voltar ao menu principal)
            print('1 - Consultar saldo geral \n2 - Consultar saldo de um item \n3- Consultar historico de movimentações \n4- Menu')
            opcao_consulta = input('Digite qual consulta que deseja realizar: ')
            
            if opcao_consulta == '1': # Saldo de todos os itens
                if not estoque_atual:
                    print('Estoque vazio. Digite 4 para voltar ao menu anterior e cadastre ao menos um item')
                else:
                    print('=== ESTOQUE ATUAL ===')
                    consulta()
            
            elif opcao_consulta == '2': # Saldo de um item específico
                item_consulta = input('Digite o item que deseja consultar: ').lower().strip()

                if item_consulta in estoque_atual: # Busca o dicionário do item e pega os campos pelo nome
                    print(f'{item_consulta} | Saldo atual: {estoque_atual[item_consulta]["saldo"]} | Data de cadastro: {estoque_atual[item_consulta]["data"]}')
                else:
                    print(f'{item_consulta} não encontrado. Não foi possível localizar o cadastro do item informado.')
                
            elif opcao_consulta == '3': # Histórico de movimentações (de um item ou geral)    
                print('1) Consultar histórico de um item \n2) Consultar historico geral \n3) Sair')
                tipo_historico = input('Digite o tipo de histórico que deseja consultar: ')

                if tipo_historico == '1': # Histórico de um item: percorre a lista e mostra só os registros dele
                   item_historico = input('Digite o item que deseja consultar o histórico: ').lower().strip()
                   encontrou = False # 'encontrou' começa False e vira True se algum registro for do item.
                   for registro in movimentacoes:
                       if registro["item"] == item_historico: # 'registro' é o dicionário da volta atual
                        print(f'{item_historico} | Ação executada: {registro["tipo_acao"]} | Saldo:{registro["saldo"]} | Responsável:{registro["responsavel"]} | Data:{registro["data"]}')
                        encontrou = True
                   if not encontrou:
                    print(f'{item_historico} não possui histórico de movimentações')  
                elif tipo_historico == '2': # Histórico geral: usa a função historico()
                    historico()
                elif tipo_historico == '3': # Sai do submenu e volta ao menu principal
                    break
                else:
                    print('Digite 1, 2 ou 3')

            elif opcao_consulta == '4': # Sai do submenu e volta ao menu principal
                break
            else: # Opção inexistente: avisa e o loop repete o submenu
                print('Digite somente 1, 2, 3 ou 4')
            
# ---------- c) Entrada no estoque ----------                            
    elif opcao_selecionada == 'c':
        while True: # Loop do item: repete enquanto o item informado não existir
            item_entrada = input('Informe qual o item: ').lower().strip()            
            if item_entrada in estoque_atual:

                while True: # Repete até a quantidade ser um inteiro maior que zero
                    saldo_adicionado = input('Informe o saldo que será adicionado no estoque: ')
                    try:
                        saldo_adicionado = int(saldo_adicionado) # ValueError se não for número
                        if saldo_adicionado > 0: 
                            estoque_atual[item_entrada]["saldo"] += saldo_adicionado # Atualiza o saldo automaticamente 
                            print(f'Item: {item_entrada} | Saldo: {estoque_atual[item_entrada]["saldo"]} | Data de cadastro: {estoque_atual[item_entrada]["data"]}')
                            data_atual = date.today().strftime('%d/%m/%Y') # A data da movimentação é a de hoje, gerada pelo sistema (evita data digitada errada)
                            movimentacoes.append({"item":item_entrada, "tipo_acao": "saldo adicionado", "saldo":saldo_adicionado, "responsavel":responsavel, "data": data_atual})
                            break
                        else:
                            print('Digite um número maior que zero')        
                    except ValueError:
                        print('Digite apenas números') # Sai do loop do item e volta ao menu principal
                break                    
            else: # Item inexistente: avisa e o loop pergunta o item de novo
                print(f'{item_entrada} não encontrado. Não foi possível localizar o cadastro do item informado.')

        
# ---------- d) Saída (baixa) do estoque ----------
    elif opcao_selecionada == 'd':
        while True: # Loop do item: repete enquanto o item informado não existir
            item_saida = input('Informe qual o item: ').lower().strip()
            if item_saida in estoque_atual: # Loop da quantidade: repete até a retirada ser válida
                while True:
                    saldo_removido = input('Informe o saldo que será retirado do estoque: ')
                    try:
                        saldo_removido = int(saldo_removido) # ValueError se não for número
                        if saldo_removido > 0: # Valida se há quantidade suficiente ANTES de alterar o estoque.
                            if (estoque_atual[item_saida]["saldo"] < saldo_removido):
                                print('A quantidade retirada não pode ser maior que o saldo disponível') # Bloqueia só quando a retirada é maior que o saldo; retirar tudo é permitido.
                            else:
                                estoque_atual[item_saida]["saldo"] -= saldo_removido
                                data_atual = date.today().strftime('%d/%m/%Y') # Data automática, como na entrada
                                print(f'Item: {item_saida} | Saldo: {estoque_atual[item_saida]["saldo"]} | Data de cadastro: {estoque_atual[item_saida]["data"]}') # Registra a saída no histórico, com responsável e data
                                movimentacoes.append({"item": item_saida, "tipo_acao": "saldo retirado", "saldo":saldo_removido, "responsavel":responsavel, "data": data_atual})
                                break # Sai do loop da quantidade
                        else:
                            print('informe um número maior que zero')
                    except ValueError:
                            print('Digite apenas números') 
                break # Sai do loop do item e volta ao menu principal
            else:
                print(f'{item_saida} não encontrado. Não foi possível localizar o cadastro do item informado.') # Item inexistente: avisa e o loop pergunta o item de novo
            


# ---------- Opção inválida / e) Sair ----------
    if opcao_selecionada not in opcoes_validas: 
        print('Digite apenas uma das opções informadas') # Letra fora de a-e: avisa e o menu reaparece na próxima volta
    elif opcao_selecionada == 'e':
        print('Obrigado por utilizar o gestor de estoque!')
        break # Encerra o loop principal e o programa