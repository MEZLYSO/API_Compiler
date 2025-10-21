# Generated from Grammar.g by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#program.
    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assign.
    def visitAssign(self, ctx:GrammarParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#print.
    def visitPrint(self, ctx:GrammarParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expr.
    def visitExpr(self, ctx:GrammarParser.ExprContext):
        return self.visitChildren(ctx)



del GrammarParser