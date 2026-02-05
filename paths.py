import os
from pathlib import Path
#print(Path.cwd()) # print current path

# for p in Path().iterdir():
#     print(p)
#p = Path(__file__).resolve() sets p to the current file path

# print(my_file.steam) prints the file without the name extention

# print(new_file.name) returns the name of the file as a string 
# print(new_file.exixts()) returns if the new_file path exists
# print(new_file.parent) returns the file parent file path
# print(new_file.absolute()) returns the absolute path of the diretory

# searching in side a path

# for p in tempfiles.rglob("*read*", case_sensitive=False):
#     print(p) recursively search for a specific file

p = Path("Tempdir")
p.rmdir()