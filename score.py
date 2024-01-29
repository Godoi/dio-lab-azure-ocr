import os

def run(input_data):
    result = {}
    for filename in os.listdir(input_data):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_data, filename)
            with open(file_path, 'r') as file:
                result[filename] = file.read()
    return result
