import os

# remove everything in test/temp
# remove everything in test/testdata
# remove everything in test/model

# remove everything in WHATEVER/data
# remove everything in WHATEVER/temp
# remove everything in WHATEVER/model

def clean():
    folders = ["test/temp", "test/testdata", "test/model"]
    for folder in folders:
        try:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    os.remove(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
        except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))