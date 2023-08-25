import aiohttp
import requests

from tgbot.config import load_config


async def scanning(url_photo: str):
    config = load_config(".env")
    url = 'https://pen-to-print-handwriting-ocr.p.rapidapi.com/recognize/'
    headers = {
        'X-RapidAPI-Key': f'{config.apis.pen_to_text_api}',
        'X-RapidAPI-Host': 'pen-to-print-handwriting-ocr.p.rapidapi.com',
    }

    data = aiohttp.FormData()
    data.add_field(name='Session', value='string')

    async with aiohttp.ClientSession() as session:
        async with session.get(url_photo) as img_response:
            img_content = await img_response.read()
            data.add_field(name='srcImg', value=img_content, content_type='image/jpeg', filename='image.jpg')

            try:
                async with session.post(url, headers=headers, data=data) as response:
                    answer = await response.json()
                    return answer['value']
            except aiohttp.ClientError as error:
                return str(error)
