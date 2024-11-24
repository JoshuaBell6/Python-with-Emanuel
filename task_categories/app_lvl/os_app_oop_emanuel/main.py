import json


class OS:
    def __init__(self):
        self.is_running = True

    def stop_app(self):
        self.is_running = False

    def display_help(self):
        print('''Here is the list of commands you can use:
ls - displays all directories and files on the current directory level
cd - changes a current directory (syntax: cd {dirname})
mkdir - creates a new directory (syntax: mkdir {dirname})
touch - creates a new file (syntax: touch {filename})
mv - renames a file or a directory (syntax: mv {existing_name} {new_name})
rmdir - deletes an empty directory (syntax: rmdir {dirname})
rm - deletes a file or a directory along with its contents
q - exits the app''')

    def display_arg_requirements(self, cmd):
        if cmd == 'mkdir':
            print(
                "'mkdir' requires an argument {dirname}; usage: mkdir {dirname}")
        elif cmd == 'touch':
            print(
                "'touch' requires an argument {filename}; usage: touch {filename}.{extension}")
        elif cmd == 'rm':
            print(
                "'rm' requires an argument {name}; usage: rm {name}")
        elif cmd == 'rmdir':
            print(
                "'rmdir' requires an argument {dirname}; usage: rmdir {dirname}")


class DirectoryManager:
    def __init__(self):
        self.main_dir = {
            'dirname': 'main',
            'parent_dir': None,
            'content': []
        }
        self.current_dir = self.main_dir
        self.savefile_path = './save_dir/savefile.json'

    def save_main_dir(self):
        with open(self.savefile_path, 'w') as file:
            json.dump(self.main_dir, file)

    def load_main_dir(self):
        try:
            with open(self.savefile_path, 'r') as file:
                self.main_dir = json.load(file)
                self.current_dir = self.main_dir
        except FileNotFoundError:
            return

    def display_current_dir_content(self):
        content: list[dict] = self.current_dir['content']
        if content:
            for i in content:
                key = 'dirname' if i.get('dirname') else 'filename'
                print(f"/{i[key]}" if key ==
                      'dirname' else f"{i[key]}.{i['extension']}")
        print('.')

    def add_file(self, filename: str, extension: str):
        content: list = self.current_dir['content']
        content.append({
            'filename': filename,
            'extension': extension,
            'parent_dir': self.current_dir['dirname']
        })
        print(f"'{filename}.{extension}' file created successfully")

    def add_dir(self, dirname: str):
        content: list = self.current_dir['content']
        content.append({
            'dirname': dirname,
            'parent_dir': self.current_dir['dirname'],
            'content': []
        })
        print(f"'{dirname}' directory created successfuly")

    def rename_file_or_dir(self, old_name: str, new_name: str):
        content: list[dict] = self.current_dir['content']
        for i in content:
            key = 'dirname' if i.get('dirname') else 'filename'
            if i[key] == old_name:
                i[key] = new_name
                self._update_parent_dir(i, new_name)
                print(f"'{old_name}' renamed to '{new_name}'")
                return
        print(f"'{old_name}' does not exist in this directory")

    def delete_file_or_dir(self, name: str, force_delete: bool, dir_only: bool = False):
        content: list[dict] = self.current_dir['content']
        if not content:
            print(f"'{name}' is not a directory")
            return
        for i in content:
            key = 'dirname' if i.get('dirname') else 'filename'
            if i[key] == name:
                if not force_delete and i.get('content'):
                    print(f"'{name}' is not an empty directory")
                    return
                if dir_only and key == 'filename':
                    print(f"'{name}' is not a directory")
                    return
                content.remove(i)
                print(f"'{name}' is deleted successfully")
                return
        print(f"'{name}' does not exist in this directory")

    def set_current_dir(self, dirname: str):
        content: list[dict] = self.current_dir['content']
        for i in content:
            if i.get('dirname') == dirname:
                self.current_dir = i
                return
        print(f"'{dirname}' does not exist in this directory")

    def set_parent_dir_as_current(self):
        if self.current_dir['dirname'] == 'main':
            return
        if self.current_dir['parent_dir'] == 'main':
            self.current_dir = self.main_dir
        self._find_parent_dir(self.main_dir['content'])

    def _find_parent_dir(self, content: list[dict]):
        if not content:
            return
        for i in content:
            key = 'dirname' if i.get('dirname') else 'filename'
            if i[key] == self.current_dir['parent_dir']:
                self.current_dir = i
                return
            self._find_parent_dir(i['content'])

    def _update_parent_dir(self, dir: dict, parent_dirname: str):
        content: list[dict] = self.current_dir['content']
        if not content:
            return
        for i in content:
            if not i.get('dirname') or i['dirname'] != dir['dirname']:
                continue
            for j in i['content']:
                j['parent_dir'] = parent_dirname
        print(self.main_dir)


