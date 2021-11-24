

from datetime import datetime
from django.conf import settings as django_settings
import os

def fpublish_opinion(content = "example 1" , startfolder = "opinions", filetype = "html", fname_prefix = "opinion"):
    fname = fcreate_path_curr_date(startfolder, filetype, fname_prefix)
    fsavefile(fname, content)

#create path, and keep the folder in hirarchy based on date
#this function return the full path of the file that
#has to be saved

def fcreate_path_curr_date(startfolder, filetype, fname_prefix):
    fdatename = datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
    lidatepath = list(fdatename.split('.'))
    fdatename = fname_prefix + fdatename+  "." + filetype
    lidatepath.insert(0, startfolder)
    root = fcreatepath(lidatepath)
    return os.path.join(root, fdatename)
#get list of path to create and return the path in string after created
def fcreatepath(lidatepath):
    root = django_settings.STATIC_ROOT
    for dirname in lidatepath:
        root = os.path.join(root, dirname)
        isexist = check_if_dir_exist(root)
        if(isexist):
            continue
        else:
            create_dir(root)
    return root

def fsavefile(fname, content):
    f = open(fname,"w")
    f.write(content)
    f.close()

def check_if_dir_exist(path):
    return os.path.isdir(path)

def create_dir(path):
    os.mkdir(path)
