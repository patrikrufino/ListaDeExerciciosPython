from Lib import Program_Name as lb


lb.program_name("PROGRAMA PARA CALCULAR O SALARIO PELAS HORAS TRABALHADAS")

salario_por_hora = float(input("Digite quanto você ganha por hora:\n"))
horas_trabalhadas = float(input("Digite quantas horas você trabalhou:\n"))

salario_por_horas_trabalhadas = salario_por_hora * horas_trabalhadas

print(f"Seu salário vai ser de R${salario_por_horas_trabalhadas}")