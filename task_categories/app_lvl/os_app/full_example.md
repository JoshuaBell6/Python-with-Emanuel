This is a simulated OS app interraction

```
main> |
```

```
main> ls
.
main> |
```

```
main> test
'test' is not a command, use 'help' to see the list of available commands
main> |
```

```
main> help
Here is the list of commands you can use:
ls - displays all directories and files on the current directory level
cd - changes a current directory (syntax: cd {dirname})
mkdir - creates a new directory (syntax: mkdir {dirname})
touch - creates a new file (syntax: touch {filename})
mv - renames a file or a directory (syntax: mv {existing_name} {new_name})
rmdir - deletes an empty directory (syntax: rmdir {dirname})
rm - deletes a file or a directory along with its contents
q - exits the app
main> |
```

```
main> mkdir
'mkdir' requires an argument {dirname}; usage: mkdir {dirname}
main> |
```

```
main> mkdir test.^
'test.^' is an invalid directory name
main> |
```

```
main> mkdir mydir
'mydir' directory created successfuly
main> |
```

```
main> ls
/mydir
.
main> |
```

```
main> cd
main> |
```

```
main> cd mydir
mydir> |
```

```
mydir> ls
.
mydir> |
```

```
mydir> touch
'touch' requires an argument {filename}; usage: touch {filename}.{extension}
mydir> |
```

```
mydir> touch myfile
'touch' argument {filename} requires an extension; usage: touch {filename}.{extension}
mydir> |
```

```
mydir> touch myfilee.txt
'myfilee.txt' file created successfully
mydir> |
```

```
mydir> ls
myfilee.txt
.
mydir> |
```

```
mydir> mv
'mv' requires an argument {existing_name}; usage: mv {existing_name} {new_name}
mydir> |
```

```
mydir> mv test
'test' does not exist in this directory
mydir> |
```

```
mydir> mv myfilee
'mv' requires an argument {new_name}; usage: mv {existing_name} {new_name}
mydir> |
```

```
mydir> mv myfilee myfile
'myfilee' renamed to 'myfile'
mydir> |
```

```
mydir> ls
myfile.txt
.
mydir> |
```

```
mydir> cd test
'test' does not exist in this directory
mydir> |
```

```
mydir> cd .
mydir> |
```

```
mydir> cd ..
main> |
```

```
main> ls
/mydir
.
main> |
```

```
main> rmdir
'rmdir' requires an argument {dirname}; usage: rmdir {dirname}
main> |
```

```
main> rmdir test
'test' does not exist in this directory
main> |
```

```
main> rmdir mydir
'mydir' is not an empty directory
main> |
```

```
main> cd mydir
mydir> |
```

```
mydir> ls
myfile.txt
.
mydir> |
```

```
mydir> rmdir myfile.txt
'myfile.txt' is not a directory
mydir> |
```

```
mydir> rm
'rm' requires an argument {name}; usage: rm {name}
mydir> |
```

```
mydir> rm mydir
'mydir' is a current directory, navigate to the parent directory to delete it
mydir> |
```

```
mydir> rm test
'test' does not exist in this directory
mydir> |
```

```
mydir> rm myfile.txt
'myfile.txt' is deleted successfully
mydir> |
```

```
mydir> ls
.
mydir> |
```

```
mydir> cd ..
main> |
```

```
main> rmdir mydir
'mydir' is deleted successfully
main> |
```

```
main> ls
.
main> |
```

```
main> q
```
