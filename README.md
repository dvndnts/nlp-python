# Estudos quanto a utilização de Python para PLN (NLP  - Neutral Language Processing)

Este repositório contém estudos e códigos relacionados ao uso de Python para Processamento de Linguagem Natural (PLN), com foco na extração de palavras-chave de textos em português.
# Scripts
## 1. [repeticao_palavras.py](https://)

Este script realiza a contagem de frequência de palavras em um conjunto de textos. Ele segue os seguintes passos:

- Pré-processamento dos textos: converte para caixa baixa e remove pontuação.
- Conta a ocorrência de cada palavra no conjunto de textos.
- Retorna as palavras mais frequentes, ordenadas da maior para a menor ocorrência.

Esse script auxilia na identificação de termos que podem ser irrelevantes para a análise e, portanto, devem ser adicionados à lista de stopwords (palavras a serem ignoradas na análise de palavras-chave).
## 2. [extracao_keywords.py](https://)

Este script tem como objetivo a extração de palavras-chave dos textos. Ele:

- Usa o modelo de língua portuguesa do spaCy para tokenizar os textos.
- Remove stopwords personalizadas e padrão do spaCy, além de identificar palavras que são similares a stopwords usando fuzzy matching (via biblioteca fuzzywuzzy).
- Retorna uma lista de palavras significativas após a remoção das stopwords.
- Gera um arquivo de texto (keywords_extraidas.txt) contendo as palavras-chave filtradas, que podem ser usadas para gerar uma Nuvem de Palavras.

## Próximos passos

Há a ideia de melhorar essa extração de palavras-chave, possivelmente com o uso de bibliotecas de machine learning como sklearn, ou melhorias nas funcionalidades do spaCy, explorando suas capacidades mais avançadas.
