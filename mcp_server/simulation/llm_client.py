"""OpenAI SDK compatible LLM client for simulation agent calls."""

import os
import time
import openai


class SimulationConfigError(Exception):
    """Raised when LLM configuration env vars are missing."""


class SimulationLLMError(Exception):
    """Raised when an LLM API call fails after retries."""


_client: openai.OpenAI | None = None


def get_client() -> openai.OpenAI:
    """Lazy-initialize the OpenAI client from env vars."""
    global _client
    if _client is not None:
        return _client

    api_key = os.environ.get("LLM_API_KEY")
    base_url = os.environ.get("LLM_BASE_URL")
    model = os.environ.get("LLM_MODEL_NAME")

    if not api_key:
        raise SimulationConfigError(
            "LLM_API_KEY not set. Configure environment variables:\n"
            "  LLM_API_KEY=your-api-key\n"
            "  LLM_BASE_URL=https://api.openai.com/v1  (or compatible endpoint)\n"
            "  LLM_MODEL_NAME=gpt-4o  (or your model)"
        )

    _client = openai.OpenAI(api_key=api_key, base_url=base_url)
    return _client


def get_model() -> str:
    return os.environ.get("LLM_MODEL_NAME", "gpt-4o")


def complete(
    system: str,
    user: str,
    temperature: float = 0.7,
    max_tokens: int = 1024,
) -> str:
    """Single LLM completion call. Returns content string.

    Retries once on API error with a 2-second delay.
    """
    client = get_client()
    model = get_model()

    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]

    for attempt in range(2):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except openai.APIError as e:
            if attempt == 0:
                time.sleep(2)
                continue
            raise SimulationLLMError(f"LLM API call failed after retry: {e}") from e