def _requires_one_argument(args: list[str]):
    return not args or not args[0] or len(args) > 1


def run_mkdir_command(arguments: list[str]):
    if _requires_one_argument(arguments):
        os.display_arg_requirements('mkdir')
        return
    dirname: str = arguments[0]
    m.add_dir(dirname)


def run_cd_command(arguments: list[str]):
    target_dir: str = arguments[0]
    if _requires_one_argument(arguments) or target_dir == '.':
        return
    if target_dir == '..':
        m.set_parent_dir_as_current()
        return
    m.set_current_dir(target_dir)


def run_touch_command(arguments: list[str]):
    if _requires_one_argument(arguments):
        os.display_arg_requirements('touch')
        return
    file_elements: list[str] = arguments[0].rsplit('.', 1)
    if len(file_elements) < 2:
        print(
            "'touch' argument {filename} requires an extension; usage: touch {filename}.{extension}")
        return
    filename = file_elements[0]
    extension = file_elements[-1]
    m.add_file(filename, extension)


def run_mv_command(arguments: list[str]):
    if not arguments or not arguments[0]:
        print(
            "'mv' requires an argument {existing_name}; usage: mv {existing_name} {new_name}")
        return
    if len(arguments) < 2:
        print(
            "'mv' requires an argument {new_name}; usage: mv {existing_name} {new_name}")
        return
    m.rename_file_or_dir(arguments[0], arguments[1])


def run_rm_command(arguments: list[str]):
    if not _requires_one_argument(arguments):
        os.display_arg_requirements('rm')
        return
    m.delete_file_or_dir(arguments[0], force_delete=True)


def run_rmdir_command(arguments: list[str]):
    if not _requires_one_argument(arguments):
        os.display_arg_requirements('rmdir')
        return
    m.delete_file_or_dir(arguments[0], force_delete=False, dir_only=True)


def handle_command(cmd: str, input: str):
    args: list[str] = input[len(cmd)+1:].split(' ')
    if cmd.strip() == '':
        return
    if cmd == 'help':
        os.display_help()
    elif cmd == 'ls':
        m.display_current_dir_content()
    elif cmd == 'mkdir':
        run_mkdir_command(args)
    elif cmd == 'cd':
        run_cd_command(args)
    elif cmd == 'touch':
        run_touch_command(args)
    elif cmd == 'mv':
        run_mv_command(args)
    elif cmd == 'rm':
        run_rm_command(args)
    elif cmd == 'rmdir':
        run_rmdir_command(args)
    elif cmd == 'q':
        os.stop_app()
    else:
        print(
            f"'{cmd}' is not a command, use 'help' to see the list of available commands")


def handle_input(input: str):
    cmd = input.split(' ')[0]
    handle_command(cmd, input)


m = DirectoryManager()
os = OS()

m.load_main_dir()

while os.is_running:
    command = input(f'{m.current_dir['dirname']}> ')
    handle_input(command)

m.save_main_dir()
