from .analisador_lexico.extrator_linhas import ExtratorLinhas
from .motor import Evento


class Compilador:
    def __init__(self):
        self.extrator = ExtratorLinhas()

    def compilar(self, nome_arquivo):
        self.extrator.add_evento(Evento('AbrirArquivo', nome_arquivo))
    