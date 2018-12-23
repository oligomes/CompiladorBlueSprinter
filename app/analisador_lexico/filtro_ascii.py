import os
import string
import app.automatos.loaders as loaders
from ..motor import MotorEventos
from ..motor import Evento
from .tokenizador import AnalisadorLexico
from ..conf import ROOT_DIR

class Filtro(MotorEventos):
    def __init__(self):
        super(Filtro, self).__init__()
        self.categorias = { 'controle':['\n'],
                            'delimitador':['\t', ' '],
                            'letra':string.ascii_uppercase[:] + string.ascii_lowercase[:],
                            'digito':string.digits[:] }
        self.categorias.update({s:s for s in string.punctuation})
        self.caracteres_classificados = []
        self.automato_tokenizador = loaders.transdutor_finito(os.path.join(ROOT_DIR, 'automatos', 'tokenizer.af'))
        self.tokenizer = AnalisadorLexico(self.automato_tokenizador)

    def trata_evento(self, evento):
        if evento.tipo == 'LeituraCaractere':
            self.leitura_caractere(*evento.informacao)
        elif evento.tipo == 'ChegadaLinha':
            self.chegada_linha(*evento.informacao)

    def leitura_caractere(self, caractere, num):
        for categoria, conjunto in self.categorias.items():
            if caractere in conjunto:
                classificacao = categoria
        self.caracteres_classificados.append((caractere, classificacao))
        self.tokenizer.add_evento(Evento('InsereNaFita', (caractere, classificacao)))
        self.tokenizer.run()

    def chegada_linha(self, linha, num):
        for i in range(len(linha)):
            caractere = linha[i]
            self.add_evento(Evento('LeituraCaractere', (caractere,i)))
