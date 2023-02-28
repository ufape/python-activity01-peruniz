# -*- coding: utf-8 -*-

# YOUR FULL NAME
# UAG00098
# Problem Set 1 - Problem 3
# Description:

"""
Inputs, Processes and Output (IPO)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Input(s):
Programa Simples de Pagamento

Informe quantas horas você trabalhou: 5

Processes:
Fornecida a quantidade de horas trabalhadas, calcule e forneça as informações conforme saída.

valor da hora trabalhada: 25
imposto: 0.125
salario bruto: valor da hora trabalhada * horas trabalhadas
impostos a cobrar: salario bruto * impostos a cobrar
salario liquido: salario bruto - impostos a cobrar

Output(s):
Programa Simples de Pagamento

Informe quantas horas você trabalhou: 5

Contracheque
        Horas trabalhadas: 5
        Valor da Hora: R$25.00
        Salário Bruto: R$125.00
        Imposto: R$15.62
        Salário Líquido: R$109.38 
"""


def main():
    print("Programa Simples de Pagamento\n")
    Horas = int(input("Informe quantas horas você trabalhou: "))
    HT = 25.00
    SB = Horas*HT
    IMP = 0.125
    IC = SB*IMP
    SL = SB-IC
    print("\nContracheque")
    print(f"\t\tHoras trabalhadas: {Horas:}")
    print(f"\t\tValor da Hora: R${HT:.2f}") 
    print(f"\t\tSalário Bruto: R${SB:.2f}")
    print(f"\t\tImposto: R${IC:.2f}")
    print(f"\t\tSalário Líquido: R${SL:.2f}")
      
      


if __name__ == '__main__':
    main()
