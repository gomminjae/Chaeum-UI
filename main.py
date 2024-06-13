from fastapi import FastAPI
import uvicorn


app = FastAPI(docs_url="/docs", openapi_url="/open-api-docs")

@app.get("/")
async def getHello():
    return "Hello, World!"