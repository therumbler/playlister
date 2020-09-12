import logging
from pathlib import Path

import aiofiles
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse, RedirectResponse

logger = logging.getLogger(__name__)
def make_app():
    app = FastAPI()
    static_dir = Path(__file__).parent.parent
    logger.info('static_dir = %s', static_dir)
    static_dir = f"{static_dir}/playlister-vue/dist/"
    app.mount(
        "/static", StaticFiles(directory=static_dir), name="static"
    )
    index_html = None
    with open("./playlister-vue/dist/index.html") as f:
        index_html = f.read()

    @app.get("/")
    async def index():
        return HTMLResponse(index_html)

    @app.get("/api")
    async def api():
        return {"hi":"there"}
    
    return app