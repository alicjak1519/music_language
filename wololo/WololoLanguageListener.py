from components.bar import Bar
from components.bar_list import BarList
from components.note import Note
from gen.MusicLanguageListener import MusicLanguageListener
from gen.MusicLanguageParser import MusicLanguageParser
from music.interpreter import Interpreter
from wololo.WololoLanguageParser import Parser


class WololoLanguageListener(MusicLanguageListener):

    def __init__(self):
        self.notes = {}
        self.bars = {}
        self.bars_lists = {}
        self.integers = {}
        self.strings = {}
        self.variables = []

    def enterProgram(self, ctx:MusicLanguageParser.ProgramContext):
        pp = Parser(ctx)
        # pp

    def enterPhrase(self, ctx: MusicLanguageParser.PhraseContext):
        pass

    def exitPlay(self, ctx: MusicLanguageParser.PlayContext):
        pass
        # check parent, if program, continue
        # else pass
        #
        # for bars_list_name in ctx.NAME():
        #     bars_list = self.bars_lists[bars_list_name.getText()]
        #     Interpreter(bars_list).play()

    def enterBars_list(self, ctx: MusicLanguageParser.Bars_listContext):
        pass

    def enterBar(self, ctx: MusicLanguageParser.BarContext):
        pass

    def enterNote(self, ctx: MusicLanguageParser.NoteContext):
        pass

    def enterInteger(self, ctx: MusicLanguageParser.IntegerContext):
        pass

    def enterString(self, ctx:MusicLanguageParser.StringContext):
        pass

    def enterCheck_if(self, ctx:MusicLanguageParser.Check_ifContext):
        x = ctx.condition()