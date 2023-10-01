from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

@app.get("/{name}")
def searching_the_name(name: str):
    return wikipedia.search(name)

@app.get("/limitations/{name}")
def searching_the_name_with_limitations(name: str, limit: int):
    return wikipedia.search(name, results=limit)

class Wiki(BaseModel):
    title: str
    sentences: int = 2
@app.post("/create_article")
def create_article(wiki: Wiki):
    return wiki.title + ' ' + wikipedia.summary(wiki.title, sentences=wiki.sentences)
