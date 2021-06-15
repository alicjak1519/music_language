from gen.MusicLanguageListener import MusicLanguageListener
from gen.MusicLanguageParser import MusicLanguageParser
from wololo.WololoLanguageParser import Parser


class WololoLanguageListener(MusicLanguageListener):

    def exitProgram(self, ctx: MusicLanguageParser.ProgramContext):
        Parser(ctx)
