Arquitetura e Funcionamento do Projeto

Frontend:

O frontend do sistema foi construído utilizando HTML e CSS, proporcionando uma interface simples e intuitiva para o usuário. A interface permite o input dos dados necessários para a criação da ficha técnica, incluindo as informações da máquina, e até três imagens do equipamento. Esses dados são enviados para processamento através de um formulário.

Backend:

O backend foi desenvolvido em Python, utilizando a API do OpenAI para processar as entradas fornecidas pelo usuário e a FastAPI para integrar os scripts de python com chamadas no frontend. As funções desenvolvidas incluem a conversão de imagens para base64, envio das informações para o ChatGPT, e correção do formato JSON recebido.
Além disso, o sistema inclui funcionalidades para salvar as respostas do ChatGPT em arquivos JSON, bem como gerar relatórios em PDF a partir desses dados.

Abordagem:

A abordagem adotada no projeto combina processamento de linguagem natural com técnicas de análise de imagem. O ChatGPT é utilizado para interpretar os dados fornecidos e gerar respostas estruturadas em JSON, que representam a ficha técnica da máquina. A conversão para PDF é realizada para facilitar a distribuição e arquivamento dos relatórios gerados.

Ao receber as imagens, é feita uma análise com as informações obtidas, e, a partir disso, é verificado se a junção dessas informações correspondem à alguma das falhas antecipadas e diagnosticadas que a Tractian já realizou.

Há as respostas obrigatórias, que possuem um campo fixo na página web, e as respostas não obrigatórias (como possíveis falhas, por exemplo), que só aparecerão na página se a resposta do chat GPT for diferente de "null". (a visualização não foi completa)

Resultados e Considerações Finais:

O sistema desenvolvido atende ao objetivo de automatizar a criação de fichas técnicas de máquinas, simplificando o processo de cadastro e fornecendo informações valiosas para sistemas de IA e manutenção. 

Propostas para melhorar o sistema:
- Para fazer o ChatGPT verificar imagens com a ajuda de outras IAs, usaríamos o OpenCV (Open Source), que é uma biblioteca de visão computacional de código aberto que pode ser usada para várias tarefas de processamento de imagem. É Totalmente gratuito e de código aberto, e capaz de processar as imagens para detecção de objetos, análise de padrões, etc., e complementar a análise do ChatGPT.
