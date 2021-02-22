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


files = sorted(os.listdir(), key=lambda v: v.upper())
for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        jpgfiles.append(file)

for filename in jpgfiles:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images, duration=1)
