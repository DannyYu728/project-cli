from model import *
from playhouse.shortcuts import model_to_dict, dict_to_model

def help():
    print("python3 app.py view to see all the notes")
    print("python3 app.py create to creat a new note")
    
def view():
  for note in Note.select():
    print(model_to_dict(note))    
    
def create(title, notes):
  note = Note(title=f"{title}", notes=f"{notes}")
  note.save()