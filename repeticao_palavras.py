from collections import Counter
import string

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


# Passo 1: Pré-processamento do texto

def preprocess_texto(texto):
    # Conversão para caixa baixa e remoção de pontuação
    texto = texto.lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    return texto


# Passo 2: Contagem de frequência de cada palavra
contagem_palavras = Counter()

for texto in textos:
    texto_processado = preprocess_texto(texto)
    palavras = texto_processado.split()
    contagem_palavras.update(palavras)

# Passo 3: Identificar palavras repetidas
threshold = 3  # Definição de um threshold para repetição
palavras_repetidas = {palavra: cont for palavra,
                      cont in contagem_palavras.items() if cont >= threshold}
palavras_repetidas_ord = dict(
    sorted(palavras_repetidas.items(), key=lambda item: item[1], reverse=True))

print("Palavras repetidas (Ordenadas por Frequência):")
for palavra, cont in palavras_repetidas_ord.items():
    print(f"{palavra}: {cont}")
