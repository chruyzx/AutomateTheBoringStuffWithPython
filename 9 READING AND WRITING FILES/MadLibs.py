import os
import re

def madLibs(filename):
    try:
        with open(os.path.join(os.path.curdir, filename), 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print("The file is not found.")
        return
    
    words = re.findall(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b', text)
    for word in words:
        if word in ['ADJECTIVE', 'ADVERB']:
            replace = input(f'Enter an {word.lower()} : ')
        else:
            replace = input(f'Enter a {word.lower()} : ')
        text = text.replace(word, replace, 1)
    print(text)
    newFilename = filename.split('.')[0] + '-madlib.' + filename.split('.')[1]
    with open(os.path.join(os.path.curdir, newFilename), 'w') as f:
        f.write(text)

if __name__ == "__main__":
    filename = input("Enter the filename with the extension here: ")
    madLibs(filename)


