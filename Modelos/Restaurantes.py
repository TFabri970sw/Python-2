class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'


restaurante_noma = Restaurante()

restaurantes = [restaurante_praca, restaurante_noma]

#print(dir(restaurante_praca))
print(vars(restaurante_praca))