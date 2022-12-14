from time import sleep
n1 = int(input('Primeiro Valor: '))
sleep(0.5)
n2 = int(input('Segundo Valor: '))
sleep(0.5)
resp = 0
while resp != 5:
    print('''Menu de Opcões
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    resp = int(input('>>>>>> Qual é a sua opcão? '))
    print('=-='*15)
    if resp == 1:
        soma = n1 + n2
        print('A soma dos numeros é {}.'.format(soma))
        print('')
    elif resp == 2:
        multi = n1 * n2
        print('A multiplicacão dos números é {}'.format(multi))
        print('')
    elif resp == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O numero maior é {}'.format(maior))
        print('')
    elif resp == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
        print('')
    elif resp == 5:
        print('Finalizando.....')
    else:
        print('Opção inválida. Tente Novamente.')
        print('')
    sleep(2)
print('Fim do Programa.')
sleep(3)
