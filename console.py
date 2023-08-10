#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """command interpreter implements:
    quit, EOF, help, prompt"""
    prompt = "(hbnb)"

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_create(self, args):
        '''
         Creates a new instance of BaseModel
        '''
        if not args:
            print('** class name missing **')
            return
        elif args in ClassDict:
            for key, value in ClassDict.items():
                if key == args:
                    newInstance = ClassDict[key]()
            storage.save()
            print(newInstance.id)
        else:
            print("** Class dosen't exist**")

    def do_show(self, args):
        '''
        Prints the string representation of an instance based on the class name
        '''
        newInstance = args.partition(' ')
        class_name = newInstance[0]
        class_id = newInstance[2]

        if not args:
            print('** class name missing **')
            return
        if class_name not in ClassDict:
            print("** class doesn't exist **")
            return
        if not class_id:
            print('** instance id missing **')
            return
        new_key = class_name + '.' + class_id
        try:
            print(storage._FileStorage__objects[new_key])
        except BaseException:
            print("** no instance found **")

    def do_destroy(self, arg):
        '''
        Deletes an instance basesd on
        class name and id
        '''
        Newargs = ""
        className = ""
        class_id = ""
        try:
            Newargs = arg.split(" ")
            className = new_args[0]
            class_id = new_args[1]
        except BaseException:
            pass
        if not class_name:
            print('** class name missing **')
        elif className not in ClassDict:
            print("** class doesn't exist **")
        elif not class_id:
            print("** instance id missing **")
        else:
            new_key = className + '.' + class_id
            try:
                del(storage._FileStorage__objects[new_key])
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        new_list = []
        if arg:
            if arg not in Class_Dict:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if key.split(".")[0] == arg:
                    new_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                new_list.append(str(value))
        print(new_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
 