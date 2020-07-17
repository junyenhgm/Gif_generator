import imageio
images = []

filenames = ['1', '2', '3', '4', '5', '6']

for filename in filenames:
    filename += ".jpg"
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images, duration=1)
