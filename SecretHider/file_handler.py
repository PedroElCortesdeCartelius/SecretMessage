import os
class FileHandler:
    def read_file(self, path:str):
        if not os.path.exists(path):
            print("The path is incorrect or the file does not exist")
        with open(path, 'r') as f:
            content = f.read()
            return content
    def write_file(self, path:str, text:str):
        with open(path, 'w') as f:
            f.write(text)





