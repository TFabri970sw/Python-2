from modelos.Restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Thiago', 3.5)
restaurante_praca.receber_avaliacao('Lucy', 5)
restaurante_praca.receber_avaliacao('Nyx', 2)

def main():
    Restaurante.lista_restaurantes()

if __name__ == '__main__':
    main()