from flask import flash
from models import users
import hashlib

def getAllUsers():
    dataUsers = users.getAllUsers()
    
    return dataUsers