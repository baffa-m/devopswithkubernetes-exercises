from fastapi import FastAPI
from pydantic import BaseSettings

class Settings(BaseSettings):
    port: str

    class Config:
        env_file = ".env"

settings = Settings()
app = FastAPI()

@app.get("/")
def hello():
    print("Server started in port {settings.port}")
    return {"message": f"Server started in port {settings.port}"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=settings.port)