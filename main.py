from app.compilador import Compilador

compilador = Compilador()
compilador.compilar('testes/fatorial_laco.txt')
compilador.exportar('out.asm')
