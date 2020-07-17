import imageio
import os
# import glob

images = []
jpgfiles = []

# arr = os.listdir()
# print(arr)

# Using glob is easier to select the file of the same type or with something in common.
# jpgfiles = []
# for file in glob.glob("*.jpg"):
#     jpgfiles.append(file)


# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".jpg") or file.endswith(".png"):
            jpgfiles.append(file)

for filename in jpgfiles:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images, duration=1)
