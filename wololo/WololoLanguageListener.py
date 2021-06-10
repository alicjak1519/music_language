from gen.MusicLanguageListener import MusicLanguageListener
from gen.MusicLanguageParser import MusicLanguageParser


class WololoLanguageListener(MusicLanguageListener):

    def __init__(self):
        self.declarations = {}

    def enterPhrase(self, ctx: MusicLanguageParser.PhraseContext):
        pass

    def enterPlay(self, ctx: MusicLanguageParser.PlayContext):
        pass

    def enterBars_list(self, ctx: MusicLanguageParser.Bars_listContext):
        pass

    def enterBar(self, ctx: MusicLanguageParser.BarContext):
        pass

    def enterNote(self, ctx: MusicLanguageParser.NoteContext):
        pass
