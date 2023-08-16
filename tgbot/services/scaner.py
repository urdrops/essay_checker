import requests


def scanning(url_photo: str):
    url = 'https://pen-to-print-handwriting-ocr.p.rapidapi.com/recognize/'
    headers = {
        'X-RapidAPI-Key': 'f3aef16d90msh4a9bf5cbd17468ep1c1434jsn4abd1443e3d5',
        'X-RapidAPI-Host': 'pen-to-print-handwriting-ocr.p.rapidapi.com',
    }

    data = {
        'Session': 'string',
    }
    response = requests.get(url_photo)
    files = {
        'srcImg': response.content,
    }

    try:
        response = requests.post(url, headers=headers, data=data, files=files)
        answer = response.json()
        return answer['value']
    except requests.exceptions.RequestException as error:
        return error
