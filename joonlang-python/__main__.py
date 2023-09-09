import sys
from .runtime import Joon

def main():
    if len(sys.argv) != 2:
        print("Usage: joon <filename.joon>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, "r", encoding="UTF-8") as file:
        code = file.read()

    interpreter = Joon()
    interpreter.compile(code)

if __name__ == "__main__":
    main()