"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgro9m02qv2dcb8nshcg-a.oregon-postgres.render.com",
        database="todoapp_m067",
        user="todoapp_m067_user",
        password="MxKAPVkkCJIrA8H1WlTmw5bx9GZxVxj1")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
