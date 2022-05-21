from Lib import Program_Name as lb
from Lib import Conversores as conv

lb.program_name("CALCULADORA DE AREA DE CIRCULOS")

raio = int(input("Entre com o o valor do raio:\n"))

print(f"Um raio de {raio}cm, tem uma área de {conv.area_of_circle(raio)}cm²")