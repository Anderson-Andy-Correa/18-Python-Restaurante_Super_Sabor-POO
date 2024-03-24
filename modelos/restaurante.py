from modelos.avaliacao import Avaliacao

class Restaurante:
    """Representa um restaurante e suas características"""
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de restaurante
        
        Parâmetros:
        - nome (str): O nome do restaurante
        - categoria (str): A categoria do restaurante
        """
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Exibe uma respresentação em string do restaurante"""
        return f'{self.nome} | {self.categoria}'


    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de cada um dos restaurantes criados"""
        titulo_listar = f'{"Nome do restaurante".ljust(25)} │ {"Categoria".ljust(25)} │ {"Avaliação".ljust(25)} | {"Status"}'
        print(titulo_listar)
        print('─'*len(titulo_listar))
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} │ {restaurante.categoria.ljust(25)} │ {str(restaurante.media_avaliacao).ljust(25)}| {restaurante.ativo}')

    @property
    def ativo(self):
        """Retorna um simbolo demostrando o seu estado de atividade do restaurante"""
        return '✅' if self._ativo else '❎'

    def alternar_estado(self):
        """Altera o estado de atividade do restaurante selecionado"""
        self._ativo = not self._ativo


    def receber_acaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante
        
        Parâmetros:
        - cliente (str): Nome do cliente que avaliou
        - nota (float): Nota atribuída pelo cliente para o restaurante (pode ser entre 0 a 5)"""
        if 0 <= nota <= 5: 
            self._avaliacao.append(Avaliacao(cliente, nota))

    @property
    def media_avaliacao(self):
        """Calcula e retorna a média das avaliações do restaurante"""
        if not self._avaliacao:
            return '-' # Sem Avaliação
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return round(soma_notas / len(self._avaliacao), 1)
