import tarfile
import os 
import shutil
from pathlib import Path
from datetime import datetime
import fnmatch
import glob
# from tempfile import TemporaryFile 
import zipfile
import fileinput
import sys



print(help(shutil))

with open('data.txt', 'w') as f:
    data = "Python has several built-in modules and functions for handling files. These functions are spread out over several modules such as os, os.path, shutil, and pathlib, to name a few."
    data = f.write(data)

with open('./data.txt', 'r') as f:
    data = f.read()
print(data)

##########################
###  list directories  ###
##########################

my_directory = r'C:\Users\p114215\Documents\Internship'

### using os.listdir()

directories = os.listdir(my_directory)
for directory in directories:
    print(directory)
print('-----'*15)
print(directories)

### Directoy listening in modern python version ###
### using os.scandir()

entities = os.scandir(my_directory)
print(entities)

with os.scandir(my_directory) as entities:
    for entity in entities:
        print(entity.name)

## using pathlib
entities = Path(my_directory)
for entity in entities.iterdir():
    print(entity.name)

## another version of the code above 
with Path(my_directory) as entities:
    for entity in entities.iterdir():
        print(entity.name)


##############################################
####  Listing all files in a directory   #####
##############################################

my_directory = r'C:\Users\p114215\Documents\Internship\coding'

for entity in os.listdir(my_directory):
    if os.path.isfile(os.path.join(my_directory, entity)):
        print(entity)

with os.scandir(my_directory) as entities:
    for entity in entities:
        if entity.is_file():
            print(entity.name)

my_directory = Path(my_directory)
files_in_my_directory = my_directory.iterdir()
for item in files_in_my_directory:
    if item.is_file():
        print(item.name)

## the same code with a generator expression
file_in_my_directory = (entity for entity in my_directory.iterdir() if entity.is_file())
for item in file_in_my_directory:
    print(item.name)

#######################################################
####  Listing all subdirectories in a directory   #####
#######################################################
## using os
my_directory = r'C:\Users\p114215\Documents'
for entities in os.listdir(my_directory):
    if os.path.isdir(os.path.join(my_directory, entities)):
        print(entities)

### using scandir
with os.scandir(my_directory) as entities:
    for entity in entities:
        if entity.is_dir():
            print(entity.name)

# # using pathlib
my_directory = Path(my_directory)
directories_in_my_directory = (entity for entity in my_directory.iterdir() if entity.is_dir())
for item in directories_in_my_directory:
    print(item.name)

#######################################################
####            Getting files attributes          #####
#######################################################

# # using scandir to see the time of last modification of the item 
with os.scandir(my_directory) as entities:
    for entity in entities:
        info = entity.stat()
        print(entity.name, info.st_mtime)

## using pathlib to see the time of last modification of the item
my_directory = Path(my_directory)
items_in_my_directory = (items for items in my_directory.iterdir())
for item in items_in_my_directory:
    info = item.stat()
    print(item.name, info.st_mtime)


####  Getting files attributes: Time in second since epochs  #####

## converting time
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def get_files():
    dir_items = os.scandir(my_directory)
    for item in dir_items:
        if not item.is_file():
            info = item.stat()
            print(f'{item.name}\t Last Modified: {convert_date(info.st_mtime)}') 
print(get_files())
 

#######################################################
####             Creating Directories             #####
#######################################################

### Single directory
os.mkdir('SQL and Python')

# # with pathlib
my_directory = r'C:\Users\p114215\Documents\Internship' 
p=Path(my_directory)
try:
    p.mkdir()
except FileExistsError as exc:
    print(exc)

romax_dir = r'C:\Users\p114215\Documents\Internship\coding\ROMAX\BDD'  # see line 295
p = Path(romax_dir)
p.mkdir(parents=True)

## another code to deal with exceptions
p.mkdir(exist_ok=True)

### Multiple directory
os.makedirs('../ROMAX/Excel Files', mode=0o770)

#### with pathlib
p = Path('/ROMAX/Excel Files')
p.mkdir(parents=True)


#######################################################
####         Filename pattern matching            #####
#######################################################

my_directory = r'C:\Users\p114215\Downloads'

# ## Get .xlsx or .pdf files using "endswith"
for file_name in os.listdir(my_directory):
    if file_name.endswith('.xlsx'):
    # if file_name.endswith('.pdf'):
        print(file_name)

