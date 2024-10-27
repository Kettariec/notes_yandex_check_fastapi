import httpx
from typing import List

YANDEX_SPELLER_API_URL = "https://speller.yandex.net/services/spellservice.json/checkText"


async def check_spelling(text: str) -> List[str]:
    async with httpx.AsyncClient() as client:
        response = await client.get(YANDEX_SPELLER_API_URL, params={"text": text})
        response.raise_for_status()
        errors = response.json()
        return [error["word"] for error in errors]
    