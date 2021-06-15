from components.bar import Bar
from components.bar_list import BarList
from components.note import Note
from gen.MusicLanguageListener import MusicLanguageListener
from gen.MusicLanguageParser import MusicLanguageParser
from music.music_interpreter import MusicInterpreter


class WololoLanguageListener(MusicLanguageListener):

    def __init__(self):
        self.notes = {}
        self.bars = {}
        self.bars_lists = {}
        self.variables = []

    def enterPhrase(self, ctx: MusicLanguageParser.PhraseContext):
        pass

    def exitPlay(self, ctx: MusicLanguageParser.PlayContext):
        bars_lists = []
        for bars_list_name in ctx.NAME():
            bars_list = self.bars_lists[bars_list_name.getText()]
            bars_lists.append(bars_list)
        MusicInterpreter(bars_lists).play()

    def enterBars_list(self, ctx: MusicLanguageParser.Bars_listContext):
        name = ctx.NAME(0).getText()
        bars = []

        if name not in self.variables:
            for bar_name in ctx.NAME()[1:]:
                bar_name_as_str = bar_name.getText()
                if bar_name_as_str in self.variables:
                    bars.append(self.bars[bar_name_as_str])

            self.bars_lists[name] = BarList(bars)
            self.variables.append(name)

    def enterBar(self, ctx: MusicLanguageParser.BarContext):
        name = ctx.NAME(0).getText()
        notes = []

        if name not in self.variables:
            for note_name in ctx.NAME()[1:]:
                note_name_as_str = note_name.getText()
                if note_name_as_str in self.variables:
                    notes.append(self.notes[note_name_as_str])

            self.bars[name] = Bar(notes)
            self.variables.append(name)

    def enterNote(self, ctx: MusicLanguageParser.NoteContext):
        name = ctx.NAME().getText()

        if name not in self.variables:
            pitch = ctx.PITCH().getText()
            duration = ctx.NUMBER().getText()

            if int(ctx.NUMBER().getText()) in [1, 2, 4, 8, 16, 32]:
                self.notes[name] = Note(pitch, duration)
                self.variables.append(name)
            else:
                print("Invalid duration vaule")

    def enterInteger(self, ctx: MusicLanguageParser.IntegerContext):
        pass
