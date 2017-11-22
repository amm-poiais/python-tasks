import os
import sys
import shutil


def get_file_list(src_dir):
    raw_names = os.listdir(src_dir)

    result = []
    for raw_name in raw_names:
        full_name = os.path.join(src_dir, raw_name)

        if os.path.isfile(full_name):
            result.append(full_name)
        elif os.path.isdir(full_name):
            nested_files = get_file_list(full_name)
            for file in nested_files:
                result.append(file)

    return result


def main():
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

    name_list = get_file_list(src_dir)
    if not name_list:
        print('Empty source directory')
        return

    for src_full_name in name_list:
        _, ext = os.path.splitext(src_full_name)
        if not ext:
            ext = "no extension"

        file_path, file_name = os.path.split(src_full_name)

        target_dir = os.path.join(dst_dir, ext)
        if not os.path.isdir(target_dir):
            os.mkdir(target_dir)

        target_full_name = os.path.join(target_dir, file_name)

        shutil.copyfile(src_full_name, target_full_name)
        print("{} goes to {}".format(src_full_name, target_full_name))


main()
