'''
Faça um programa que leia uma frase pelo
teclado e mostre:
Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a ultima vez
'''

frase = str(input("Informe uma frase qualquer:")).upper().strip()
print("A letra A aparece {}vezes".format(frase.count('A')))
print("A letra A aparece na posição {}".format(frase.find('A')+1))
print("A letra A aparece na posição {}".format(frase.rfind('A')+1))