### Get .xlsx or .pdf files using "fnmatch"
for file_name in os.listdir(my_directory):
    if fnmatch.fnmatch(file_name, '*.pdf'):
        print(file_name)

# #### Advanced Pattern matching 
for filename in os.listdir(my_directory):
    if fnmatch.fnmatch(filename, '*vehicle*'):
        print(filename)


# #### File Pattern matching using glob ####
py_files_in_repo = glob.glob('*.py')
for file in py_files_in_repo:
    print(file)

for name in glob.glob('*[A-Z]*.txt'):
    print(name)

# ##### Recursive search with glob
for file in glob.iglob('**/*.py', recursive=True):
    print(file)

# #### with pathlib
p = Path(r'C:\Users\p114215\Downloads')
for name in p.glob('*[A-C]*.pdf'):
    print(name.name) 



#######################################################
####     Traversing and processing directories    #####
#######################################################
my_directory=r'C:\Users\p114215\Documents\Internship\coding'

for dirpath, dirnames, files in os.walk(my_directory):
    print(f'Found directory: {dirpath}')
    for file in files:
        print(file)

for dirpath, dirnames, files in os.walk(my_directory, topdown=False):
    print(f'Found directory: {dirpath}')
    for file in files:
        print(file)

print(os.getcwd())
print(help(os.walk))
for root, dirs, files in os.walk(os.getcwd()):
    print('current path: ', root)
    print('Directories: ', dirs)
    print('Files: ', files)
    print()


# ####----x     Looking for empty directories in a certain path    x----#####
my_dir = r'C:\Users\p114215\Documents\Internship\coding\ROMAX project\ROMAX\BDD'
empty = []
for roots, dirs, files in os.walk(my_dir):
    if not len(dirs) and not len(files):
        empty.append(roots)

print(empty)


#######################################################
####     Deleting files and directories          #####
#######################################################

####     Deleting files      #####
    # os.remove(), os.unlink() or pathlib.Path.unlink()#
## os.remove()
file_to_delete = r'C:\Users\p114215\Documents\Internship\coding\Excel and Python\xxx.xlsx'
# os.remove(file_to_delete)

## os.unlink()
os.unlink(file_to_delete)

## check if the file in directory
if os.path.isfile(file_to_delete):
    os.remove(file_to_delete)
else:
    print(f'Error: \'{file_to_delete}\' not a valid filename')

# ## use exception handling
try:
    os.remove(file_to_delete)
except OSError as e:
    print(f'Error: {file_to_delete} : {e.strerror}')

# ## pathlib
file_to_delete = Path(file_to_delete)
try:
    file_to_delete.unlink()
except FileNotFoundError as e:
    print(f'Error: {file_to_delete}: {e.strerror}')


####     Deleting directories      #####
    # os.rmdir(), pathlib.Path.rmdir() or shutil.rmtree() #

# ## os.rmdir()
dir_to_delete = r'C:\Users\p114215\Documents\Internship\coding\Path Python\my_directory\ROMAX\Excel Files'

try:
    os.rmdir(dir_to_delete)
except OSError as e:
    print(f'Error {dir_to_delete}: {e.strerror}')

## pathlib.Path.rmdir()
dir_to_delete = Path(dir_to_delete)

try:
    Path.rmdir(dir_to_delete)
except OSError as e:
    print(f'Error: {dir_to_delete} : {e.strerror}')

### Deleting the entire directory trees using shutil.rmtree
dir_to_delete_tree = r'C:\Users\p114215\Documents\Internship\coding\Path Python\my_directory'

try:
    shutil.rmtree(dir_to_delete_tree)
except OSError as e:
    print(f'Error: {dir_to_delete_tree} : {e.strerror}')

### Deleting the entire directory trees using os.walk
for dirpath, dirnames, files in os.walk(dir_to_delete_tree):
    try:
        os.rmdir(dirpath)
    # except OSError as ex:
    except:
        pass 

####################################################################
####    Copying, Moving, and Renaming files and Directories    #####
####################################################################

####    Copying files  #####
src = r'C:\Users\p114215\Alliance\DEA-MKN Stage Data Analyst - General\BDD_ROMAX'
dst = r'C:\Users\p114215\Documents\Internship\coding\ROMAX\BDD'
shutil.copy(src, dst) # copy only a file (without its information --contents and permision)

