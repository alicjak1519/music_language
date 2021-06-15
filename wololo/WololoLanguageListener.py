from gen.MusicLanguageListener import MusicLanguageListener
from gen.MusicLanguageParser import MusicLanguageParser
from wololo.WololoLanguageParser import Parser


class WololoLanguageListener(MusicLanguageListener):

    def enterProgram(self, ctx:MusicLanguageParser.ProgramContext):
        pp = Parser(ctx)
        pp