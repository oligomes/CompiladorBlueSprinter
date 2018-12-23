import string
from ..motor import MotorEventos
from ..motor import Evento
from .filtro_ascii import Filtro

class ExtratorLinhas(MotorEventos):
    def __init__(self):
        super(ExtratorLinhas, self).__init__()
        self.linhas_indexadas = []
        self.filtro = Filtro()

    def trata_evento(self, evento):
        if evento.tipo == 'AbrirArquivo':
            self.abrir_arquivo(evento.informacao)
        elif evento.tipo == 'FecharArquivo':
            self.fechar_arquivo()
        elif evento.tipo == 'LeituraLinha':
            self.leitura_linha()

    def abrir_arquivo(self, nome_arquivo):
        self.arquivo_fonte = open(nome_arquivo)
        self.contador_linhas = 0
        self.add_evento(Evento('LeituraLinha'))

    def fechar_arquivo(self):
        self.arquivo_fonte.close()

    def leitura_linha(self):
        linha = self.arquivo_fonte.readline() + '\n'
        if linha != '':
            self.filtro.add_evento(Evento('ChegadaLinha', (linha, self.contador_linhas)))
            self.filtro.run()
            self.add_evento(Evento('LeituraLinha'))
        else:
            self.add_evento(Evento('FecharArquivo'))
