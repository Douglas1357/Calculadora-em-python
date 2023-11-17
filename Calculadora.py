def somar (n1: float,n2: float) -> float:
    return n1 + n2
def subtrair (n1: float,n2: float) -> float:
    return n1 - n2
def dividir (n1: float,n2: float) -> float or str:
    if n2 == 0:
        return'não é possível dividir um numero por 0'
    return n1 / n2
def multiplicar (n1: float,n2: float) -> float:
    return n1 * n2

print('[1] - somar')
print('[2] - subtrair')
print('[3] - multiplicar')
print('[4] - dividir')
print('[5] - sair')
while True:
    operação = input('digite uma operação:')
if operação == '1':
    n1 = float(input('Digite o 1 numero:'))
    n2 = float(input('Digite o 1 numero:'))
    print(f'seu resultado é {n1 + n2}')
    pass
elif operação == '2':
    n1 = float(input('Digite o 1 numero:'))
    n2 = float(input('Digite o 1 numero:'))
    print(f'seu resultado é {n1 - n2}')
    pass
elif operação == '3':
    n1 = float(input('Digite o 1 numero:'))
    n2 = float(input('Digite o 1 numero:'))
    print(f'seu resultado é {n1 * n2}')
    pass
elif operação == '4':
    n1 = float(input('Digite o 1 numero:'))
    n2 = float(input('Digite o 1 numero:'))
    print(f'seu resultado é {n1 / n2}')
    pass
else:
    print('operação invalida')
