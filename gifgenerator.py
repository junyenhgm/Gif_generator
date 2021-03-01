import imageio
import os

def Make_from_video():
    from moviepy.editor import *
    clip = (VideoFileClip("input.mp4")
            .subclip((1,22.65),(1,10))
            .resize(0.3))
    clip.write_gif("use_your_head.gif")


images = []
jpgfiles = []

files = sorted(os.listdir(), key=lambda v: v.upper())
for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        jpgfiles.append(file)

for filename in jpgfiles:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images, duration=1)
