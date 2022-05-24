from Lib import Program_Name as lb

lb.program_name("PROGRAMA PESO IDEAL")


def calcula_peso_ideal(altura):
    (72.7 * altura) - 58


in_altura = float(input("Digite a sua altura em Metros:\n"))

print(f"Seu peso ideal é: {calcula_peso_ideal(in_altura)}")
