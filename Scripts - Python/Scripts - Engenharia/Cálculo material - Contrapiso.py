print('-=' * 15)
print('Cálculo Materiais - Contrapiso')
print('-=' * 15)
rendimento = 0.2
área = float(input('Área (m²): '))
hc = float(input('Altura do Contrapiso (cm): '))
garagem = str(input('Será Garagem? [S/N] ')).upper().strip()[0]
if garagem in 'Ss':
    lata_areia = 7
    lata_brita = 7
if garagem in 'Nn':
    lata_areia = 9
    lata_brita = 6
'''carrinho = 3 * latas
fck = 10MPa'''
volume = área * (hc/100)
betonadas = volume / rendimento
volume_areia = lata_areia * betonadas * 0.018
volume_brita = lata_brita * betonadas * 0.018
lareia = volume_areia // 0.018
lbrita = volume_brita // 0.018
careia = lareia // 3
cbrita = lbrita // 3
print(f'Para executar esse Contrapiso de {volume}m³ e 10MPa\nSerão necessários os seguintes materiais em {betonadas:.0f} betonadas:')
print(f'{betonadas:.0f} Sacos de Cimento 50kg')
print(f'{volume_areia:.2f}m³ de Areia Média: {lareia:.0f} Latas 18l ou {careia:.0f} Carrinhos')
print(f'{volume_brita:.2f}m³ de Brita 0: {lbrita:.0f} Latas 18l ou {cbrita:.0f} Carrinhos')


