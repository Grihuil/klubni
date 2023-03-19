import os

def tree(path, level=0):
    print('|  '*level, end='')
    print('|--', os.path.basename(path))
    if os.path.isdir(path):
        for file in os.listdir(path):
            tree(os.path.join(path, file), level+1)
#чисто изменения внесу вот таким вот текстом
tree('.')