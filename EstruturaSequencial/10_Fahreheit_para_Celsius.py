from Lib import Program_Name as lb


lb.program_name("PROGRAMA PARA TRANSFORMAR TEMPERATURA EM FAHRENHEIT PARA CELSIUS")

def transforma_fahrenheit_para_celsius(g_fahreheit):
    return (g_fahreheit - 32 ) / 1.8

input_graus = float(input("Digite o graus em Fahreheit:\n"))

print(f"{input_graus}Fº = {transforma_fahrenheit_para_celsius(input_graus)}Cº")