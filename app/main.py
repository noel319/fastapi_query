from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.routes.user_routes import router as user_router

app = FastAPI()

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="./static"), name="static")

# Include the user router for API endpoints
app.include_router(user_router)

# Root route to serve the index.html file
@app.get("/")
async def read_root():
    return FileResponse("./static/index.html")
