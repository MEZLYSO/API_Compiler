# Generated from Grammar.g by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#assign.
    def enterAssign(self, ctx:GrammarParser.AssignContext):
        pass

    # Exit a parse tree produced by GrammarParser#assign.
    def exitAssign(self, ctx:GrammarParser.AssignContext):
        pass


    # Enter a parse tree produced by GrammarParser#print.
    def enterPrint(self, ctx:GrammarParser.PrintContext):
        pass

    # Exit a parse tree produced by GrammarParser#print.
    def exitPrint(self, ctx:GrammarParser.PrintContext):
        pass


    # Enter a parse tree produced by GrammarParser#expr.
    def enterExpr(self, ctx:GrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#expr.
    def exitExpr(self, ctx:GrammarParser.ExprContext):
        pass



del GrammarParser