# Importação dos módulos

import test_es
import test_proc


#Definição das Funções

def escolhedora(dados: list) -> float:
    """esta função escolhe a operação adequada de acordo com o usuário"""
    if dados[1] == "+":
        resultado = test_proc.somadora(dados[0][0], dados[0][1])
    elif dados[1] == "-":
        resultado = test_proc.diminuidora(dados[0][0], dados[0][1])
    elif dados[1] == "*":
        resultado = test_proc.multiplicadora(dados[0][0], dados[0][1])
    elif dados[1] == "/":
        resultado = test_proc.divisora(dados[0][0], dados[0][1])
    else:
        resultado = test_proc.divisora(dados[0][0], dados[0][1])
    return resultado


def main():
    dados = es.leitora()
    resultado = escolhedora(dados)
    es.escritora(resultado)
    
# Execução

if__name__== "__main__":
    main()
    
