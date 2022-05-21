from Lib import Program_Name as lb
from Lib import Conversores as conv

lb.program_name("CONVERSOR DE METROS PARA CENTIMETROS")

metros = int(input("Entre com um número em Metros para ser convertido em Centimetros:\n"))

print(f"{metros}m = {conv.metros_to_centimeters(metros)}cm")