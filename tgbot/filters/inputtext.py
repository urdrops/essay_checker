
import aiohttp
import openai
import json
from tgbot.config import load_config


async def analyzes(type1: str, topic: str, essay: str, additional_list=None):
    if additional_list is None:
        additional_list = []
    with open('prompts.json', 'r') as j:
        json_data = json.load(j)
    prompt: str = ""
    user: str = ""
    tokens: int = 0
    match type1:
        case "IELTS Writing Task 2":
            prompt = json_data["ielts_prompt"]
            user = f"Question:\"{topic}\"\nAnswer:\"{essay}\""
            tokens = 800

        case "CEFR proficiency test":
            prompt = json_data["cefr_prompt"]
            user = f"Topic:\"{topic}\"\nEssay:\"{essay}\""
            tokens = 500
        # best version
        case "IELTS Writing Task 2 best":
            additional_list.append()
            prompt = json_data["ielts_prompt"]
            user = f"Question:\"{topic}\"\nAnswer:\"{essay}\""
            tokens = 800

    config = load_config(".env")
    openai.api_key = config.apis.openai_api
    async with aiohttp.ClientSession() as session:
        try:
            # Make the API request
            response = await session.post(
                url="https://api.openai.com/v1/chat/completions",
                json={
                    "model": "gpt-3.5-turbo-16k",
                    "messages": [
                        {"role": "system", "content": prompt},
                        {"role": "user", "content": user},
                        *additional_list
                    ],
                    "temperature": 0,
                    "max_tokens": tokens,
                    "top_p": 1,
                    "frequency_penalty": 0,
                    "presence_penalty": 0
                },
                headers={"Authorization": f"Bearer {openai.api_key}"}
            )

            # Handle API response
            print("enter to get json")
            response_data = await response.json()
            print(response_data)
            return response_data['choices'][0]['message']['content']

        except aiohttp.ClientError as error:
            return str(error)