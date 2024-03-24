class Avaliacao:
    """Representa uma avaliação de um modelo"""
    def __init__(self, cliente, nota):
        """
        Inicializa uma intancia a avaliação
        
        Parâmetros:
        - cliente (str): Nome do cliente avaliador
        - nota (float): Nota atribuida pelo cliente"""
        self._cliente = cliente
        self._nota = nota
