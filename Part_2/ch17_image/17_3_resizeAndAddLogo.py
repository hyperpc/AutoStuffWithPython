#! python3
import os, sys
from PIL import Image

def main():
    currentPath = os.path.dirname(sys.argv[0])
    imgPath = os.path.join(currentPath, 'img')
    # 第1步
    LOGO_FILENAME = 'catlogo.png'
    LOGO_FILENAME_RESIZED = 'catlogo_resized.png'
    SQUARE_FIT_SIZE = 300
    logoImg = Image.open(os.path.join(imgPath, LOGO_FILENAME)).convert('RGBA')
    logoW, logoH = logoImg.size
    if logoW > 80 or logoH> 100:
        if logoW > 80:
            logoH = int((80/logoW)*logoH)
            logoW = 80
        else:
            logoW = int((100/logoH)*logoW)
            logoH = 100
    logoImg_resized = logoImg.resize((logoW, logoH))
    logoImg_resized.save(os.path.join(imgPath, LOGO_FILENAME_RESIZED))
    logoImg_resized = Image.open(os.path.join(imgPath, LOGO_FILENAME_RESIZED)).convert('RGBA')

    withLogoPath = os.path.join(imgPath, 'withLogo')
    os.makedirs(withLogoPath, exist_ok=True)
    # 第2步
    # loop over all files in the working directory
    for filename in os.listdir(imgPath):
        if not (filename.endswith('.png') or filename.endswith('.jpg') \
            or filename == LOGO_FILENAME):
            continue # skip non-image files and the logo file itself
        img = Image.open(os.path.join(imgPath, filename)).convert('RGBA')
        width, height = img.size
        #check if image needs to be resized
        if width> SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
            # calculate the new width and height to resize to
            if width > height:
                height = int((SQUARE_FIT_SIZE/width)*height)
                width = SQUARE_FIT_SIZE
            else:
                width = int((SQUARE_FIT_SIZE/height)*width)
                height = SQUARE_FIT_SIZE
            # resize the image
            print('Resizing %s(%d, %d)...' % (filename, width, height))
            img = img.resize((width, height))

            # add logo
            print('Adding logo(%d, %d) to %s...' % (logoW, logoH, filename))
            img.paste(logoImg_resized, box=(width - logoW, height - logoH))
            img.save(os.path.join(withLogoPath, filename))
            nameArray = filename.split('.')
            filename_transpose = nameArray[0] + '_transpose.' + nameArray[len(nameArray) - 1]
            img.paste(logoImg_resized, box=(width - logoW, height - logoH), mask=logoImg_resized)
            img.save(os.path.join(withLogoPath, filename_transpose))

    print('Done')

if __name__ == '__main__':
    main()