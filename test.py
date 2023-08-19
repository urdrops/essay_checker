import asyncio
import aiohttp
import openai

# Создаем мьютекс для синхронизации доступа к analyzes
analyzes_lock = asyncio.Lock()


async def result_handler(user_info):
    data_task = asyncio.create_task(analyzes(user_info['type'], user_info['topic'], user_info['essay']))
    # Выполняйте другие задачи здесь, если нужно
    # ...

    data_result = await data_task
    print(data_result)


async def analyzes(type1: str, topic: str, essay: str):
    async with analyzes_lock:  # Блокируем доступ для других вызовов analyzes
        ielts_prompt = "подсказка для искусственного интеллекта"

        config = load_config(".env")
        openai.api_key = f"{config.apis.openai_api}"

        async with aiohttp.ClientSession() as session:
            response = await session.post(
                "https://api.openai.com/v1/chat/completions",
                json={
                    "model": "gpt-3.5-turbo-16k",
                    "messages": [
                        {"role": "system", "content": ielts_prompt},
                        {"role": "user", "content": f"Question:\"{topic}\"\nAnswer:\"{essay}\""}
                    ],
                    "temperature": 0,
                    "max_tokens": 800,
                    "top_p": 1,
                    "frequency_penalty": 0,
                    "presence_penalty": 0
                },
                headers={"Authorization": f"Bearer {openai.api_key}"}
            )
            response_data = await response.json()

        print("готово")
        return response_data['choices'][0]['message']['content']


# Создаем список пользователей для обработки
users = [
    {'type': 'type1', 'topic': 'topic1', 'essay': 'essay1'},
    {'type': 'type2', 'topic': 'topic2', 'essay': 'essay2'},
    # Добавьте других пользователей
]


# Запускаем обработку для каждого пользователя
async def main():
    tasks = [result_handler(user_info) for user_info in users]
    await asyncio.gather(*tasks)


asyncio.run(main())
