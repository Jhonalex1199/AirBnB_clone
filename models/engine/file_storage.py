#!/usr/bin/python3
""" Import the modules need it for this storage """




"""Future models to import in the project"""


class FileStorage:
 """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

 __file_path = "file.json"
 __objects = {}



 def all(self):
  """ public instance return dictionary """
  return FileStorage.__objects


  def new(self, obj):
   """ public instance that sets in __objects """
   FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

   def save(self):
    """ Public instance that serializes __objects """
    new_dict = {}
    for key, value in FileStorage.__objects.items():
     new_dict[key] = value.to_dict()

     def reload(self):
      """ Public instance that deserializes JSON to object """
      try:
       with open(FileStorage.__file_path, 'r', encoding="UTF-8") as file:
        list_data = json.load(file)
        for key, value in list_data.items():
         FileStorage.__objects[key] = eval(
          value['__class__'])(**value)
         # State(**vale)
        except Exception:
         pass
