from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

import json, sqlite3, os, subprocess
from subprocess import PIPE
from module import *

# Env for DB
DB_NAME = "db.sqlite3"
TABLE_NAME = "oogiri"

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/files", StaticFiles(directory="files"), name="files")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    init_db_url = request.url_for("init_db")
    list_url = request.url_for("list")
    confirm_url = request.url_for("confirm")

    path = os.getcwd() + "/files/"
    files = os.listdir(path)

    return templates.TemplateResponse('index.html', {'request': request, "files": files, 'init_db_url': init_db_url, 'list_url': list_url, "confirm_url": confirm_url})

@app.api_route("/list/", methods=["GET", "POST"], response_class=HTMLResponse)
def list(request: Request, message: Optional[str] = None):
    index_url = request.url_for('index')
    answer_url = request.url_for('answer')

    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()

        sql = 'SELECT * FROM "{}"'.format(TABLE_NAME)
        cur.execute(sql)
        objects = data_to_dict(cur.fetchall())

        return templates.TemplateResponse('list.html', {'request': request, 'index_url': index_url, 'answer_url': answer_url, 'objects': objects, 'message': message})

    except Exception as e:
        message = "{0}\n{1}".format(message, str(e))
        return templates.TemplateResponse('list.html', {'request': request, 'index_url': index_url, 'answer_url': answer_url, 'message': message})

@app.get("/answer/", response_class=HTMLResponse)
def answer(request: Request, id: int, title: str, image: str, answer: str):
    list_url = request.url_for("list")
    update_db_url = request.url_for("update_db")

    return templates.TemplateResponse('answer.html', {'request': request, 'list_url': list_url, 'update_db_url': update_db_url, 'id': id, 'title': title, 'answer': answer, 'image': image})

@app.get("/init_db/", response_class=RedirectResponse)
def init_db(request: Request, db_init_file: str):
    url = request.url_for('list')

    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        
        # Create table
        cur.execute('drop table if exists "%s"' % TABLE_NAME)
        cur.execute('CREATE TABLE "%s" (id INTEGER PRIMARY KEY, title VARCHAR, answer VARCHAR, image VARCHAR)' % TABLE_NAME)
        
        # Initialize table
        path = "files/" + db_init_file
        data = json.load(open(path, 'r'))

        for value in data.values():
            sql = 'INSERT INTO {0}(title, answer, image) VALUES("{1}", "{2}", "{3}")'.format(TABLE_NAME, value[0], value[1], value[2])
            cur.execute(sql)
        
        con.commit()
        con.close()

        return url

    except Exception as e:
        print(str(e))
        url = "{0}?message=Failed to initialize the DB".format(url)
        return url

@app.get("/update_db/", response_class=RedirectResponse)
def update_db(request: Request, id, answer):
    print(id, answer)
    url = request.url_for('list')

    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()

        # update table
        sql = 'UPDATE {0} SET answer="{1}" where id={2}'.format(TABLE_NAME, answer, id)
        print("####", sql)
        cur.execute(sql)

        con.commit()
        con.close()

        return url

    except Exception as e:
        print(str(e))
        url = "{0}?message=Failed to Update the DB".format(url)
        return url

@app.get("/confirm/", response_class=HTMLResponse)
def confirm(request: Request, file: str):
    index_url = request.url_for('index')
    try:
        path = os.getcwd() + "/files/" + file
        proc = subprocess.run("cat {}".format(path), shell=True, stdout=PIPE, stderr=PIPE, text=True)
        stdout = proc.stdout

        return templates.TemplateResponse('confirm.html', {'request': request, 'index_url': index_url, 'stdout': stdout})
    except:
        return RedirectResponse(index_url)
