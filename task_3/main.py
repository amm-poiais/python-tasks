import os
import sys
import shutil

src_dir = sys.argv[1]
dst_dir = sys.argv[2]

if not os.path.isdir(src_dir):
    print("Error: Input file is not a directory")
    exit(1)

if os.path.isfile(dst_dir) or os.path.islink(dst_dir):
    print("Error: Output directory is a file or symlink")
    exit(1)

if not os.path.isdir(dst_dir):
    os.mkdir(dst_dir)

names = os.listdir(src_dir)

for name_ext in names:
    src_filename = os.path.join(src_dir, name_ext)
    if not os.path.isfile(src_filename):
        continue

    _, ext = os.path.splitext(name_ext)

    target_dir = os.path.join(dst_dir, ext[1:])
    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)

    src_filename = os.path.join(src_dir, name_ext)
    target_filename = os.path.join(target_dir, name_ext)

    shutil.copyfile(src_filename, target_filename)
