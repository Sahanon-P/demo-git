from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_text():
    return {"messages": "Hello World!"}


@app.post("/{text}")
def post_text(text : str):
    return {"messages": "Done",
    "text" : text}

