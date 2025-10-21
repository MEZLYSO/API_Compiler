from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from MyVisitor import MyVisitor
from flask import Flask, request, jsonify
from flask_cors import CORS
import io
import sys
import traceback


app = Flask(__name__)
CORS(app) 

def run_code(code: str):
    """Run the provided code using the generated parser/visitor and capture printed output.

    Returns a tuple (success: bool, output: str). If success is False, output contains the
    exception traceback.
    """
    # Prepare streams and parser
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


code = """x = 4
y = 3
z = x * y + 10
print(z)
x = x + 1
print(x)
"""


@app.route("/", methods=["POST"])
def index():
    code = None
    if request.is_json:
        data = request.get_json()
        if isinstance(data, dict):
            code = data.get('text') 

    output = run_code(code)
    return jsonify({'output': output})



if __name__ == "__main__":
    app.run(debug=True)
