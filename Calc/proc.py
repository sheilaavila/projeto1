"""
Módulo Proc
Descrição: Este módulo provê funções de calculadora básica.
Autor: Eu
Versão: 0.0.1
Data:29/11/2023

"""



def somadora(numero1: float, numero2: float) -> float:
    """Esta função pega números reais e retorna a soam deles"""
    return numero1 + numero2

def diminuidora(numero1: float, numero2: float) -> float:
    """ Está função pega números reais e retorna a soma deles"""
    return numero1 - numero2


def multiplicadora(numero1: float, numero2: float) -> float:
    """ Está função pega números reais e retorna a soma deles"""
    return numero1 * numero2


def divisora(numero1: float, numero2: float) -> float:
    """ Está função pega números reais e retorna a soma deles"""
    if numero2 ==0:
        resultado = "não existe divisão por zero"
    else:
        resultado = numero1/numero2 
    return resultado
