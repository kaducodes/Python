#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
c = float(input('Informe a temperatura em ºC: '))
f = float(1.8 * c + 32)
k = float(c + 273)
print(f'A temperatura de {c:.2f}ºC corresponde a:\n{f:.2f}ºF e\n{k:.2f}K')

