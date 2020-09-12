from fastapi import FastAPI



def make_app():
    app = FastAPI()

    @app.get("/")
    async def index():
        return 'hi'
    return app