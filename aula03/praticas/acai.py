def recebe_acompanhamentos():
    print(':: RECEBENDO OS INGREDIENTES ::')
    acompanhamentos = []
    while(True):
        acompanhamento = input('Insira um ingrediente: ')
        if acompanhamento == '':
            break
        
        acompanhamentos.append(acompanhamento)
    
    return acompanhamentos

def pedido_acai(*ingredientes):
    print(':: PEDIDO DE AÇAÍ ::')
    print('Complementos:')
    for ingrediente in ingredientes:
        print(f'- {ingrediente}')
    
    print('🍌'*20)

lista_de_ingredientes = recebe_acompanhamentos()

pedido_acai(*lista_de_ingredientes)

'''pedido_acai()
pedido_acai('leite em pó')
pedido_acai('granola', 'leite em pó', 'M&M')
pedido_acai('granola', 'leite em pó', 'M&M', 'leite condensado', 'banana', 'paçoca')
'''