import os
import shutil

print("폴더 예시 : C:/Users/개붕이/../")
path_dir_a = input("폴더 A의 주소 입력:")
path_dir_b = input("폴더 B의 주소 입력:")

file_list_a = os.listdir(path_dir_a)
file_list_b = os.listdir(path_dir_b)

for i in range(len(file_list_a)):
    file = file_list_a[i]
    name = file[0:file.find('.')]
    file_list_a[i] = name

for i in range(len(file_list_b)):
    file = file_list_b[i]
    name = file[0:file.find('.')]
    if name in file_list_a:
     shutil.move(path_dir_b + file, path_dir_a + file)

print(os.listdir(path_dir_a))
