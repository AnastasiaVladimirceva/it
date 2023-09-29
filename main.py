from fastapi import FastAPI
import pyjokes

app = FastAPI()
@app.get("/{friend}")
def joke():
    return pyjokes.get_joke()

def friends_joke(friend: str):
    return friend + " tells his joke:" + pyjokes.get_joke()

def multi_friends_joke(friend: str, jokes_number: int):
    result = ""
    for i in range(jokes_number):
        result += friend + f" tells his joke #{i + 1}: " + pyjokes.get_joke() + ""
    return result