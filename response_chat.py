from openai import OpenAI
import json 
import re
import base64
import requests

client = OpenAI()

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





def convert_image_to_base64(image_path):
    try:
        with open(image_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_image
    except FileNotFoundError:
        return "Imagem não encontrada. Verifique o caminho do arquivo."

def setup():

    

    # Nome do arquivo onde os dados serão salvos
    arquivo_nome = 'resposta.json'

    image_content1 = convert_image_to_base64("./image1.jpg")
    image_content2 = convert_image_to_base64("./image2.jpg")
    image_content3 = convert_image_to_base64("./image3.jpg")

    nome = "10009204 - MOTOR ROLOS FIXO (LADO B) 40CV"
    manufaturado = "WEG"
    modelo = "electricMotor-threePhase"

    stream = client.chat.completions.create(

        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Eu vou converter a string que você enviar em JSON usando json.loads. Ou seja, eu não quero crases ou barras, eu quero que você complete as informações desse JSON de acordo com as imagens da maquina e as informações extras entrgues pelo usuario. Eu só quero o JSON respondido e mais nada. { nome: '', modelo: '', ano: '', valor: '', tipo: '', fabricante: '', identificação: '' }"},
                    {"type": "text", "text": """ Instruções para Análise e Relatório de Manutenção Industrial

    Objetivo: Analisar imagens e dados JSON fornecidos para extrair a maior quantidade de informações possíveis sobre uma máquina em operação, utilizando conhecimentos avançados de Engenharia Mecânica e Elétrica. A análise deve ser precisa e detalhada, considerando tanto os dados fornecidos quanto os registros públicos de máquinas semelhantes da mesma empresa.

    Dados JSON Fornecidos:
    'name': Nome da máquina ou equipamento.
    'manufacturer': Nome da empresa que fabricou o equipamento.
    'model': Tipo ou categoria da máquina.

    Identificação dos Dados do JSON:
    Nome: Extraia o nome do campo 'name' dos dados JSON fornecidos.
    Fabricante: Extraia o nome da empresa fabricante do campo 'manufacturer'.
    Tipo: Identifique o tipo ou categoria da máquina a partir do campo 'model'.
    Identificação e Análise das Imagens:

    Identificacao: Verifique se a identificação (número de série ou código) está presente nos dados JSON ou nas imagens.
    Localizacao: Determine a localização da máquina dentro da planta, observando elementos visuais nas imagens (ex.: cor, material da estrutura).
    Potencia: Identifique a potência nominal da máquina, medida em CV (cavalos-vapor) ou kW (quilowatts). Este dado pode estar no campo 'name' dos dados JSON.
    Tensao: Determine a tensão nominal de operação da máquina.
    Frequencia: Verifique a frequência da corrente elétrica utilizada pela máquina, geralmente em Hz (hertz).
    Rotacao: Identifique a velocidade de rotação do motor, geralmente medida em RPM (rotações por minuto).
    Grau_de_Protecao: Classifique o nível de proteção da máquina contra poeira, água e outros elementos ambientais conforme padrões como o IP (Ingress Protection).
    Eficiencia: Determine a eficiência energética da máquina, expressa em percentual ou classes como IE3.
    Avaliacao do Estado Atual e Condicoes Fisicas:
    Estado_Atual: Descreva o estado atual da máquina, incluindo desgaste, falhas, condições de operação, anomalias e necessidade de manutenção.
    Condicoes_Fisicas: Observe sinais de desgaste, corrosão, rachaduras ou vazamentos.
    Fiacao_e_Conexoes: Avalie o estado das conexões elétricas e cabos.
    Lubrificacao: Verifique pontos de lubrificação e condições de graxa ou óleo.
    Correias_e_Polias: Inspecione o estado de correias, polias e outros componentes mecânicos.
    Acoplamentos_e_Engrenagens: Inspecione visualmente acoplamentos e engrenagens visíveis.
    Localizacao: Descreva o ambiente onde a máquina está instalada (interior, exterior, ambientes com poeira, umidade, etc.).
    Bases_e_Suportes: Verifique a condição e adequação das bases e suportes da máquina.
    Protecoes_e_Seguranca: Confirme a existência e estado de proteções, barreiras de segurança e outros dispositivos de proteção.
    Etiquetas_e_Anotacoes: Procure por notas de manutenção, etiquetas de calibração ou adesivos de última inspeção.
    Acessorios_e_Ferramentas: Verifique a presença de acessórios ou ferramentas acoplados à máquina, como indicadores de pressão, medidores, etc.
    Sinais_de_Reparos: Identifique marcas, soldas ou outras indicações de reparos na máquina.
    Botoes_e_Interruptores: Avalie o estado e função dos controles manuais.
    Indicadores_e_Displays: Verifique a presença e leitura atual de indicadores digitais ou analógicos.
    Cabos_e_Conectores: Avalie o estado dos cabos conectados a painéis de controle.
    Advertencias_e_Instrucoes: Procure por adesivos de advertência, etiquetas de segurança e instruções operacionais.
    Simbolos_de_Perigo: Identifique símbolos que indicam riscos como choque elétrico, superfícies quentes ou peças em movimento.
    Capacidade_e_Desempenho: Para máquinas como compressores, bombas ou motores, inclua informações sobre capacidade de processamento, pressão, vazão, etc.
    Tipos_de_Fluido_ou_Energia_Utilizados: Identifique os tipos de fluidos (óleo, ar comprimido) ou energia utilizados pela máquina.
    Componentes_de_Medicao: Verifique a presença de sensores, medidores ou outros componentes de controle de processos.
    Manuais_ou_Diagramas: Procure por qualquer documentação anexada à máquina, como manuais de operação ou diagramas.
    Conclusao do Relatório: Com base na inspeção visual detalhada, liste as falhas potenciais identificadas e os sinais visuais correspondentes:
    Falhas_de_Lubrificacao: Resíduos de óleo em torno de vedações e rolamentos, coloração escura do óleo.
    Desgaste_de_Rolamentos: Descoloração ou marcas de desgaste nos rolamentos.
    Passagem_de_Pas/Palhetas: Desgaste irregular ou danos nas pás/palhetas.
    Cavitacoes: Danos ou erosão nas superfícies internas das bombas.
    Turbulencias: Fluxo irregular de fluidos, presença de bolhas de ar.
    Recirculacao_de_Bombas: Vibrações anormais na bomba, desgaste nos rotores.
    Barras_de_Rotor_Danificadas/Soltas: Movimentação excessiva, desgaste visível.
    Desgaste_de_Engrenagens: Desgaste visível nos dentes.
    Excentricidade_de_Engrenagens/Rotores: Desgaste desigual.
    Enrolamentos_de_Estator_Soltos: Deslocamento perceptível dos enrolamentos.
    Desalinhamento: Desgaste irregular nos acoplamentos.
    Problemas_Operacionais: Sobrecarga visível, sinais de aquecimento excessivo.
    Deformacao_de_Tubulacoes: Dobras ou deformações visíveis nas tubulações.
    Friccao_ou_Cisalhamento: Desgaste excessivo em áreas de contato.
    Erosao_de_Rolamentos_por_Fuga_de_Corrente: Marcas de queimadura ou desgaste irregular nos rolamentos.
    Desgaste_de_Correias/Polias: Desgaste visível, rachaduras ou quebras.
    Estrutura da Resposta:
    A resposta deve seguir exatamente a estrutura json a seguir:

    {
    "Nome": "resposta",
    "Fabricante": "resposta",
    "Tipo": "resposta",
    "Identificacao": "resposta",
    "Localizacao": "resposta",
    "Potencia": "resposta",
    "Tensao": "resposta",
    "Frequencia": "resposta",
    "Rotacao": "resposta",
    "Grau_de_Protecao": "resposta",
    "Eficiencia": "resposta",
    "Estado_Atual": "resposta",
    "Condicoes_Fisicas": "resposta",
    "Fiacao_e_Conexoes": "resposta",
    "Lubrificacao": "resposta",
    "Correias_e_Polias": "resposta",
    "Acoplamentos_e_Engrenagens": "resposta",
    "Localizacao": "resposta",
    "Bases_e_Suportes": "resposta",
    "Protecoes_e_Seguranca": "resposta",
    "Etiquetas_e_Anotacoes": "resposta",
    "Acessorios_e_Ferramentas": "resposta",
    "Sinais_de_Reparos": "resposta",
    "Botoes_e_Interruptores": "resposta",
    "Indicadores_e_Displays": "resposta",
    "Cabos_e_Conectores": "resposta",
    "Advertencias_e_Instrucoes": "resposta",
    "Simbolos_de_Perigo": "resposta",
    "Capacidade_e_Desempenho": "resposta",
    "Tipos_de_Fluido_ou_Energia_Utilizados": "resposta",
    "Componentes_de_Medicao": "resposta",
    "Manuais_ou_Diagramas": "resposta",
    "Conclusao_de_Relatorio": "resposta",
    "Falhas_de_Lubrificacao": "resposta",
    "Desgaste_de_Rolamentos": "resposta",
    "Passagem_de_Pas/Palhetas": "resposta",
    "Cavitacoes": "resposta",
    "Turbulencias": "resposta",
    "Recirculacao_de_Bombas": "resposta",
    "Barras_de_Rotor_Danificadas/Soltas": "resposta",
    "Desgaste_de_Engrenagens": "resposta",
    "Excentricidade_de_Engrenagens/Rotores": "resposta",
    "Enrolamentos_de_Estator_Soltos": "resposta",
    "Desalinhamento": "resposta",
    "Problemas_Operacionais": "resposta",
    "Deformacao_de_Tubulacoes": "resposta",
    "Friccao_ou_Cisalhamento": "resposta",
    "Erosao_de_Rolamentos_por_Fuga_de_Corrente": "resposta",
    "Desgaste_de_Correias/Polias": "resposta"
    }
    Sempre detalhe a resposta, principalmente quando não houver certeza de que a informação está completamente correta.".
    """},
                    {"type": "text", "text": "Informações extras que voce deve usar: nome: {nome}, manufaturado: {manufaturado}, modelo: {modelo}"},
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