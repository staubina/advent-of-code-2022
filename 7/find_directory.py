class FileSystem:
    def __init__(self):
        self.current_location = 0
        self.root = Directory(name="/", parent=None)
        
class DataObject:
    def __init__(self, size, parent, name):
        self.size = size
        self.parent = parent
        self.name = name

class File(DataObject):
    def __init__(self, name, size, parent):
        DataObject.__init__(self, size, parent, name)

class Directory(DataObject):
    def __init__(self, name, parent):
        DataObject.__init__(self, size=0, parent=parent, name=name)
        self.files = []

    def get_total_size(self):
        total_size = 0
        if self.files:
            for file in self.files:
                if isinstance(file, File):
                    total_size += file.size
                else:
                    total_size += file.get_total_size()
        return total_size
    
    def get_directory(self, dir_name):
        if self.files:
            for file in self.files:
                if file.name == dir_name and isinstance(file, Directory):
                    return file
                elif isinstance(file, Directory):
                    return file.get_directory(dir_name)
        return None
            

def cd(file_system, current_dir, param):
    if param == "/":
        return file_system.root
    elif param == "..":
        return current_dir.parent if current_dir.parent else current_dir
    else:
        for file in current_dir.files:
            if file.name == param:
                return file

def ls(current_dir, input, line_idx):
    line_split = input[line_idx].split(" ")
    while line_split[0] != "$":
        if line_split[0] == "dir":
            current_dir.files.append(Directory(name=line_split[1], parent=current_dir))
        elif line_split[0].isdigit():
            current_dir.files.append(
                File(
                    size=int(line_split[0]),
                    name=line_split[1],
                    parent=current_dir
                )
            )
        
        line_idx = line_idx + 1
        if line_idx >= len(input):
            break
        line_split = input[line_idx].split(" ")
    return line_idx

def process_term_output(input):
    file_system = FileSystem()
    current_dir = file_system.root
    for line_idx in range(len(input)):
        line_split = input[line_idx].split(" ")
        if line_split[0] == '$':
            command = line_split[1]
            if command == "cd":
                param = line_split[2]
                current_dir = cd(file_system, current_dir, param)
            elif command == "ls":
                line_idx += 1
                line_idx = ls(current_dir, input, line_idx)
    return file_system

def compute_100k_dir_total(dir):
    dirs_less_than_100 = []
    if dir.files:
        for file in dir.files:
            if isinstance(file, Directory):
                if file.get_total_size() <= 100000:
                    # print(f'name: {file.name}, size: {file.get_total_size()}')
                    dirs_less_than_100.append(file)
                dirs_less_than_100.extend(compute_100k_dir_total(file))
    return dirs_less_than_100

def find_dir_to_remove(dir, space_needed):
    possible_dir_to_remove = []
    if dir.files:
        for file in dir.files:
            if isinstance(file, Directory):
                if file.get_total_size() >= space_needed:
                    print(f'name: {file.name}, size: {file.get_total_size()}')
                    possible_dir_to_remove.append(file)
                possible_dir_to_remove.extend(find_dir_to_remove(file, space_needed))
    return possible_dir_to_remove

def get_all_dir_sizes(dir):
    if dir.files:
        for file in dir.files:
            if isinstance(file, Directory):
                print(f'name: {file.name}, size: {file.get_total_size()}')
                get_all_dir_sizes(file)

input = open('input2.txt').read().split("\n")
file_system = process_term_output(input)
dir_list = compute_100k_dir_total(file_system.root)
result = 0
for dir in dir_list:
    result += dir.get_total_size()
print(result)

# Find Directory to delete
FILESYSTEM_MAX = 70000000
UPDATE_SPACE = 30000000
remaining_space = FILESYSTEM_MAX - file_system.root.get_total_size()
print(f'remaining: {remaining_space}')
space_needed = UPDATE_SPACE - remaining_space
print(f'space_needed: {space_needed}')
dirs_to_remove = find_dir_to_remove(file_system.root, space_needed)
print([(dir.name, dir.get_total_size()) for dir in dirs_to_remove])
smallest_dir_to_remove = min(dirs_to_remove, key= lambda file: file.get_total_size())
print(f'name: {smallest_dir_to_remove.name}, size: {smallest_dir_to_remove.get_total_size()}')