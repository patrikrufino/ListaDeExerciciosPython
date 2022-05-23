from Lib import Program_Name as lb


lb.program_name("PROGRAMA PARA TRANSFORMAR TEMPERATURA EM CELSIUS PARA FAHRENHEIT")

def transforma_celsius_para_fahrenheit(graus_em_celsius):
    return (graus_em_celsius * 9 / 5) + 32

input_graus = float(input("Digite o graus em Celsius:\n"))

print(f"{input_graus}Cº = {transforma_celsius_para_fahrenheit(input_graus)}Fº")