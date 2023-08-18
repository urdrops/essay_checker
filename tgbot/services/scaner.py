import requests
from tgbot.config import load_config


async def scanning(url_photo: str):
    config = load_config(".env")
    url = 'https://pen-to-print-handwriting-ocr.p.rapidapi.com/recognize/'
    headers = {
        'X-RapidAPI-Key': f'{config.apis.pen_to_text_api}',
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
        answer = await response.json()
        await answer['value']
    except requests.exceptions.RequestException as error:
        return error
