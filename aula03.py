palavra_secreta = 'Roberta'
letra_certa = ''
while True : 
    letra_digitada = input('Digite uma letra:')
    uma_letra = 1  
    if len(letra_digitada) > uma_letra :
        print('Digite apenas uma letra')
        continue
    if letra_digitada in palavra_secreta :
        letras_certas = letra_digitada
        palavra_formada = ''
    for letra_secreta in palavra_secreta : 
        if letra_secreta in letras_certas :
            palavra_formada = letra_secreta
        else :
         palavra_formada += '*'
       
    print(palavra_formada)

    # não está certo!