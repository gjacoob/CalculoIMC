Altura = float(input('Digite sua altura em CM: '))
Peso = float(input('Digite seu peso em KG: '))

IMC = Peso / (Altura/100)**2

print(IMC)

if IMC < 18.5:
    print('Seu IMC é de {:.2f} é classificado como Magreza'.format(IMC))

elif IMC >= 18.5 and IMC < 24.9:
    print('Seu IMC é de {:.2f} é classificado como Normal'.format(IMC))

elif IMC >= 25 and IMC < 29.9:
    print('Seu IMC é de {:.2f} é classificado como Sobrepeso I'.format(IMC))

elif IMC >= 30 and IMC < 39.9:
    print('Seu IMC é de {:.2f} é classificado como Obresidade II'.format(IMC))

elif IMC >= 40:
    print('Seu IMC é de {:.2f} é classificado como Obresidade III'.format(IMC))