## using of copy2 to preserve metadata
src =  r'C:\Users\p114215\Documents\Internship\reading\Modus Vivendi\Convention-Dicken.pdf'
dst = r'C:\Users\p114215\Documents\Internship\coding\ROMAX\BDD'  # see line 146
shutil.copy2(src, dst)  # copy a file and its information

### Copying Directories  ####
src = r'C:\Users\p114215\Documents\Internship\reading\Modus Vivendi'
dst = r'C:\Users\p114215\Videos\Essai'  # the destination dir must not already exist
shutil.copytree(src, dst)

####    Moving files and Directories    #####
# src = r'C:\Users\p114215\Documents\Internship\reading\Projets'
src = r'C:\Users\p114215\Documents\Internship\coding\Path Python\Modus Vivendi'
dst = r'C:\Users\p114215\Documents\Internship\coding\ROMAX\BDD'
shutil.move(src, dst)

####    Renaming files and Directories    #####
first_name_dir = r'C:\Users\p114215\Documents\Internship\coding\ROMAX\BDD\Modus Vivendi'
second_name_dir = r'C:\Users\p114215\Documents\Internship\coding\ROMAX\BDD\Mode de vie' 
# os.rename(first_name_dir, second_name_dir)

data_dir = Path(second_name_dir) #define the path
try:
    data_dir.rename(first_name_dir)
except FileNotFoundError as e:
    print(f'{e} The is nothing found in \"{data_dir.name}\", your source directory')


##################################
####      Archiving files    #####
##################################

####    Reading zip files    #####

get_my_file = r'C:\Users\p114215\Documents\Internship\coding\ROMAX.zip'
unzip_dst = r'C:\Users\p114215\Documents\Internship\coding'

#getting all files in the zipfile object
with zipfile.ZipFile(get_my_file, 'r') as zipobj:
    print(zipobj.namelist())


#### getting info in the file ####
my_file = r'ROMAX/BDD/Projets/Romax.docx'
with zipfile.ZipFile(get_my_file, 'r') as zipobj:
    bar_info = zipobj.getinfo(my_file) # a directory in a zip file
    print(f'filename : {bar_info.filename}') #full path
    print(f'file size : {bar_info.file_size}')  
    print(f'compress size : {bar_info.compress_size}')
    print(f'date time : {bar_info.date_time}') #last modification date  

### extracting ZIP archives ####

# all files in the zip file
data_zip = zipfile.ZipFile(get_my_file, 'r')
data_zip.extractall(path=unzip_dst) # exctract all files into
                                    # a different directory
data_zip.close()

#the equivalence of the code above
with zipfile.ZipFile(get_my_file, 'r') as data_zip:
    data_zip.extractall(path=unzip_dst)

print(os.listdir())

## single file
file_zip_dir = r'C:\Users\p114215\Documents\Internship\coding\zip_file.zip'
file_list = ['file.txt', 'income.xlsx']
with zipfile.ZipFile(file_zip_dir, 'r') as file_in_zip_dir:
    for file in file_list:
        file_in_zip_dir.extract(file) # extract only one file a time

###    creating ZIP archives    #####
with zipfile.ZipFile('zip_file.zip', 'w') as zip_file:
    for file in file_list:
        zip_file.write(file)


#### opening TAR archives ####
with tarfile.open('file.tar', 'r') as tar_file:
    print(tar_file.getnames())

tar = tarfile.open('file.tar', mode='r')
print(tar.getnames())

# #### an easier way of creating archives ####
src_dir = r'C:\Users\p114215\Documents\Internship\coding\ROMAX\BDD\Modus da Vivendi'
dst_dir = r'C:\Users\p114215\Documents\Internship\coding\Path Python' # the same elt is the name of the final directory
shutil.make_archive(dst_dir, 'zip', dst_dir)


###########################################
###     Reading multiple files        #####
###########################################

# to run this code below, use terminal
# Here is the command: $python '.\Path Python\dir_scripts.py' .\file.txt '.\Path Python\data.txt'
files = fileinput.input()
for line in files:
    if fileinput.isfirstline():
        print(f'\n --- Reading {fileinput.filename()} ---')
    print(' ->' + line, end='')
print()


# with open('generator.py', 'w') as f:
#     f.write()
