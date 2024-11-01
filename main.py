#cria uma calculadora:soma,sub de %,mult,div,potencia
#Menu
#Me perguntar a cada operaçao se desejo continuar ou nao 

print('##### CALCULADORA #####\n')

def Soma():
    print('Bem-vindo à opção de Soma!')
    num = float(input('Insira o 1º número da soma: '))
    num2 = float(input('Insira o 2º número da soma: '))
    result = num + num2
    print(f'O resultado da soma é {result}')

def Subtracao():
    print('Bem-vindo à opção de Subtração!')
    num = float(input('Insira o 1º número: '))
    num2 = float(input('Insira o 2º número: '))
    result = num - num2
    print(f'O resultado da subtração é {result}')

def Divisao():
    print('Bem-vindo à opção de Divisão!')
    num = float(input('Insira o 1º número: '))
    num2 = float(input('Insira o 2º número: '))
    result = num / num2
    print(f'O resultado da divisão é {result}')

def Multiplicacao():
    print('Bem-vindo à opção de Multiplicação!')
    num = float(input('Insira o 1º número: '))
    num2 = float(input('Insira o 2º número: '))
    result = num * num2
    print(f'O resultado da multiplicação é {result}')

def Potencia():
    print('Bem-vindo à opção de Potência!')
    num = float(input('Insira o 1º número: '))
    num2 = float(input('Insira o 2º número: '))
    result = num ** num2
    print(f'O resultado da potência é {result}')

def Porcentagem():
    print('Bem-vindo à opção de Porcentagem!')
    num = float(input('Insira o 1º número: '))
    num2 = float(input('Insira o 2º número: '))
    result = num * (num2 / 100)
    print(f'O resultado da porcentagem é {result}')

def menu():
    opcao = 0
    while opcao != 7:
        opcao = int(input('1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n5 - Potência\n6 - %\n7 - Sair\nSelecione o número: '))
        if opcao == 1:
            Soma()
        elif opcao == 2:
            Subtracao()
        elif opcao == 3:
            Divisao()
        elif opcao == 4:
            Multiplicacao()
        elif opcao == 5:
            Potencia()
        elif opcao == 6:
            Porcentagem()

menu()
print('##### CALCULADORA #####\n')

def Soma():
    print('Bem-vindo à opção de Soma!')
    num = float(input('Insira o 1º número da soma: '))
    num2 = float(input('Insira o 2º número da soma: '))
    result = num + num2
    print(f'O resultado da soma é {result}')

def Subtracao():
    print('Bem-vindo à opção de Subtração!')
    num = float(input('Insira o 1º número: '))
    num2 = float(input('Insira o 2º número: '))
    result = num - num2
    print(f'O resultado da subtração é {result}')

def Divisao():
    print('Bem-vindo à opção de Divisão!')
    num = float(input('Insira o 1º número: '))
    num2 = float(input('Insira o 2º número: '))
    result = num / num2
    print(f'O resultado da divisão é {result}')

def Multiplicacao():
    print('Bem-vindo à opção de Multiplicação!')
    num = float(input('Insira o 1º número: '))
    num2 = float(input('Insira o 2º número: '))
    result = num * num2
    print(f'O resultado da multiplicação é {result}')

def Potencia():
    print('Bem-vindo à opção de Potência!')
    num = float(input('Insira o 1º número: '))
    num2 = float(input('Insira o 2º número: '))
    result = num ** num2
    print(f'O resultado da potência é {result}')

def Porcentagem():
    print('Bem-vindo à opção de Porcentagem!')
    num = float(input('Insira o 1º número: '))
    num2 = float(input('Insira o 2º número: '))
    result = num * (num2 / 100)
    print(f'O resultado da porcentagem é {result}')

def menu():
    opcao = 0
    while opcao != 7:
        opcao = int(input('1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n5 - Potência\n6 - %\n7 - Sair\nSelecione o número: '))
        if opcao == 1:
            Soma()
        elif opcao == 2:
            Subtracao()
        elif opcao == 3:
            Divisao()
        elif opcao == 4:
            Multiplicacao()
        elif opcao == 5:
            Potencia()
        elif opcao == 6:
            Porcentagem()

menu()


    

  
  



