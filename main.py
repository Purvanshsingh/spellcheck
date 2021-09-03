from fastapi import FastAPI
from pydantic import BaseModel
from spellcorrector import SpellCorrector


class Response(BaseModel):
    word: str


app = FastAPI()
corrector = SpellCorrector()


@app.get('/')
def index():
    return "Enter misspelled word @ /spellcheck"


@app.post('/spellcheck/')
async def index_route(word: Response):
    corrected_word = await corrector.spellcorrect(word.word)
    return {"incorrect_word": word.word, "corrected_word": corrected_word}
