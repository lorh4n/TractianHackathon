prompt = """
Eu vou converter a string que você enviar em JSON usando json.loads. Ou seja, eu não quero crases ou barras, eu quero que você complete as informações desse JSON de acordo com as imagens da maquina e as informações extras entrgues pelo usuario. Eu só quero o JSON respondido e mais nada. { exemplo: 'resposta', : '', : '' 


Instruções para Análise e Relatório de Manutenção Industrial

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
Sempre detalhe a resposta, principalmente quando não houver certeza de que a informação está completamente correta. QUANDO NÃO SOUBER A RESPOSTA, COLOQUE APENAS "null".
"""