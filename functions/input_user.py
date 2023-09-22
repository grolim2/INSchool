def operacao():
    while True:
        op = input('\nDigite a operação que deseja realizar: \n'
                   '+ = SOMA\n'
                   '- = SUBTRAÇÃO\n'
                   '/ = DIVISÃO\n'
                   '* = MULTIPLICAÇÃO\n'
                   '** = EXPONENCIAÇÃO\n'
                   'Sair = Encerrar a aplicação\n'
                   '===== ')
        if op.lower() not in ['+', '-', '/', '*', '**', 'sair']:
            print('\n*****Digite uma operação válida.*****\n')
            continue
        else:
            return op.lower()

def valores():
    v1 = float(input('Digite o Valor 1: '))
    v2 = float(input('Digite o Valor 2: '))
    return v1,v2