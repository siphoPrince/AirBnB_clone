#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

