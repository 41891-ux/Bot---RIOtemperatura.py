import requests
from bs4 import BeautifulSoup

cidade_id = 241  # Rio de Janeiro
url = f"http://servicos.cptec.inpe.br/XML/cidade/{cidade_id}/previsao.xml"

resposta = requests.get(url)
resposta.encoding = 'utf-8'

if resposta.status_code != 200:
    print(f"Erro ao acessar a API: {resposta.status_code}")
else:
    soup = BeautifulSoup(resposta.text, 'xml')
    cidade = soup.find('nome').text
    uf = soup.find('uf').text

    previsao = soup.find('previsao')
    if previsao:
        dia = previsao.find('dia').text
        temp_min = previsao.find('minima').text
        temp_max = previsao.find('maxima').text
        tempo = previsao.find('tempo').text  # código do tempo (ex: 'ec', 'c', 'pn', etc.)
        print(f"{cidade}/{uf} — {dia}: {temp_min}°C a {temp_max}°C ({tempo})")
    else:
        print("Não foi possível obter a previsão.")
        
tempos = {
    'ec': 'Encoberto com Chuvas Isoladas',
    'c': 'Chuva',
    'pn': 'Parcialmente Nublado',
    'pp': 'Possibilidade de Pancadas de Chuva',
    'n': 'Nublado',
    'ci': 'Chuvas Isoladas',
    'in': 'Instável',
    'ps': 'Predomínio de Sol',
    'e': 'Encoberto',
    'nv': 'Nevoeiro',
    'g': 'Geada',
    'ne': 'Neve',
    'nd': 'Não Definido',
}

descricao = tempos.get(tempo, 'Desconhecido')
print(f"{cidade}/{uf} — {dia}: {temp_min}°C a {temp_max}°C — {descricao}")