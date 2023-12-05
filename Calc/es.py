
# Função que lê números sem repetir a frase

def leitora_numeros()-> list: 
    """ Está função... """
    i = 0
    numeros = []
    while i < 2:
        numeros.append(float(input(f"digite o primeiro número {i+1} que deseja operar")))
        i+=1
    return numeros
    
leitora_numeros()


def leitora_operacao() -> str: 
    """Está função..."""
    operacao = input("""Digite a operação que deseja realizar.
Pressione + para adição;
- para subtração;
* para multiplicação;
/ para divisão""")
    return operacao


def leitora() -> list:
    """Está função"""
    lista_numeros = leitora_numeros()
    operacao = leitora_operacao()
    return [lista_numeros, operacao]
leitora()

def escritora(resultado):
    """ Esta função coloca o resultado na tela"""
    print(f"O resultado da operação é igual a (resultado).")
    
resultado = 9

escritora(resultado)

