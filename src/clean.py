import os

# remove everything in test/temp
# remove everything in test/testdata
# remove everything in test/model

# remove everything in WHATEVER/data
# remove everything in WHATEVER/temp
# remove everything in WHATEVER/model

def clean():
    folders = ["test/temp", "test/testdata", "test/model"]
    try:
        for folder in folders:
            try:
                for filename in os.listdir(folder):
                    file_path = os.path.join(folder, filename)
                    try:
                        os.remove(file_path)
                        print(file_path + " removed!")
                    except Exception as e:
                        print('Failed to delete %s. Reason: %s' % (file_path, e))
            except Exception as e:
                        print('Failed to find folder. Reason: %s' % (file_path, e))
    except Exception as e:
        print("NO FILES TO CLEAN!")