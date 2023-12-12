# Assessment
This code implements an in-memory file system in Python. It provides functionalities similar to a terminal, allowing you to create directories, navigate through directories, list directory contents, create files, display file contents, move files or directories, copy files or directories, and remove files or directories.

To use the file system, simply run the code. It will start an infinite loop where you can enter commands. The current directory is displayed as a prompt, and you can enter commands like mkdir, cd, ls, grep, cat, touch, echo, mv, cp, and rm followed by the necessary arguments.

For example, 
to create a new directory, you can use the mkdir command followed by the directory name:
mkdir new_directory

To change the current directory, you can use the cd command followed by the directory name:
cd new_directory

To list the contents of the current directory or a specified directory, you can use the ls command:
ls
ls directory_name

To display the contents of a file, you can use the cat command followed by the file name:
cat file_name

To create a new empty file, you can use the touch command followed by the file name:
touch new_file.txt

To write text to a file, you can use the echo command followed by the text and the file name:
echo 'This is some text' > file.txt

To move a file or directory to another location, you can use the mv command followed by the source and destination paths:
mv source_path destination_path

To copy a file or directory to another location, you can use the cp command followed by the source and destination paths:
cp source_path destination_path

To remove a file or directory, you can use the rm command followed by the file or directory name:
rm file_or_directory

# For run the code 
simply run the assessment.py in vs code 
give the .txt file path 
