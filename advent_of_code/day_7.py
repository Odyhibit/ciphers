from collections import defaultdict


def get_dirs(dir_path: str) -> []:
    output = [dir_path]
    while len(dir_path) > 3 or dir_path == "/":
        end = dir_path.rfind("/")
        dir_path = dir_path[:end]
        output.append(dir_path)
    # print(output)
    return output


def add_or_create(dictionary: {}, filename: tuple, amount: int):
    if filename in dictionary:
        dictionary[filename] += amount
    else:
        dictionary[filename] = amount


cur_dir = ""
dir_dict = {"/": 0}
with open("input/day_7.txt", "r") as inputs:
    for line in inputs:
        if "$ cd .." in line:
            cur_dir = cur_dir[:cur_dir.rfind("/")]
        elif "$ cd" in line and "/" not in line:
            cur_dir += "/" + line[5:].strip("\n")
        elif "$" not in line and "dir" not in line:
            size, file_name = line.strip("\n").split(" ")
            dir_list = get_dirs(cur_dir)
            dir_dict["/"] += int(size)
            for this_dir in dir_list:
                add_or_create(dir_dict, this_dir, int(size))
print(dir_dict)
print(sum(size for size in dir_dict.values() if size <= 100000))
total_disk_space = 70000000
required_space = 30000000
used_space = dir_dict["/"]
min_size = required_space - (total_disk_space - used_space)
print(min(size for size in dir_dict.values() if size >= min_size))

'''
lines = map(str.split, open('day_7.txt').read().splitlines())
path, dirs = [], defaultdict(int)

for l in lines:
    if l[0] == "$":
        if l[1] == "cd":
            if l[2] == "..":
                path.pop()
            else:
                path.append(l[2])
    elif l[0] != "dir":
        for i in range(len(path)):
            dirs[tuple(path[: i + 1])] += int(l[0])

print(sum(size for size in dirs.values() if size <= 100000))

required = 30000000 - (70000000 - dirs[("/",)])

print(min(size for size in dirs.values() if size >= required))
print(f"correct {len(dirs)} mine {len(dir_dict)}")
print(dirs)
print(dir_dict["/"])
'''