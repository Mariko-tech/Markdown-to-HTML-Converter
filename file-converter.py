import markdown
import sys

def validateArgs():
    use_method = sys.argv[1]
    methods = {
        "markdown": 4
    }

    if len(sys.argv) != 4 or sys.argv[1] != "markdown":
        print("Wrong argument num or usage name!")
        print_usage()
        sys.exit()

def print_usage():
    print("Usage:")
    print(" python3 file-convertor.py markdown input.md output.html")

def main():
    validateArgs()
    use_method, input_file, output_file = sys.argv[1:4]

    with open(input_file) as input_f:
        contents = input_f.read()

    if use_method == "markdown":
        new_contents = markdown.markdown(contents)

    with open(output_file, 'w') as output_f:
        output_f.write(new_contents)

if __name__ == "__main__":
    main()