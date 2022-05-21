from Lib import Program_Name as lb


lb.program_name("PROGRAMA PARA VER A MEDIA DE NOTAS")

nota_1 = int(input("Entre com a nota número 1:"))
nota_2 = int(input("Entre com a nota número 2:"))
nota_3 = int(input("Entre com a nota número 3:"))
nota_4 = int(input("Entre com a nota número 4:"))

def media_notas(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4


print(f"A média das notas é = {media_notas(nota_1, nota_2, nota_3, nota_4)}")