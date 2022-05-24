from Lib import Program_Name as lb


lb.program_name("PROGRAMA PARA DAR SOMAS ALEATÓRIAS")

numero_inteiro_1 = int(input("Digite um número inteiro:\n"))
numero_inteiro_2 = int(input("Digite um segundo número inteiro:\n"))
numero_real = float(input("Digite um número real:\n"))

# A => O PRODUTO DO DOBRO DO PRIMEIRO COM A METADE DO SEGUNDO
questao_a = (numero_inteiro_1 * 2) + (numero_inteiro_2 / 2)

# B => A SOMA DO TRIPLO DO PRIMEIRO COM O TERCEIRO
questao_b = (numero_inteiro_1 * 3 ) + numero_real


# C => O TERCEIRO ELEVADO AO CUBO
questao_c = numero_real ** 3

print(f"Questão A:\nResposta:{questao_a}")
print(f"Questão B:\nResposta:{questao_b}")
print(f"Questão C:\nResposta:{questao_c}")