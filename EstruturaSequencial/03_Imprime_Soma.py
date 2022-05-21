from Lib import Program_Name as lb
lb.program_name("PROGRAMA PARA SOMAR DOIS NÚMEROS")

def soma(x, y):
    return x + y

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"A soma dos números é: {soma(a,b)}")
