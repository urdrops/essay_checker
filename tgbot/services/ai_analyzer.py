import aiohttp
import openai

from tgbot.config import load_config


async def analyzes(type1: str, topic: str, essay: str):
    ielts_prompt = """
You will be provided with IETLS writing task 2 from user. Your task is to analyze the provided essay for IELTS Writing Task 2 considering the following evaluation sections: **Task Response, Coherence and Cohesion, Lexical Resource, and Grammatical Range and Accuracy.** Evaluate each section on a scale of 1 to 9, provide brief feedback, and indicate examples from the essay.

Pattern: 

<b>Evaluation and Feedback:</b>

1. <b>Task Response:</b> [Rating and Feedback]
2. <b>Coherence and Cohesion:</b> [Rating and Feedback]
3. <b>Lexical Resource:</b> [Rating and Feedback]
4. <b>Grammatical Range and Accuracy:</b> [Rating and Feedback]

<b>Overall:</b>[Score]

<b>Mistakes:</b>
(show mistakes from the essay)

<b>Improvement Recommendations:</b>
(provide concise recommendations based on identified errors and shortcomings, with brief examples.)"""

    config = load_config(".env")
    openai.api_key = f"{config.apis.openai_api}"

    async with (aiohttp.ClientSession() as session):
        response = await session.post(
            url="https://api.openai.com/v1/chat/completions",
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
    return response_data['choices'][0]['message']['content']
