import spacy
from fuzzywuzzy import fuzz
# Fuzz pra checar a similaridade de palavras com stopwords

# Carregar o modelo em Português com spacy
nlp = spacy.load('pt_core_news_sm')

# Lista de respostas abertas
textos = [
    "Usei o sabonete por causa da fragrância, gostei muito do cheiro",
    "Sabonete parece que deixa a pele um toque macio e a fragrância ela não ser rápido da pele",
    "Refrescante, cheiro agradável",
    "Que o cheiro dele fuça na pele depois do banho um cheiro cítrico muito bom o cheiro não é forte transmite limpeza depois do banho eu gostei muito",
    "O cheiro e suave não e fedido forte , e a pele não fico seca ficou macio",
    "O cheiro e bom gostei é suave no banho fragrância atraente da sensação de perfume fresco no banho levemente doce sabonete cheiroso",
    "Nada",
    "Intenso deixa bem perfumado a pele",
    "Gostei que lembra a fragrância do meu dove e eu gosto muito , sinto sensação de limpeza ele deixa pele sedosa",
    "Gostei que ele tem um cheiro floral e que ele elimina todo tipo de resíduos do meu corpo deixando um ótimo cheiro",
    "Gostei pq não enjoativo.fica um cheiro agradável na pele e mesmo depois de um tempo permanece o perfume",
    "Gostei mais do cheiro porque não é muito forte e não deixa minha pele desidratada depois do uso",
    "Gostei do cheiro e muito cheiroso",
    "Gostei do cheiro e como se fixou na minha pele",
    "Gostei deixa cheiro bom na pele",
    "Gostei da fragrância é uma fragrância fresca penetra na pele deixando minha pele cheirosa",
    "Fragrância fresca ,bem cheiroso,fica por bom tempo na pele ,me sentir,me cativou",
    "Fragrância floral e de limpeza",
    "Fa fragrância na pele achei que fuça bastante tempo a fragancia ela não some evapora tem uma durabilidade ótima lembra flores alho floral é fresquinho leve muito bom",
    "Ele e delicado, tem um cheiro de limpeza no corpo passa uma sensação de bem estar",
    "Ele é bem cheiroso, cheiro leve e marcante. Da muita sensação de limpeza.",
    "E um sabonete que deixa a pele limpa deixa com cheiro bom o banheiro fica cheiroso enquanto tomo banho",
    "Dela na pele ela deixa a pele cheirosa deixa um cheiro suave agradavel de sentir da sensação de pele limpa o cheiro transmite limpeza esse cheirinho de flores na pele",
    "Deixou minha pele e minhas mãos macias e cheirosa por mais tempo do que os outros sabonetes.",
    "Deixa a pele macia,cheiroso",
    "Cheiro suave",
    "Cheiro muito bom espuma bem e tem a fragrância boa",
    "Cheiro e a consistência",
    "Cheiro e a consistência",
    "Cheiro agradável deixa perfume duradouro",
    "Aroma agradável e bem suave.",
    "Além de limpar ele tratou da minha pele deixou a minha pele macia e não deixou ressecada",
    "Aí eu gostei muito porque é um sabonete que faz bastante espuma eu adoro bastante espuma",
    "Achei o cheiro bem normal comparado a outras marcas, não há nada surpreendente",
    "Achei leve o cheiro não achei artificial tem um cheiro leve cítrico o cheiro fica natural cítrico achei muito bom o cheiro durante o banho",
    "Achei a fragrância bem convencional, parecida com outros sabonetes disponíveis no mercado."
]

# Adicionando stopwords personalizadas além das padrão do spacy
stopwords_adicionais = {'achei', 'nada', 'gostei',
                        'usei', 'alho', 'fuça', 'fedido', 'deixa'}
# Stopwords a serem removidas da lista padrão
stopwords_remocao = {'bem', 'bom'}

# Combina as stopwords padrão do spaCy com as adicionais
# Incluir as stopwords do Spacy
stopwords_adicionais.update(nlp.Defaults.stop_words)
stopwords_adicionais -= stopwords_remocao  # Remover as stopwords especificadas


# Função para verificar se há stopwords padrão e palavras similares às stopwords
def checar_stopwords(texto):
    doc = nlp(texto)

    # Identifica stopwords padrão no texto
    stopwords_encontradas = [token.text for token in doc if token.is_stop]

    # Identifica palavras similares às stopwords usando fuzzy matching
    palavras_similares = []
    for token in doc:
        if token.text not in stopwords_encontradas and token.is_alpha and token.is_lower:
            for stopword in nlp.Defaults.stop_words:
                similarity = fuzz.ratio(token.text, stopword)
                if similarity > 90:  # Threshold de 90 para considerar a palavra similar
                    palavras_similares.append(token.text)
                    break
    return stopwords_encontradas, palavras_similares

# Função para tokenizar o texto, remover stopwords e palavras similares


def tokenizar_remover_stopwords(text):
    doc = nlp(text)

    # Encontra stopwords e palavras similares no texto
    stopwords_encontradas, palavras_similares = checar_stopwords(text)

    # Atualiza a lista de stopwords com palavras similares encontradas
    stopwords_adicionais.update(stopwords_encontradas)
    stopwords_adicionais.update(palavras_similares)

    # Filtra tokens removendo stopwords e mantendo apenas palavras alfabéticas (descarta conjunções)
    tokens_filtrados = [token.text for token in doc if token.text.lower(
    ) not in stopwords_adicionais and token.is_alpha]

    return tokens_filtrados


# Aplicação da função de tokenização em todos os textos
palavras_frases = []
for texto in textos:
    tokens_filtrados = tokenizar_remover_stopwords(texto)
    # Junta tokens filtrados como frases
    palavras_frases.append(' '.join(tokens_filtrados))

# Junta todas as palavras/frases significativas com quebras de linha
output = '\n'.join(palavras_frases)

# Salvar o resultado para um arquivo .txt
with open('keywords_extraidas.txt', 'w', encoding='utf-8') as f:
    f.write(output)

print(output)
