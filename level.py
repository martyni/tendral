from numpy import array
import json


class Level(object):
   def __init__(self, size=array((100,100,100))):
      self.size = size
      self.characters = {}

   def add_character(self, name, start_location=array((0,0,0)), team=0):
      self.characters[name] = Character(name, start_location, team) 
      return self.return_characters()
      
   def return_characters(self):
      return json.dumps({char: self.characters[char].character_info() for char in self.characters})
   
   def update_character(self, name, movement):
      try:
         self.characters.get(name).update_location(movement)
         return self.return_characters()
      except:
         return self.return_characters()

class Character(object):
   
   def __init__(self, name, start_location, team):
      self.name = name
      self.start_location = start_location
      self.team = team
      self.location = array(self.start_location)
   
   def update_location(self, movement):
      self.location +=  movement


   def character_info(self):
      return {"team":self.team, "position": list(self.location)}

if __name__ == "__main__":
   name = "Keith"
   movement = (1,2,3)
   my_l = Level()
   my_l.add_character("Keith")
   print my_l.return_characters()
   print my_l.update_character(name, movement)
  
