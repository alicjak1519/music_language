import antlr4
import argparse

from gen.MusicLanguageLexer import MusicLanguageLexer
from gen.MusicLanguageParser import MusicLanguageParser
from wololo.WololoErrorListener import ThrowingErrorListener
from wololo.WololoLanguageListener import WololoLanguageListener


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--composition-path', type=str,
                        help='Path to input file with your composition in Wololo language')
    args = parser.parse_args()

    interpret_composition(args.composition_path)


def interpret_composition(composition_path: str):
    input_stream = antlr4.FileStream(composition_path)
    lexer = MusicLanguageLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())

    stream = antlr4.CommonTokenStream(lexer)
    parser = MusicLanguageParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())

    tree = parser.program()
    printer = WololoLanguageListener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(printer, tree)


if __name__ == '__main__':
    main()
