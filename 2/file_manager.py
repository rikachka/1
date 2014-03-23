import os
import shutil
while True:
	arr = input().split()
	if arr[0] == 'create_folder':
		os.mkdir(arr[1])
	if arr[0] == 'delete_folder':
		os.rmtree(arr[1])
	if arr[0] == 'remove_folder':
		shutil.move(arr[1], arr[2])
	if arr[0] == 'copy_folder':
		shutil.copytree(arr[1], arr[2])
	if arr[0] == 'create_file':
		f = open(arr[1], 'w')
		f.close()
	if arr[0] == 'delete_file':
		os.remove(arr[1])
	if arr[0] == 'remove_file':
		shutil.move(arr[1], arr[2])
	if arr[0] == 'copy_file':
		shutil.copy(arr[1], arr[2])
