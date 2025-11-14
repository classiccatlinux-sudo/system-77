import time
import os

print("welcome to system-77 a simple way to cleen up multiple files!")
print("WARNING this program will delete files and folders permanently i am not responsible for any loss of data")
time.sleep(4)
os.system('clear')

names = input("enter name of folder(s) or files(s) to remove (enter done to stop): ")
folders = names.split()

for folder in folders:
    if folder != 'done':
        os.system(f'rm -rf "{folder}"')
print("all done!")



