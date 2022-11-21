# Treinando função em Python 

while True:
    a = int(input('\nDigite um valor para A: '))
    b = int(input('Digite um valor para B: '))

    # Função para soma
    def soma(a,b):
        resultado = a + b
        return resultado

    # Função para soma  
    def subtracao(a,b):
        return a - b

    # Função para soma
    def divisao(a,b):
        return a / b

    # Função para soma    
    def multiplicacao(a,b):
        return a * b 

    print('\nA soma de A e B :' , soma(a,b))
    print('A subtração de A e B :' , subtracao(a,b))
    print('A divisão de A e B :' , divisao(a,b))
    print('A multiplicação de A e B :' , multiplicacao(a,b))