 
lista = []


while True : 

    print('Selecione uma opção:')
    opção= input('[i]nserir [a]pagar [l]istar: ')

    if 'i' in opção:
        Valor= input('Valor:')
        lista.append(Valor)
    if Valor == '' : 
       print('Por favor digite um valor!')
       Valor = input('Valor:')
       lista.append(Valor)

    if 'a' in opção :
       indice_str= input('Qual indice você quer apagar?')
       try: 
          indice = int(indice_str)
          del lista[indice]
       except ValueError :
            print('Não foi possivel apagar esse indice!')
       except IndexError :
            print('Indice não existe nessa lista.')
       except Exception : 
            print('Erro desconhecido')

    if 'l' in opção :
      
      for i, Valor in enumerate(lista) :
        print(i,Valor)

    

    

       


