# The above class represents a simple file system with basic commands such as creating directories,
# navigating through directories, listing files and directories, searching for text in files, creating
# and reading files, moving and copying files, and deleting files and directories.
import os
import re

class FileSystem:
    def __init__(self):
        """
        The above function is the initialization method for a class that sets the current directory to the
        root directory and initializes an empty file system dictionary.
        """
        self.current_directory = "/"
        self.file_system = {}


    def run(self):
        """
        The function runs a command line interface that prompts the user for commands and executes them
        until the user enters "exit".
        """
        while True:
            command = input(self.current_directory + "> ")
            if command == "exit":
                break
            self.execute_command(command)


    def execute_command(self, command):
        """
        The `execute_command` function takes a command as input and executes the corresponding method based
        on the command name.
        
        :param command: The `command` parameter is a string that represents the command to be executed. It
        can contain multiple parts separated by spaces. The first part is the command name, and the
        remaining parts are the arguments for that command
        """
        command_parts = command.split(" ")
        command_name = command_parts[0]
        arguments = command_parts[1:]

        if command_name == "mkdir":
            self.mkdir(arguments)
        elif command_name == "cd":
            self.cd(arguments)
        elif command_name == "ls":
            self.ls(arguments)
        elif command_name == "grep":
            self.grep(arguments)
        elif command_name == "cat":
            self.cat(arguments)
        elif command_name == "touch":
            self.touch(arguments)
        elif command_name == "echo":
            self.echo(arguments)
        elif command_name == "mv":
            self.mv(arguments)
        elif command_name == "cp":
            self.cp(arguments)
        elif command_name == "rm":
            self.rm(arguments)
        else:
            print("Invalid command")



    def mkdir(self, arguments):
        """
        The `mkdir` function creates a new directory in the file system.
        
        :param arguments: The `arguments` parameter is a list that contains the arguments passed to the
        `mkdir` function. In this case, it is assumed that the first argument in the list is the name of the
        directory to be created
        """
        directory_name = arguments[0]
        path = self.get_absolute_path(directory_name)
        self.file_system[path] = {}



    def cd(self, arguments):
        """
        The `cd` function changes the current directory based on the given arguments.
        
        :param arguments: The `arguments` parameter is a list that contains the arguments passed to the `cd`
        function. In this case, it is assumed that the first argument in the list is the directory name that
        the user wants to change to
        """
        directory_name = arguments[0]
        if directory_name == "..":
            self.current_directory = os.path.dirname(self.current_directory)
        elif directory_name == "/":
            self.current_directory = "/"
        else:
            path = self.get_absolute_path(directory_name)
            if path in self.file_system and isinstance(self.file_system[path], dict):
                self.current_directory = path
            else:
                print("Directory not found")



    def ls(self, arguments):
        """
        The `ls` function lists the contents of a directory in a file system.
        
        :param arguments: A list of arguments passed to the `ls` function. These arguments represent the
        directory or directories for which the function should list the contents
        """
        if len(arguments) == 0:
            directory = self.current_directory
        else:
            directory_name = arguments[0]
            directory = self.get_absolute_path(directory_name)

        if directory in self.file_system and isinstance(self.file_system[directory], dict):
            print("\n".join(self.file_system[directory].keys()))
        else:
            print("Directory not found")



    def cat(self, arguments):
        """
        The `cat` function takes a file name as an argument, retrieves the absolute path of the file, and
        prints the contents of the file if it exists in the file system.
        
        :param arguments: The `arguments` parameter is a list that contains the arguments passed to the
        `cat` function. In this case, it is assumed that the first argument in the list is the file name
        """
        file_name = arguments[0]
        path = self.get_absolute_path(file_name)
        if path in self.file_system and isinstance(self.file_system[path], str):
            print(self.file_system[path])
        else:
            print("File not found")



    def touch(self, arguments):
        """
        The `touch` function creates an empty file with the given file name.
        
        :param arguments: A list of arguments passed to the `touch` method. The first argument is assumed to
        be the file name
        """
        file_name = arguments[0]
        path = self.get_absolute_path(file_name)
        self.file_system[path] = ""



    def echo(self, arguments):
        """
        The `echo` function takes a list of arguments, extracts the file name from the last argument, gets
        the absolute path of the file, joins the remaining arguments into a single string, and assigns the
        string as the value of the file in the file system dictionary.
        
        :param arguments: A list of arguments passed to the `echo` method. The last element of the list is
        assumed to be the file name, and the remaining elements are assumed to be the text to be written to
        the file
        """
        file_name = arguments[-1]
        path = self.get_absolute_path(file_name)
        text = " ".join(arguments[:-2])
        self.file_system[path] = text



    def mv(self, arguments):
        """
        The `mv` function moves a file from a source path to a destination path in a file system.
        
        :param arguments: The `arguments` parameter is a list that contains two elements. The first element
        is the source file or directory path, and the second element is the destination file or directory
        path
        """
        source = arguments[0]
        destination = arguments[1]
        source_path = self.get_absolute_path(source)
        destination_path = self.get_absolute_path(destination)
        if source_path in self.file_system:
            self.file_system[destination_path] = self.file_system.pop(source_path)
        else:
            print("Source not found")



    def cp(self, arguments):
        """
        The `cp` function copies a file from a source path to a destination path in a file system.
        
        :param arguments: The `arguments` parameter is a list that contains two elements. The first element
        is the source file or directory path, and the second element is the destination file or directory
        path
        """
        source = arguments[0]
        destination = arguments[1]
        source_path = self.get_absolute_path(source)
        destination_path = self.get_absolute_path(destination)
        if source_path in self.file_system:
            self.file_system[destination_path] = self.file_system[source_path]
        else:
            print("Source not found")



    def rm(self, arguments):
        """
        The `rm` function removes a file or directory from the file system.
        
        :param arguments: A list of arguments passed to the `rm` function. The first argument is the file or
        directory to be removed
        """
        file_or_directory = arguments[0]
        path = self.get_absolute_path(file_or_directory)
        if path in self.file_system:
            self.file_system.pop(path)
        else:
            print("File or directory not found")



    def get_absolute_path(self, path):
        """
        The function `get_absolute_path` returns the absolute path of a given file or directory.
        
        :param path: The `path` parameter is a string that represents a file or directory path
        :return: the absolute path of a given file or directory. If the path starts with "/", it is already
        an absolute path and is returned as is. Otherwise, the function joins the current directory with the
        given path using the os.path.join() function and returns the resulting absolute path.
        """
        if path.startswith("/"):
            return path
        else:
            return os.path.join(self.current_directory, path)


# The `if __name__ == "__main__":` block is used to ensure that the code inside it is only executed
# when the script is run directly, and not when it is imported as a module.
if __name__ == "__main__":
    file_system = FileSystem()
    file_system.run()
