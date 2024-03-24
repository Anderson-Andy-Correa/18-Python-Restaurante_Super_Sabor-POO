from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_acaliacao('Andy', 10)
restaurante_praca.receber_acaliacao('Igor', 8)
restaurante_praca.receber_acaliacao('Barbara', 5)
restaurante_praca.alternar_estado()
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
restaurante_japones = Restaurante('Japa', 'Japonesa')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
