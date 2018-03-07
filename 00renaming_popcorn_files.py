import os
import shutil

path='C:\\Users\\soori\\movies\\Popcorn Time'
final_path="C:\\Users\\soori\\movies\\sorted"

all_filesname=os.listdir(path)

for filenames in all_filesname:
    tree_files=path+"\\"+filenames
    final_file=os.listdir(tree_files)
    for files in final_file:
        if files.endswith(".torrent"):
            #print files
            next
        else:
            path_source=tree_files+"\\"+files
            print path_source
            shutil.move(path_source,final_path)
    shutil.rmtree(tree_files)
