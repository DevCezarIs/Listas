"""
6. Faça um programa que calcule o imposto de renda de um contribuinte de um país imaginário
onde as regras do imposto são as seguintes:
• Todos pagam a mesma alíquota, de 20%.
• São descontados da base de cálculo (proventos) as despesas com educação e despesas
médicas.
• São descontados R$ 1000,00 por dependente.
• O imposto devido ou a receber pode ser parcelado em até 6 vezes.
• Valores de imposto (devido ou a receber) abaixo de R$100,00 não são cobrados nem
pagos.

"""

def calcular_imposto(proventos, despesas_educacao, despesas_medicas, dependentes):

    # Alíquota do imposto
    aliquota = 0.20
    
    # Descontos
    desconto_dependentes = dependentes * 1000
    base_calculo = proventos - despesas_educacao - despesas_medicas - desconto_dependentes
    
    # Calcula o imposto bruto
    imposto_bruto = base_calculo * aliquota
    
    # Aplica a regra de valores mínimos
    if imposto_bruto < 100:
        return 0.0
    
    return imposto_bruto

def exibir_parcelas(imposto):
    """
    Exibe o valor do imposto parcelado em até 6 vezes.
    
    Parâmetros:
    imposto (float): Valor do imposto a ser parcelado.
    """
    if imposto == 0:
        print("\nO imposto é inferior a R$ 100,00 e não precisa ser pago.")
    else:
        parcelas = min(6, int(imposto / 100) + (imposto % 100 != 0))
        valor_parcela = imposto / parcelas
        
        print(f"\nImposto total: R$ {imposto:.2f}")
        print(f"Pode ser parcelado em {parcelas} vez(es) de R$ {valor_parcela:.2f}.")

def obter_entrada(mensagem, tipo):
    """
    Solicita e valida a entrada do usuário.
    
    Parâmetros:
    mensagem (str): Mensagem para exibir ao usuário.
    tipo (type): Tipo de dado esperado (int ou float).
    
    Retorna:
    tipo: Valor fornecido pelo usuário, convertido para o tipo especificado.
    """
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print(f"Entrada inválida. Por favor, insira um valor válido de tipo {tipo.__name__}.")

def main():
    print("=== Cálculo do Imposto de Renda ===")
    print("Este programa calcula o imposto de renda de acordo com as regras fornecidas.")
    
    # Solicita informações ao usuário com validação
    proventos = obter_entrada("Digite o valor dos proventos (R$): ", float)
    despesas_educacao = obter_entrada("Digite o valor das despesas com educação (R$): ", float)
    despesas_medicas = obter_entrada("Digite o valor das despesas médicas (R$): ", float)
    dependentes = obter_entrada("Digite o número de dependentes: ", int)
    
    # Calcula o imposto devido
    imposto = calcular_imposto(proventos, despesas_educacao, despesas_medicas, dependentes)
    
    # Exibe o resultado
    exibir_parcelas(imposto)

# Executa o programa
main()
