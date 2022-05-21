from Lib import Program_Name as lb
from Lib import Conversores as conv

lb.program_name("O DOBRO DA ÁREA DO QUADRADO")

lado = int(input("Entre com o tamanho de um dos lados do quadrado em cm: \n"))

print(f"O quadrado possui uma área de {conv.area_of_square(lado)}cm².\n")

print(f"O dobro desta área é: {conv.area_of_square(lado) * 2 }cm²")
