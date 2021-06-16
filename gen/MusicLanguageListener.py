# Generated from /Users/sol/Documents/MyStuff/informatyka_rokIII/TKiK/music_language/MusicLanguage.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MusicLanguageParser import MusicLanguageParser
else:
    from MusicLanguageParser import MusicLanguageParser

# This class defines a complete listener for a parse tree produced by MusicLanguageParser.
class MusicLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by MusicLanguageParser#program.
    def enterProgram(self, ctx:MusicLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#program.
    def exitProgram(self, ctx:MusicLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#declaration.
    def enterDeclaration(self, ctx:MusicLanguageParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#declaration.
    def exitDeclaration(self, ctx:MusicLanguageParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#tempo.
    def enterTempo(self, ctx:MusicLanguageParser.TempoContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#tempo.
    def exitTempo(self, ctx:MusicLanguageParser.TempoContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#meter.
    def enterMeter(self, ctx:MusicLanguageParser.MeterContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#meter.
    def exitMeter(self, ctx:MusicLanguageParser.MeterContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#timbre.
    def enterTimbre(self, ctx:MusicLanguageParser.TimbreContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#timbre.
    def exitTimbre(self, ctx:MusicLanguageParser.TimbreContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#note.
    def enterNote(self, ctx:MusicLanguageParser.NoteContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#note.
    def exitNote(self, ctx:MusicLanguageParser.NoteContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#bar.
    def enterBar(self, ctx:MusicLanguageParser.BarContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#bar.
    def exitBar(self, ctx:MusicLanguageParser.BarContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#bars_list.
    def enterBars_list(self, ctx:MusicLanguageParser.Bars_listContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#bars_list.
    def exitBars_list(self, ctx:MusicLanguageParser.Bars_listContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#play.
    def enterPlay(self, ctx:MusicLanguageParser.PlayContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#play.
    def exitPlay(self, ctx:MusicLanguageParser.PlayContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#integer.
    def enterInteger(self, ctx:MusicLanguageParser.IntegerContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#integer.
    def exitInteger(self, ctx:MusicLanguageParser.IntegerContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#string.
    def enterString(self, ctx:MusicLanguageParser.StringContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#string.
    def exitString(self, ctx:MusicLanguageParser.StringContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#phrase.
    def enterPhrase(self, ctx:MusicLanguageParser.PhraseContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#phrase.
    def exitPhrase(self, ctx:MusicLanguageParser.PhraseContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#phrases.
    def enterPhrases(self, ctx:MusicLanguageParser.PhrasesContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#phrases.
    def exitPhrases(self, ctx:MusicLanguageParser.PhrasesContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#arithmetic.
    def enterArithmetic(self, ctx:MusicLanguageParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#arithmetic.
    def exitArithmetic(self, ctx:MusicLanguageParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#logic.
    def enterLogic(self, ctx:MusicLanguageParser.LogicContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#logic.
    def exitLogic(self, ctx:MusicLanguageParser.LogicContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#nequals.
    def enterNequals(self, ctx:MusicLanguageParser.NequalsContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#nequals.
    def exitNequals(self, ctx:MusicLanguageParser.NequalsContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#check_if.
    def enterCheck_if(self, ctx:MusicLanguageParser.Check_ifContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#check_if.
    def exitCheck_if(self, ctx:MusicLanguageParser.Check_ifContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#condition.
    def enterCondition(self, ctx:MusicLanguageParser.ConditionContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#condition.
    def exitCondition(self, ctx:MusicLanguageParser.ConditionContext):
        pass


    # Enter a parse tree produced by MusicLanguageParser#for_loop.
    def enterFor_loop(self, ctx:MusicLanguageParser.For_loopContext):
        pass

    # Exit a parse tree produced by MusicLanguageParser#for_loop.
    def exitFor_loop(self, ctx:MusicLanguageParser.For_loopContext):
        pass



del MusicLanguageParser