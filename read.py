# read contents of ./submodule/note.txt
with open('./submodule/note.txt', 'r') as file:
    content = file.read()
    print(content)