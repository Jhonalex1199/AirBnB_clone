# AirBnB_clone

<h3> This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration… </h3>

<h2> How to use it </h2>
<ul>
<li>[AUTHORS]- list of contributors</li>
<li>[console.py] - command interpreter
<ul>
<li><code>do_create</code> - create a new instance of a class</li>
<li><code>do_show</code> - prints string representation of an instance based on class name and id</li>
<li><code>do_all</code> - prints all string representation of all instances based or not on the class name</li>
<li><code>do_destroy</code> - deletes an instance based on the class name and id</li>
<li><code>do_update</code> - updates an instance based on the class name and id by adding or updating attribute</li>
<li><code>emptyline</code> - ensures that hitting 'enter' will not remember the last command</li>
<li><code>do_quit</code> - quit program</li>
<li><code>do_EOF</code> - exit at end of file</li>
</ul>
</li>
<li>[file_storage.py] - class FileStorage
<ul>
<li><code>all</code> - returns the dictionary __objects</li>
<li><code>new</code> - sets in __objects the obj with key .id</li>
<li><code>save</code> - serializes __objects to the JSON file (path: __file_path)</li>
<li><code>reload</code> - deserializes the JSON file to __objects</li>
</ul>
</li>
<li>[base_model.py]- parent class that will take care of initialization/serialization/deserialization of future instances
<ul>
<li><code>__init__</code> - initialize instance attributes</li>
<li><code>__str__</code> - creates formatted string representation of instance</li>
<li><code>__repr__</code> - returns string representation of instance</li>
<li><code>save</code> - updates public instance attribute updated_at with current datetime</li>
<li><code>to_dict</code> - creates a dictionary containing all keys/values of <code>__dict__</code> of the instance</li>
</ul>
</li>
</ul>

<h2> examples </h3>
<pre>
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
</pre>
