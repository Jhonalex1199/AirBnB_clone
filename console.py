#!/usr/bin/python3
"""Console"""
import json
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Command args main module """
    classes = ['BaseModel', 'User', 'City', 'State\
                ', 'Place', 'Amenity', 'Review']
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit coomand args"""
        return True

    def emptyline(self):
        """ Empty args """
        pass

    def do_EOF(self, args):
        """ EOF - press C^d to quit commnad args """
        print("")
        return True

    def do_create(self, args):
        """ Create a new instance
        Usage:
        1 - create <class name>
        """
        if not args:
            print("** class name missing **")
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args)()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, args):
        '''Print the object with id specified and his dictionary'''
        new_list = args.split()
        if not args:
            print("** class name missing **")
        elif new_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(new_list) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = new_list[0] + '.' + new_list[1]
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """ Destroy an instance.
        Usage :
        1 - destroy <class> <id>
        2 - <class name>.destroy("<id>")
        """
        commands = args.split()
        if len(commands) < 1:
            print("** class name missing **")
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            key_to_validate = "{}.{}".format(commands[0], commands[1])
            instances = storage.all()
            if key_to_validate not in instances:
                print("** no instance found **")
            else:
                del instances[key_to_validate]
                storage.save()

    def do_update(self, args):
        """update an instance.
        Usage :
        1 - update <class name> <id> <attribute name> "<attribute value>
        2 - <class name>.update(<id>, <attribute name>, <attribute value>)
        3 - <class name>.update(<id>, <dictionary representation>)
        """
        if len(args) < 1:
            print("** class name missing **")
        else:
            comds = args.split()
            if comds[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(comds) < 2:
                print('** instance id missing **')
            else:
                instances = storage.all()
                key = "{}.{}".format(comds[0], comds[1])
                if key not in instances:
                    print("** no instance found **")
                if len(comds) < 3:
                    print("** attribute name missing **")
                elif len(comds) < 4:
                    print("** value missing **")
                else:
                    for key_id, obj in instances.items():
                        if key == key_id:
                            value = comds[3].split("\"")
                            if len(value) > 1:
                                value = value[1]
                            else:
                                value = comds[3]
                            if hasattr(obj, comds[2]):
                                value = type(
                                    getattr(obj, comds[2]))(value)
                            elif value.isdigit() is True:
                                value = int(value)
                            setattr(obj, comds[2], value)
                            storage.all()[key_id].save()

    def do_all(self, args):
        """ Print all instances.
        Usage:
        1 - all <class name>
        2 - all
        3 - <class name>.all()
        """
        if args not in self.classes and len(args) > 0:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            list_instances = []
            for key_id in instances.keys():
                key = key_id.split('.')
                if len(args) < 1:
                    list_instances.append(str(instances[key_id]))
                elif key[0] == args:
                    list_instances.append(str(instances[key_id]))
            print(list_instances)

    def default(self, args):
        """
        Retrieve all instances of a class by using: <class name>.all().
        """
        if '.' not in args:
            print("*** Unknown syntax: " + args)
            return
        No_commands = {"all()": self.do_all, "count()": self.do_count}
        args = args.split(".")
        if args[0] not in self.classes:
            print("*** Unknown syntax: " + args)
        elif len(args) != 2:
            print("*** Unknown syntax: " + args)
        else:
            if args[1] in No_commands:
                No_commands[args[1]](args[0])

    def do_count(self, arg):
        """
        to retrieve the number of instances of a class: <class name>.count().
        """
        None_count = 0
        all_objs = storage.all()
        for key, obj in all_objs.items():
            if arg in obj.__str__():
                None_count += 1
        print(None_count)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
