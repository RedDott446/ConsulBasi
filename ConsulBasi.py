import phonenumbers

nmr = input('Digite o número a ser consultado: ')
# ajuste do telefone
telefone = "+5522999937509"
telefone_ajustado = phonenumbers.parse(telefone)
print(telefone_ajustado)

# descobrir a loc do tel
from phonenumbers import geocoder
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print("Este número é do(a): " + local)

# descobrir operadora
from phonenumbers import carrier
operadora = carrier.name_for_number(telefone_ajustado, "pt-br")
print("Utilizando a operadora: " + operadora)
