from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
@app.get("/search")
async def read_search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})

@app.get("/add-product")
async def read_add_product_page(request: Request):
    return templates.TemplateResponse("add_product.html", {"request": request})

@app.post("/search")
async def search(query: str = Form(...)):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Perform a SQL query to search for products that match the query term
    cursor.execute("SELECT name, description FROM products WHERE name LIKE ?", ('%' + query + '%',))
    results = [{"name": row[0], "description": row[1]} for row in cursor.fetchall()]

    # Close the database connection
    conn.close()

    # Return the results as JSON
    return JSONResponse(content=results)

# endpoint to add a product
@app.post("/add_product")
async def add_product(name: str = Form(...), description: str = Form(...)):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()
    return JSONResponse(content={"message": "Product added successfully"})