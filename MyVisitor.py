from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser


class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory = {}

    def visitProgram(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value

    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        print(value)

    def visitExpr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            name = ctx.ID().getText()
            if name not in self.memory:
                raise NameError(f"Variable '{name}' no definida")
            return self.memory[name]
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            if ctx.op.text == "+":
                return left + right
            if ctx.op.text == "-":
                return left - right
            if ctx.op.text == "*":
                return left * right
            if ctx.op.text == "/":
                if right == 0:
                    raise ValueError("División por cero")
                return left / right
        else:
            return self.visit(ctx.expr(0))
