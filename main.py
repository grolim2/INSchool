from functions.operations import soma,subtracao,exp,multi,divisao
from functions.input_user import operacao,valores

while True:
    operador = operacao()
    if operador.lower() == 'sair':
        print("Adeus.")
        break
    else:
        v1,v2 = valores()

        if operador == '+':
            print(f"\nResultado: {soma(v1, v2)}")
        elif operador == '-':
            print(f"\nResultado: {subtracao(v1, v2)}")
        elif operador == '/':
            print(f"\nResultado: {divisao(v1, v2)}")
        elif operador == '*':
            print(f"\nResultado: {multi(v1, v2)}")
        elif operador == '**':
            print(f"\nResultado: {exp(v1, v2)}")
