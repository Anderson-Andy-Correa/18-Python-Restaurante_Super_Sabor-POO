from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'


    @classmethod
    def listar_restaurantes(cls):
        titulo_listar = f'{"Nome do restaurante".ljust(25)} │ {"Categoria".ljust(25)} │ {"Avaliação".ljust(25)} | {"Status"}'
        print(titulo_listar)
        print('─'*len(titulo_listar))
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} │ {restaurante.categoria.ljust(25)} │ {str(restaurante.media_avaliacao).ljust(25)}| {restaurante.ativo}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'

    def alternar_estado(self):
        self._ativo = not self._ativo


    def receber_acaliacao(self, cliente, nota):
        if 0 <= nota <= 5: 
            self._avaliacao.append(Avaliacao(cliente, nota))

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-' # Sem Avaliação
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return round(soma_notas / len(self._avaliacao), 1)
