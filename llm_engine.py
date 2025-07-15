import os
import openai
import anthropic

OPENAI_MODEL = "gpt-4"  # or gpt-3.5-turbo
ANTHROPIC_MODEL = "claude-3-haiku-20240307"

def get_llm_response(prompt: str) -> str:
    engine = os.getenv("LLM_PROVIDER", "openai")

    if engine == "openai":
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
            max_tokens=500
        )
        return response["choices"][0]["message"]["content"].strip()

    elif engine == "anthropic":
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=500,
            temperature=0.8,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text.strip()

    else:
        raise ValueError("Unsupported LLM_PROVIDER")
