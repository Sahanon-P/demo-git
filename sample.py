from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_text():
    pass


@app.post("/{text}")
def post_text(text : str):
    pass

