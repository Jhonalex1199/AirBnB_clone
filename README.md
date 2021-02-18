# AirBnB_clone

<h3> This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… </h3>

<h2> How to use it </h2>
[AUTHORS]- list of contributors
[console.py] - command interpreter
do_create - create a new instance of a class
do_show - prints string representation of an instance based on class name and id
do_all - prints all string representation of all instances based or not on the class name
do_destroy - deletes an instance based on the class name and id
do_update - updates an instance based on the class name and id by adding or updating attribute
emptyline - ensures that hitting 'enter' will not remember the last command
do_quit - quit program
do_EOF - exit at end of file
[file_storage.py] - class FileStorage
all - returns the dictionary __objects
new - sets in __objects the obj with key .id
save - serializes __objects to the JSON file (path: __file_path)
reload - deserializes the JSON file to __objects
[base_model.py]- parent class that will take care of initialization/serialization/deserialization of future instances
__init__ - initialize instance attributes
__str__ - creates formatted string representation of instance
__repr__ - returns string representation of instance
save - updates public instance attribute updated_at with current datetime
to_dict - creates a dictionary containing all keys/values of __dict__ of the instance
<h2> examples </h3>
<code>
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$</code>