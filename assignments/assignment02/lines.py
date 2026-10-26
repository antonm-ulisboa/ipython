import sys


def get_filename():
    # Check the arguments before opening the file.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    return filename


def count_code_lines(filename):
    total = 0

    with open(filename, encoding="utf-8") as source:
        for line in source:
            # Skip blank lines and full-line comments.
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                total += 1

    return total


def main():
    filename = get_filename()

    try:
        print(count_code_lines(filename))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
