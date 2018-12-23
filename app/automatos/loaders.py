import re
from .automato_finito import TransdutorFinito

__all__ = ['transdutor_finito']


def parse_tf(espec):
    match_automato = re.compile(r'^[\s\t]*<(?P<nome>\w+)>\n(.*)\s*</(?P=nome)>', re.DOTALL | re.MULTILINE)
    match_transicoes = re.compile(r"\(([a-zA-Z]\w*)\s*,\s*'(.+)'\s*\)\s*->\s*([a-zA-Z]\w*)(?:\s*\\\s*(\w+))?\n")

    match_output_1 = match_automato.search(espec)
    nome_automato = match_output_1.group(1)
    linhas = match_output_1.group(2).split('\n')

    # estados
    estados = re.sub(r'^[\s\t]+', r'', linhas[0]).split()

    # inicial
    inicial = re.sub(r'^[\s\t]+', r'', linhas[1])

    # estados finais
    finais = re.sub(r'^[\s\t]+', r'', linhas[2]).split()

    # alfabeto
    alfabeto = re.sub(r'^[\s\t]+', r'', linhas[3]).split()

    # Automato Transdutor
    tf = TransdutorFinito(nome=nome_automato, estados=estados, estadoInicial=inicial, estadosFinais=finais, alfabeto=alfabeto)

    for match_output_2 in match_transicoes.finditer(match_output_1.group(2)):
        qi, s, qj, saida = match_output_2.groups()
        tf.add_transicao(de=qi, com=s, para=qj)
        if saida is not None:
            tf.add_saida(de=qi, com=s, saida=saida)

    return tf


def transdutor_finito(nome_arquivo):
    with open(nome_arquivo) as f:
        texto = f.read()
        texto = re.sub(r'\n+', '\n', texto)
        return parse_tf(texto)

    return None
