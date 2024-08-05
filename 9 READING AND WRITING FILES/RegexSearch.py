import os, re
from pathlib import Path

def searchInTheFolder(path, pattern):
    path = Path(path)
    regex = re.compile(pattern)
    filenames = os.listdir(path)
    for filename in filenames:
        if re.search(r"\.txt$", filename): # if filename.endwith('.txt'):
            with open(path / filename, 'r') as file:
                for lineNum, line in enumerate(file, 1):
                    if regex.search(line.strip()):
                        print(f'Match found in file {filename}, line {lineNum}: {line.strip()}')

def main():
    path = input("Enter the absolute path of the directory: ")
    pattern = input("Enter the Regex Pattern here : ")
    searchInTheFolder(path, pattern)

if __name__ == "__main__":
    main()