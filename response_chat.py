from openai import OpenAI
import json 
import re
import base64
import requests

def salvar_json_em_arquivo(json_string, arquivo_nome):
    try:
        # Convertendo a string JSON em um objeto Python (dicionário)
        dados = json.loads(json_string)
        
        # Salvando o objeto Python em um arquivo JSON
        with open(arquivo_nome, 'w') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)
        
        print(f"Dados salvos em '{arquivo_nome}'.")
    except json.JSONDecodeError:
        print("A string JSON fornecida não é válida.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def corrigir_json(json_string):
    # Corrige aspas simples para aspas duplas
    json_string = json_string.replace("`", "")
    json_string = json_string.replace("json", "")
    
    # Corrige vírgulas faltando antes das chaves e valores
    json_string = re.sub(r'(\w+):', r'"\1":', json_string)
    
    # Adiciona aspas duplas ao redor das chaves se necessário
    json_string = re.sub(r'(?<=:)\s*(\w+)(?=,|\})', r'"\1"', json_string)

    # Remove caracteres indesejados (por exemplo, barras invertidas)
    json_string = json_string.replace('\\', '')

    # Tenta carregar o JSON para verificar se está correto
   

    return json_string


def convert_image_to_base64(image_path):
    try:
        with open(image_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_image
    except FileNotFoundError:
        return "Imagem não encontrada. Verifique o caminho do arquivo."


client = OpenAI()

# Nome do arquivo onde os dados serão salvos
arquivo_nome = 'resposta.json'

image_content = convert_image_to_base64("./julho.jpg")



stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Eu vou converter a string que você enviar em JSON usando json.loads. Ou seja, eu não quero crases ou barras, eu quero que você complete as informações desse JSON de acordo com as imagens da maquina e as informações extras entrgues pelo usuario. Eu só quero o JSON respondido e mais nada. { nome: '', modelo: '', ano: '', valor: '', tipo: '', fabricante: '', identificação: '' }"},
                {"type": "text", "text": "Informações extras: nome: 10009204 - MOTOR ROLOS FIXO (LADO B) 40CV, manufaturado: WEG, modelo: electricMotor-threePhase"},
                {
                "type": "image_url",
                "image_url":{ "url": f"data:image/jpeg;base64,{image_content}"
                }

                },
            ],
        }
    ],
    stream=True,
)

response_chat = []

# Processando a resposta em streaming
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        response_chat.append(chunk.choices[0].delta.content)

# Unindo as partes da resposta
resultado = ''.join(response_chat)
print (resultado)

# Chama a função para salvar o JSON em um arquivo
json_corrigido = corrigir_json(resultado)
print(json_corrigido)
salvar_json_em_arquivo(json_corrigido, arquivo_nome)