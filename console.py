#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Class dictionary for the available classes
ClassDict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
}

class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing instances"""

    # Set the command prompt
    prompt = "(hbnb) "

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        return True

    def do_create(self, args):
        """Create a new instance of a class and save it to storage"""
        if not args:
            print('** class name missing **')
            return
        class_name = args
        if class_name in ClassDict:
            newInstance = ClassDict[class_name]()
            newInstance.save()
            print(newInstance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Print the string representation of an instance"""
        if not args:
            print('** class name missing **')
            return
        newInstance = args.split()
        class_name = newInstance[0]
        if class_name not in ClassDict:
            print("** class doesn't exist **")
            return
        if len(newInstance) < 2:
            print('** instance id missing **')
            return
        class_id = newInstance[1]
        instance_key = "{}.{}".format(class_name, class_id)
        if instance_key in storage.all():
            print(storage.all()[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance based on class name and id"""
        if not args:
            print('** class name missing **')
            return
        new_args = args.split()
        class_name = new_args[0]
        if class_name not in ClassDict:
            print("** class doesn't exist **")
            return
        if len(new_args) < 2:
            print("** instance id missing **")
            return
        class_id = new_args[1]
        instance_key = "{}.{}".format(class_name, class_id)
        if instance_key in storage.all():
            del storage.all()[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Print all string representations of instances"""
        if args and args not in ClassDict:
            print("** class doesn't exist **")
            return
        new_list = []
        #for key, value in storage.all().items():
            #if not args or key.split(".")[0] == args:
                # new_list.append(str(value))
        storage_list = storage.all()
        for instance in storage_list:
            print("first item: {}".format(storage_list[instance]))
            if args == instance:
                new_list.append(str(instance))
                print(new_list)

    def do_update(self, args):
        """Update an instance attribute and save the change"""
        new_args = args.split()
        if not new_args:
            print("** class name missing **")
            return
        class_name = new_args[0]
        if class_name not in ClassDict:
            print("** class doesn't exist **")
            return
        if len(new_args) < 2:
            print("** instance id missing **")
            return
        obj_id = new_args[1]
        if "{}.{}".format(class_name, obj_id) not in storage.all():
            print("** no instance found **")
            return
        if len(new_args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = new_args[2]
        if len(new_args) < 4:
            print("** value missing **")
            return
        attribute_value = new_args[3]
        instance = storage.all()["{}.{}".format(class_name, obj_id)]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

