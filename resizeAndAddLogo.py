import os
from PIL import Image

SQUARE_FIT_SIZE = 1000
LOGO_FILENAME = 'catlogo.png'

logoIM = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIM.size

os.makedirs('withLogo', exist_ok=True) #创建文件夹

# TODO:Loop over all the files in the directory
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
        or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself
    im=Image.open(filename)
    width, height = im.size #get the dimensions of the opened picture file

    # TODO: Check if image needs to be resized
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # TODO: Calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height) #resizes height in proportion to width
            width = SQUARE_FIT_SIZE #set width, the largest dimension, to 1000
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
    # TODO: Resize the image
        print('Resizing %s to %sx%s' % (filename, width, height))
        im.resize((width, height)) #width and height need to be put in double parenthesis

    # TODO: Add the logo
    print('Adding logo to %s...' % (filename))
    im.paste(logoIM, (width - logoWidth, height - logoHeight), logoIM) #3rd argument is for transparency pixels
    # TODO: Save the image
    im.save(os.path.join('withLogo' ,filename)) #saves the new image in the withLogo folder