import sys
import antlr4

from gen.MusicLanguageLexer import MusicLanguageLexer
from gen.MusicLanguageParser import MusicLanguageParser
from wololo.WololoLanguageListener import WololoLanguageListener


def main():
    input_stream = antlr4.FileStream(sys.argv[1])
    lexer = MusicLanguageLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = MusicLanguageParser(stream)
    tree = parser.program()
    printer = WololoLanguageListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()
