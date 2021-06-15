from components.bar import Bar
from components.bar_list import BarList
from components.note import Note
from gen.MusicLanguageParser import *
from antlr4.tree import Tree

from music.music_interpreter import MusicInterpreter
from wololo.WololoLanguageOperators import Operators


class Parser:
    def __init__(self, ctx: MusicLanguageParser.ProgramContext):
        self._ctx = ctx
        self.notes = {}
        self.bars = {}
        self.bars_lists = {}
        self.integers = {}
        self.strings = {}
        self.variables = {}
        self.timbre = "Piano"

        self.parseChildren()

    def parseChildren(self, node=None):
        ctx = self._ctx if node is None else node
        for child in ctx.getChildren():
            if isinstance(child, Tree.TerminalNodeImpl):
                continue

            self.parseDeclaration(child)

    def parseDeclaration(self, ctx: ParserRuleContext):
        if isinstance(ctx, Tree.TerminalNodeImpl) or isinstance(ctx, MusicLanguageParser.ConditionContext):
            pass

        elif isinstance(ctx, MusicLanguageParser.PhrasesContext) or \
                isinstance(ctx, MusicLanguageParser.PhraseContext) or \
                isinstance(ctx, MusicLanguageParser.DeclarationContext):
            for child in ctx.getChildren():
                self.parseDeclaration(child)

        elif isinstance(ctx, MusicLanguageParser.NoteContext):
            self.parseNoteDeclaration(ctx)

        elif isinstance(ctx, MusicLanguageParser.BarContext):
            self.parseBarDeclaration(ctx)

        elif isinstance(ctx, MusicLanguageParser.Bars_listContext):
            self.parseBarsListDeclaration(ctx)

        elif isinstance(ctx, MusicLanguageParser.IntegerContext):
            self.parseIntegerDeclaration(ctx)

        elif isinstance(ctx, MusicLanguageParser.StringContext):
            self.parseStringDeclaration(ctx)

        elif isinstance(ctx, MusicLanguageParser.Check_ifContext):
            self.parseCheckIfStatement(ctx)

        elif isinstance(ctx, MusicLanguageParser.For_loopContext):
            self.parseForLoopStatement(ctx)

        elif isinstance(ctx, MusicLanguageParser.PlayContext):
            self.parsePlayStatement(ctx)

        elif isinstance(ctx, MusicLanguageParser.TimbreContext):
            self.parseTimbreDeclaration(ctx)

        else:
            print(type(ctx))

    # parse Note context
    def parseNoteDeclaration(self, ctx: MusicLanguageParser.NoteContext):
        name = ctx.NAME().getText()
        if name not in self.variables.keys():
            pitch = ctx.PITCH().getText()
            duration = ctx.NUMBER().getText()

            if int(ctx.NUMBER().getText()) in [1, 2, 4, 8, 16]:
                self.notes[name] = Note(pitch, duration)
                self.variables[name] = self.notes
            else:
                print("raise invalid duration value")

    # parse Bar context
    def parseBarDeclaration(self, ctx: MusicLanguageParser.BarContext):
        name = ctx.NAME(0).getText()
        notes = []

        if name not in self.variables.keys():
            for note_name in ctx.NAME()[1:]:
                note_name_as_str = note_name.getText()
                if note_name_as_str in self.variables:
                    notes.append(self.notes[note_name_as_str])

            self.bars[name] = Bar(notes)
            self.variables[name] = self.bars

    # parse list of Bars
    def parseBarsListDeclaration(self, ctx: MusicLanguageParser.Bars_listContext):
        name = ctx.NAME(0).getText()
        meter = (int(ctx.meter().NUMBER(0).getText()),
                 int(ctx.meter().NUMBER(1).getText()))
        bars = []

        if name not in self.variables.keys():
            for bar_name in ctx.NAME()[1:]:
                bar_name_as_str = bar_name.getText()
                if bar_name_as_str in self.variables:
                    bars.append(self.bars[bar_name_as_str])

            self.bars_lists[name] = BarList(bars, meter)
            self.variables[name] = self.bars_lists

    # parse integers
    def parseIntegerDeclaration(self, ctx: MusicLanguageParser.IntegerContext):
        name = ctx.NAME().getText()

        if name not in self.variables.keys():
            val = int(ctx.NUMBER().getText())
            self.variables[name] = self.integers
            self.integers[name] = val

    # parse strings
    def parseStringDeclaration(self, ctx: MusicLanguageParser.StringContext):
        name = ctx.NAME().getText()

        if name not in self.variables.keys():
            val = str(ctx.NAME(1).getText())
            self.variables[name] = self.strings
            self.strings[name] = val

    # parse if statement
    def parseCheckIfStatement(self, ctx: MusicLanguageParser.Check_ifContext):
        condition = True
        else_present = False
        else_position = len(ctx.children)
        for i, child in enumerate(ctx.getChildren()):
            if isinstance(child, Tree.TerminalNodeImpl):
                if child.symbol.text == 'else:\n':
                    else_present = True
                    else_position = i

            elif isinstance(child, MusicLanguageParser.ConditionContext):
                condition = self.checkIfStatement(child)

        if condition:
            for i, child in enumerate(ctx.getChildren()):
                if else_position > i:
                    self.parseDeclaration(child)
        elif else_present:
            for i, child in enumerate(ctx.getChildren()):
                if else_position < i:
                    self.parseDeclaration(child)

    def checkIfStatement(self, ctx: MusicLanguageParser.ConditionContext) -> bool:
        names = len(ctx.NAME())
        numbers = len(ctx.NUMBER())
        if names > 1:
            val1 = ctx.NAME(0).getText()
            val2 = ctx.NAME(1).getText()
        elif numbers > 1:
            val1 = ctx.NUMBER(0).getText()
            val2 = ctx.NUMBER(1).getText()
        else:
            val1 = ctx.NAME(0).getText()
            val2 = ctx.NUMBER(0).getText()

        statement = ctx.logic().children[0]
        if type(statement) is MusicLanguageParser.NequalsContext:
            statement = '!=='
        else:
            statement = str(statement)

        if val1 in self.variables.keys():
            val1 = self.variables[val1][val1]
        if val2 in self.variables.keys():
            val2 = self.variables[val2][val2]

        # print(Operators().logic(statement, val1, val2))
        return Operators().logic(statement, val1, val2)

    def parseForLoopStatement(self, ctx: MusicLanguageParser.For_loopContext):
        starting_var = ctx.NAME().getText()
        if starting_var in self.variables and starting_var not in self.integers:
            print("raise type error")
        else:
            start_number = int(ctx.NUMBER(0).getText())
            end_number = int(ctx.NUMBER(1).getText())
            self.integers[starting_var] = start_number
            if start_number < end_number:
                growth = True
            else:
                growth = False
            # condition = self.checkLoopCondition(end_number, starting_var, growth)
            condition = True
            while condition:
                condition = self.checkLoopCondition(end_number, starting_var, growth)
                for child in ctx.getChildren():
                    self.parseDeclaration(child)

    def checkLoopCondition(self, end_number, starting_var, growth):
        if growth:
            print(self.integers[starting_var])
            self.integers[starting_var] += 1
            if self.integers[starting_var] > end_number:
                return False
            return True
        else:
            print(self.integers[starting_var])
            self.integers[starting_var] -= 1
            if self.integers[starting_var] < end_number:
                return False
            return True

    def parsePlayStatement(self, ctx: MusicLanguageParser.PlayContext):
        bars_lists = []
        for list_ in ctx.NAME():
            name = list_.symbol.text
            print(name)
            if name in self.bars_lists.keys():
                bars_lists.append(self.bars_lists[name])
        MusicInterpreter(bars_lists, self.timbre).play()

    def parseTimbreDeclaration(self, ctx: MusicLanguageParser.TimbreContext):
        timbre = ctx.TIMBRE().getText()
        self.timbre = timbre
