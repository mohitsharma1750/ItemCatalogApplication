#!/usr/bin/python

#Flask Dependency Import
from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash, g
from flask import session as login_session

#SQL Alchemy Import
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

#Database Setup Import
from db_setup import Base, Categories, CategoryItem, User

#Utility Imports
from functools import wraps
import random
import string
import httplib2
import json
from flask import make_response
import requests

#Outh2 Dependencies Import
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError



app = Flask(__name__)
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Movie Catalog Application"

engine = create_engine('sqlite:///movie_catalogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()