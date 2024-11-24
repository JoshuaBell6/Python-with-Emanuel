## Bugs:

- '?' and 'key' commands are your debug commands and should not be executable by users

### 'mkdir' command

- adding an extra argument after a required one crashes the program

### 'touch' command

- adding as many dots in the extension is allowed, should be restricted to only one

### 'mv' command

- successful 'mv' command displays the success message twice
- if the file/directory doesn't exist, displays an error and then success message
- renaming a file with multiple dots in its name creates a new one instead despite saying its renamed

### Other

- Make sure to have a dedicated folder where you store a save file

## Code review

```py
# return list of strings until dot, even without dot
def remove_after_dot_list(input_data):
    def process_string(s):
        parts = s.split('.', 1)  # Split at most once
        return parts[0] if len(parts) > 1 else s

    if isinstance(input_data, str):
        return process_string(input_data)
    elif isinstance(input_data, list):
        return [process_string(item) for item in input_data]
    else:
        raise TypeError("Input must be a string or a list of strings")
```

Use of method inside of a method is highly unencouraged as it adds complexity to readability and limits its scope to just its parent method

```py
# returns True if the word ends with a valid extension
def ends_with_extension(word):
    valid_extensions = {'.txt', '.text', '.md'}  # set of allowed extensions
    return any(word.lower().endswith(ext) for ext in valid_extensions)
```

Very poor set of allowed extensions, better to not put any at all, or add an acceptable char length as a limit

```py
if len(rest) == 0 or one_word == '.':
    pass
```

'pass' is a placeholder keyword used on an empty method for a time the developer is not sure what to write inside. Using it in the actual program logic is redundant.
Whatever code block the 'pass' keyword is in, becomes obsolete.

```py
something = dict_to_list(deleted)
directories = transform_list(something)
```

Never name variables like this, you will confuse anyone trying to understand that code and, if you don't look at it for weeks, yourself.

All in all, the code is unreadable, if you had 15 minutes to explain it to someone else, could you do it?
Best solution for this task was OOP. It can be done without it as well, but its very difficult to keep the code organized and not introduce high complexity and potential readability issue.
