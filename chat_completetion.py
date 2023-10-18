import requests

def completion_api_call(context: str) -> str:
    """It makes API call to OpenAI's ChatGPT

    Args:
        context (str): context

    Returns:
        str: output based on context
    """

    api_key = "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"
    endpoint = "https://api.openai.com/v1/chat/completions"

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    payload = {"messages": [{"role": "user", "content": context}], "model": "gpt-3.5-turbo-0613", "temperature": 0}

    response = requests.post(endpoint, headers=headers, json=payload)
    response_data = response.json()
    ans = response_data["choices"][0]["message"]["content"]
    return ans


def context_query(query):

    context = f"""
    [Role]: You are a voice assistant that helps us understand user's intent.

    [Description]:
    You will identify user's intent and give me appropraite output based on the following options:
    - youtube: user wants to open or watch videos on youtube
    - google: user wants to search things online or open google
    - github: user wants to open github
    - teams: user wants to open microsoft teams
    - spotify: user wants to play music or open spotify
    - whatsapp: user wants to open and use whatsapp
    - close: user wants to close/exit the application.
    - small_talk: Detect this if none of the above are detected

    [Instructions]:
    - Classify user's intent and generate only 1 intent

    [Query]: {query}
    [Answer]:
"""
    return completion_api_call(context=context)
