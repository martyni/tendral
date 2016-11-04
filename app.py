from flask import Flask
from level import Level
import json
app = Flask(__name__)
level = Level()


def comma_split(string_):
   return [ arg for arg in string_.split(",")]

@app.route('/')
def show_level():
   return level.return_characters()

@app.route('/add/<character>')
def add_character(character):
   return level.add_character(character)

@app.route('/move/<character>/<movement>')
def move_character(character, movement):
   try:
      movement = [int(vector) for vector in  comma_split(movement)]
   except:
      pass
   return level.update_character(character, movement)



if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
