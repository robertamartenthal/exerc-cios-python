Nome_do_usuario = input('Qual seu primeiro nome?')
tamanho_nome = len(Nome_do_usuario)

if tamanho_nome >= 1  and tamanho_nome <= 4:
    print('Seu nome é curto') 
elif tamanho_nome >= 5 and tamanho_nome <= 6 :
    print('Seu nome é normal')
elif tamanho_nome >= 7 :
    print('Seu nome é muito grande')
else:
    print('Por favor digite um nome correto')