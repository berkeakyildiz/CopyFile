#
# Created by Berke Akyıldız on 28/August/2019
#

import shutil

# shutil.copy2('/src/file.ext', '/dst/dir')

src_file = input("Enter source file path: \n")

src_file = src_file.replace("\\", "\\\\")
file_base_name = src_file.split(".")[0]
file_extension = src_file.split(".")[1]

copy_count = input("Enter copy file count: \n")

for i in range(2, int(copy_count)+2):
    dst_file_name = file_base_name + " - " + str(i) + "." + file_extension
    print(dst_file_name)
    shutil.copy2(src_file, dst_file_name)
