# Processamento de Imagens com Azure ML

Este projeto realiza OCR (Optical Character Recognition) em imagens usando Azure ML para transformar as imagens em dados.

## Estrutura do Projeto

project_root/
|-- inputs/
| |-- image1.jpg
| |-- image2.jpg
| |-- ...
|-- output/
|-- transform_images.py
|-- score.py
|-- requirements.txt
|-- readme.md


## Instruções de Uso

1. Coloque suas imagens na pasta `inputs`.
2. Execute `transform_images.py` para realizar o pré-processamento e gerar arquivos de texto na pasta `output`.
3. Implante os scripts no Azure ML e use `score.py` como script de inferência.

## Dependências

As dependências estão listadas no arquivo `requirements.txt`. Você pode instalá-las usando:

```bash
pip install -r requirements.txt


### Observações:

- O script `transform_images.py` utiliza a biblioteca `pytesseract` para OCR. Certifique-se de ter o Tesseract OCR instalado no seu sistema.
- Este exemplo é básico e pode ser estendido para atender a requisitos mais complexos ou cenários de produção.



