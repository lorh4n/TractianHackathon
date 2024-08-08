from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import os
import base64
from response_chat import setup, client, corrigir_json, salvar_json_em_arquivo, convert_image_to_base64
from prompt import prompt
import json

app = FastAPI()
print("entrou")

# Configurações para servir arquivos estáticos e templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templets")

# Rota principal para servir a página HTML
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Função auxiliar para converter a imagem para base64
async def convert_image_to_base64(file: UploadFile) -> str:
    content = await file.read()
    encoded_image = base64.b64encode(content).decode('utf-8')
    return encoded_image

# Rota para processar o formulário
@app.post("/submit")
async def submit_form(nome: str = Form(...), marca: str = Form(...), modelo: str = Form(...),
                      imagem1: UploadFile = File(...), imagem2: UploadFile = File(...), imagem3: UploadFile = File(...)):
    print("entrou")
    image_content1 = await convert_image_to_base64(imagem1)
    image_content2 = await convert_image_to_base64(imagem2)
    image_content3 = await convert_image_to_base64(imagem3)

    # Aqui você pode usar o código do arquivo Python que você já tem, com as variáveis obtidas do formulário
    response_chat = []
    
    # Chamando o cliente OpenAI para gerar a resposta
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": f"{prompt}"},
                    {"type": "text", "text": f"Informações extras que voce deve usar: nome: {nome}, manufaturado: {marca}, modelo: {modelo}"},
                    {
                    "type": "image_url",
                    "image_url":{ "url": f"data:image/jpeg;base64,{image_content1}"}
                    },
                    {
                    "type": "image_url",
                    "image_url":{ "url": f"data:image/jpeg;base64,{image_content2}"}
                    },
                    {
                    "type": "image_url",
                    "image_url":{ "url": f"data:image/jpeg;base64,{image_content3}"}
                    },
                ],
            }
        ],
        stream=True,
    )

    # Processando a resposta em streaming
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response_chat.append(chunk.choices[0].delta.content)

    # Unindo as partes da resposta
    resultado = ''.join(response_chat)

    # Corrigindo o JSON gerado e salvando em um arquivo
    json_corrigido = corrigir_json(resultado)
    salvar_json_em_arquivo(json_corrigido, 'resposta.json')

    return json.loads(json_corrigido)
