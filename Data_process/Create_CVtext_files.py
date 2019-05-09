"""
This is a file that allows you to move certain target files in a target folder
to another named folder, and you define the target file names from another files
which contains the names
"""

import shutil, os
target_files_to_move = [] #define a list of files to move

current_dir = os.getcwd()#current directory, in this case, CV_images

"""##redefine this"""
reference_folder = os.path.join(current_dir,"CV_image","009")

#get the area names in the image folder, i.e CV_image/001
reference_names = [f for f in os.listdir(reference_folder) if os.path.isfile(os.path.join(reference_folder, f))]
#area_names would be: ["001.jpg","002.jpg" etc...]

target_files_to_move = [w.replace('jpg', 'txt') for w in reference_names] #created correspond area names

"""##redefine this"""
for f in target_files_to_move:
    try:
        shutil.move("train_text/{}".format(f), 'CV_text/009_text')
    except:
        pass
