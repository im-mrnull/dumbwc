import argparse
import os
import sys

def create_parser():
    parser=argparse.ArgumentParser(description="Coding Challenge 1: wc tool")
    parser.add_argument('-c','--bytes', action='store_true', help="Return number of bytes of file")
    parser.add_argument('-l','--lines', action='store_true', help="Return number of lines in the file")
    parser.add_argument('-w','--words', action='store_true', help="Return number of words in the file")
    parser.add_argument('-m','--characters', action='store_true', help="Return number of characters in the file")
    parser.add_argument('filename',nargs='*',default=['-'],help="File to analyze")
    return parser

def calculate_bytes(file_name):
    try:
        file_path=("./"+file_name)
        file_size_bytes=os.path.getsize(file_path)
        return file_size_bytes
    except FileNotFoundError:
        print("File Not Found 1")
    except Exception as e:
        print(f"An Error occured: {e}")
        
def calculate_lines(file_name):
    try:
        file_path=("./"+file_name)
        with open(file_path,'r') as file:
            file_lines=len(file.readlines())
        return file_lines
    except FileNotFoundError:
        print("File Not Found 2")
    except Exception as e:
        print(f"An Error occured: {e}")


def calculate_words(file_name):
    try:
        count=0
        file_path=("./"+file_name)
        with open(file_path,'r') as file:
            file_lines=file.readlines()
        # print(file_lines)
        for line in file_lines:
            line=line.split()
            for word in line:
                if word.isnumeric() or word.isalpha:
                    count+=1
        return count
    except FileNotFoundError:
        print("File Not Found 3")
    except Exception as e:
        print(f"An Error occured: {e}")

def calculate_characters(file_name):
    try:
        file_path=("./"+file_name)
        with open(file_path,'r', encoding='utf-8', newline='') as file:
            file_char=len(file.read())
        return file_char
    except FileNotFoundError:
        print("File Not Found 4")
    except Exception as e:
        print(f"An Error occured: {e}")

def main():
    parser=create_parser()
    args=parser.parse_args()

    filename = args.filename[0] if args.filename else '-'

    if filename == '-':
        filename=sys.stdin.read()

    if args.bytes:
        bytes = calculate_bytes(filename)
        print (f"{bytes} {filename}")
    elif args.lines:
        lines = calculate_lines(filename)
        print (f"{lines} {filename}")
    elif args.words:
        words = calculate_words(filename)
        print (f"{words} {filename}")
    elif args.characters:
        characters = calculate_characters(filename)
        print (f"{characters} {filename}")
    elif filename:
        lines = calculate_lines(filename)
        words = calculate_words(filename)
        characters = calculate_characters(filename)

        print(f"{lines} {words} {characters} {filename}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()