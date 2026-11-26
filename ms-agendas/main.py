from fastapi import FastAPI


app = FastAPI(debug=True)

@app.get("/")
def home():
    return {"message": "holis"}

