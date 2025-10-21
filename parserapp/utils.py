from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from MyVisitor import MyVisitor
import io
import sys
import traceback


def run_code(code: str):
    """Run the provided code using the generated parser/visitor and capture printed output.

    Returns a tuple (success: bool, output: str). If success is False, output contains the
    exception traceback.
    """
    input_stream = InputStream(code)
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.program()

    old_stdout = sys.stdout
    buf = io.StringIO()
    sys.stdout = buf
    try:
        visitor = MyVisitor()
        visitor.visit(tree)
        sys.stdout.flush()
        output = buf.getvalue()
        return True, output
    except Exception:
        tb = traceback.format_exc()
        return False, tb
    finally:
        sys.stdout = old_stdout
