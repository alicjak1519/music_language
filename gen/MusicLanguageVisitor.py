# Generated from /Users/sol/Documents/MyStuff/informatyka_rokIII/TKiK/music_language/MusicLanguage.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MusicLanguageParser import MusicLanguageParser
else:
    from MusicLanguageParser import MusicLanguageParser

# This class defines a complete generic visitor for a parse tree produced by MusicLanguageParser.

class MusicLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MusicLanguageParser#program.
    def visitProgram(self, ctx:MusicLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#declaration.
    def visitDeclaration(self, ctx:MusicLanguageParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#tempo.
    def visitTempo(self, ctx:MusicLanguageParser.TempoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#meter.
    def visitMeter(self, ctx:MusicLanguageParser.MeterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#timbre.
    def visitTimbre(self, ctx:MusicLanguageParser.TimbreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#note.
    def visitNote(self, ctx:MusicLanguageParser.NoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#bar.
    def visitBar(self, ctx:MusicLanguageParser.BarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#bars_list.
    def visitBars_list(self, ctx:MusicLanguageParser.Bars_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#play.
    def visitPlay(self, ctx:MusicLanguageParser.PlayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#integer.
    def visitInteger(self, ctx:MusicLanguageParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#string.
    def visitString(self, ctx:MusicLanguageParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#phrase.
    def visitPhrase(self, ctx:MusicLanguageParser.PhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#phrases.
    def visitPhrases(self, ctx:MusicLanguageParser.PhrasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#arithmetic.
    def visitArithmetic(self, ctx:MusicLanguageParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#logic.
    def visitLogic(self, ctx:MusicLanguageParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#nequals.
    def visitNequals(self, ctx:MusicLanguageParser.NequalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#check_if.
    def visitCheck_if(self, ctx:MusicLanguageParser.Check_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#condition.
    def visitCondition(self, ctx:MusicLanguageParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MusicLanguageParser#for_loop.
    def visitFor_loop(self, ctx:MusicLanguageParser.For_loopContext):
        return self.visitChildren(ctx)



del MusicLanguageParser