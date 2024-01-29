import os
from PIL import Image
import pytesseract

input_folder = 'inputs'
output_folder = 'output'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

        # Ler a imagem e realizar OCR
        img = Image.open(input_path)
        text = pytesseract.image_to_string(img, lang='eng')

        # Salvar o texto no arquivo de saída
        with open(output_path, 'w') as file:
            file.write(text)
