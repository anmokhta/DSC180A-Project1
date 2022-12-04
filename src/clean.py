import os

def clean():
    folders = ["test", "nips", "political"]
    subfolders = ["raw", "temp", "out"]

    for folder in folders:
        for subfolder in subfolders:
            currdir = os.path.join(folder, subfolder)
            try:
                for filename in os.listdir(currdir):
                    file_path = os.path.join(currdir, filename)
                    try:
                        os.remove(file_path)
                        print(file_path + " removed!")
                    except Exception as e:
                        print('Failed to delete %s. Reason: %s' % (file_path, e))
            except Exception as e:
                        print('Failed to find folder. Reason: %s' % (e))