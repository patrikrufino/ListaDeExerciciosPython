from Lib import Program_Name as lb

lb.program_name("PROGRAMA PESO IDEAL")

in_altura = float(input("Digite a sua altura em Metros:\n"))


def calcula_peso_ideal(h, sexo):
    if sexo == 1:
        return (72.7 * h) - 58
    else:
        return (62.1 * h ) - 44.7

print(f"Se você for homem, seu peso ideal é = {calcula_peso_ideal(in_altura, 1)}")
print(f"Se você for homem, seu peso ideal é = {calcula_peso_ideal(in_altura, 0)}")



