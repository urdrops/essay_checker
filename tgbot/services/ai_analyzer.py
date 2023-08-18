import openai
from tgbot.config import load_config


def analyzes(type1: str, topic: str, essay: str):
    config = load_config(".env")
    openai.api_key = f"{config.apis.openai_api}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with IETLS writing task 2. Your task is conduct a thorough analysis of the presented essay in line with the evaluation criteria of IELTS Writing Task 2. For each of the four specified criteria: <b>Task Achievement</b>, <b>Coherence and Cohesion</b>, <b>Lexical Resource</b>, and <b>Grammatical Range and Accuracy</b>, provide a score from 0 to 9 and justify it with examples from the text. Additionally, highlight the strengths of the work and provide constructive feedback on potential areas for improvement.\n\nPattern:\n\n<b>Feedback:</b>\n- <b>Task Achievement:</b> Score: X with float. Example: Your response doesn't fully cover all aspects of the topic. For instance, in point Y, you could have included more in-depth arguments.\n- <b>Coherence and Cohesion:</b> Score: X with float. Example: Your text is easily readable, but the paragraph structure in point Z could be more consistent.\n- <b>Lexical Resource:</b> Score: X with float. Example: Your vocabulary is impressive; however, using specific terms in point W could enhance your argumentation.\n- <b>Grammatical Range and Accuracy:</b> Score: X with float. Example: Your grammar is generally good, but in sentence V, pay attention to the correct use of tenses.(Underlined error: \"needs\" should be \"need\".)\n\n**Overall:**Score: X with float. Example: Your score is that because..\n\n**Strengths:**\nCompelling arguments in point A, a good flow of ideas in point B.\n\n**Areas for Improvement:**\nDeeper analysis in point C, maintaining consistency in point D.\n\nPlease use this analysis to further develop your writing skills.\n\nThank you for your work on the essay!"
            },
            {
                "role": "user",
                "content": f"Question:\"{topic}\"\n\nAnswer:\"{essay}\""
            }
        ],
        temperature=0,
        max_tokens=1300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content

