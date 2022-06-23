import os


def get_filename_dict(path):
    filename_list = os.listdir(path)

    filename_dict = {}
    for filename in filename_list:
        filename_dict[filename[:-4]] = filename

    return filename_dict