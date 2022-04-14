import os
import random
esporte = ['atletismo','automobilismo','basquete', 'beisebol', 'boliche', 'canoagem','crossfit', 'dama', 'fisiculturismo', 'futebol', 'futsal', 'golfe','handebol',
            'motociclismo','natação', 'skate', 'surfe', 'xoleibol', 'xadrez']
opcoes = ['argentina', 'angola', 'chile', 'china', 'congo', 'dinamarca', 'equador', 'espanha','frança', 'holanda', 'jamaica', 'portugal', 'venezuela' 'turquia']
animais = ['abelha','abutre','anaconda','baleia','besouro','borboleta','camarão','cascavel','crocodilo','dinossauro','elefante','esquilo','flamingo','formiga','gafanhoto','girafa',
            'guaxinim','hamster', 'hamster','iguana','javali','jiboia','lagarta', 'leopardo','macaco','mamute','minhoca','mosquito', 'ornitorrinco','papagaio','piranha','raposa','sardinha','serpente']
digitada = []
chances = 6
secreto = random.choice(esporte)
secreto_1 = random.choice(opcoes)
secreto_2 = random.choice(animais)


def linha (tam=42): #Linha
    return '-' * tam
print(linha())
print('Jogo da forca'.center(42))
print(linha())

menu = ['Jogar','Sair'] #Menu Central

a = 0
for item in menu:
    print(f'{a}-{item}')
    a += 1
print(linha())

validouDigito_1 = True

while validouDigito_1:

    val1 = input('Opção: ')
    print(linha())

    if not val1.isdigit():
        print(f'Letras não fazem parte das opções, tente novamente.')
    else:
        val1 = int(val1)

        if 0 == val1:  # Jogar
            validouDigito = False
            print('Selecione a opção desejada')

            menu_1 = [' Esporte', ' Pais', ' Animal', ' Sair']  # Caracteristicas do jogo

            b = 0
            for iten in menu_1:
                print(f'{b}-{iten}')
                b += 1

            validouDigito_1 = True

            while validouDigito_1:
                print(linha())
                val2 = input('Opção: ')

                print(linha())

                if not val2.isdigit():
                    print(f'Letras não fazem parte das opções, tente novamente.')
                else:
                    val2 = int(val2)
                    if 0 == val2: #Esporte
                        validouDigito_1 = False

                        while True:

                            if chances == 0:
                                print('Você perdeu!')
                                break

                            letra = input('Digite uma letra:')
                            letra = format(letra.lower())

                            if len(letra) > 1:
                                print('Digite apenas 1 letra')
                                continue

                            digitada.append((letra))

                            if letra in secreto:
                                print(f'O Esporte tem a letra {letra}')
                            else:
                                print(f'A letra {letra} não pertence ao esporte')
                                digitada.pop()

                            secreto_temporario = ''
                            for letra_secreta in secreto:
                                if letra_secreta in digitada:
                                    secreto_temporario += letra_secreta
                                else:
                                    secreto_temporario += '_'

                            if secreto_temporario == secreto:
                                print(f'Meus parabéns, você acertou! {secreto_temporario.capitalize()}')
                                break
                            else:
                                print(f'{secreto_temporario.center(21)}')

                            if letra not in secreto:
                                chances -= 1

                            print(f'Você ainda tem {chances} chances\n')
                            print(linha())
                    elif 1 == val2: #Pais
                        validouDigito_1 = False

                        while True:

                            if chances == 0:
                                print('Você perdeu!')
                                break

                            letra = input('Digite uma letra:')
                            # letra = format(letra.upper())

                            if len(letra) > 1:
                                print('Digite apenas 1 letra')
                                continue

                            digitada.append((letra))

                            if letra in secreto_1:
                                print(f'O Pais tem a letra {letra}')
                            else:
                                print(f'A letra {letra} não pertence ao Pais')
                                digitada.pop()

                            secreto_temporario = ''
                            for letra_secreta in secreto_1:
                                if letra_secreta in digitada:
                                    secreto_temporario += letra_secreta
                                else:
                                    secreto_temporario += '_'

                            if secreto_temporario == secreto_1:
                                print(
                                    f'Meus parabéns, você acertou {secreto_temporario.capitalize()}')
                                break
                            else:
                                print(f'{secreto_temporario.center(21)}')

                            if letra not in secreto_1:
                                chances -= 1

                            print(f'Você ainda tem {chances} chances \n')
                            print(linha())
                    elif 2 == val2: #Animais
                        validouDigito_1 = False

                        while True:

                            if chances == 0:
                                print('Você perdeu!')
                                break

                            letra = input('Digite uma letra:')
                            # letra = format(letra.upper())

                            if len(letra) > 1:
                                print('Digite apenas 1 letra')
                                continue

                            digitada.append((letra))

                            if letra in secreto_2:
                                print(f'O animal tem a letra {letra}')
                            else:
                                print(f'A letra {letra} não pertence ao animal')
                                digitada.pop()

                            secreto_temporario = ''
                            for letra_secreta in secreto_2:
                                if letra_secreta in digitada:
                                    secreto_temporario += letra_secreta
                                else:
                                    secreto_temporario += '_'

                            if secreto_temporario == secreto_2:
                                print(f'Meus parabéns, você acertou! {secreto_temporario.capitalize()}')
                                break
                            else:
                                print(f'{secreto_temporario.center(21)}')

                            if letra not in secreto_2:
                                chances -= 1

                            print(f'Você ainda tem {chances} chances \n')
                            print(linha())
                    elif 3 == val1:  # Sair
                        validouDigito = False
                        break
                    else:
                        print('Opção invalida, tente novamente')
                        continue
        elif 1 == val1:
            print('Volte sempre ao nosso jogo.')
            break
        else:
             print("Opção não existe, tentar novamente.")
