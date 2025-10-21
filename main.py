from parserapp.utils import run_code


if __name__ == "__main__":
    # Convenience: read from stdin and run
    import sys
    code = sys.stdin.read()
    success, output = run_code(code)
    if success:
        print(output)
    else:
        print(output, file=sys.stderr)
