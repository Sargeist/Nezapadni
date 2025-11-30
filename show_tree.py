import os

def print_tree(startpath, prefix=""):
    for i, item in enumerate(os.listdir(startpath)):
        path = os.path.join(startpath, item)
        connector = "└── " if i == len(os.listdir(startpath)) - 1 else "├── "
        print(prefix + connector + item)
        if os.path.isdir(path):
            extension = "    " if i == len(os.listdir(startpath)) - 1 else "│   "
            print_tree(path, prefix + extension)

print_tree(".")
