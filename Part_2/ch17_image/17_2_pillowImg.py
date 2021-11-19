from PIL import Image, ImageColor
import os, sys

def imgInfo(imgObj):
    '''
    获取图像对象的信息
    '''
    print(imgObj.size)
    width,height = imgObj.size
    print(width, height)
    print(imgObj.filename)
    print(imgObj.format)
    print(imgObj.format_description)
    print(imgObj.save('zophie.jpg'))

def newImg(path):
    '''
    new()新建一个图像，并保存到本地
    '''
    # (100, 200)表示图像的宽、高，颜色为'purple'，不透明
    # (20, 20)表示图像的宽、高，颜色为黑色，全透明
    newImg1 = Image.new('RGBA', (100, 200), 'purple')
    newImg1.save(os.path.join(path, 'img', 'purpleImg.png'))
    newImg2 = Image.new('RGBA', (20, 20))
    newImg2.save(os.path.join(path, 'img', 'transparentImg.png'))

def cropImg(imgObj, path):
    '''
    crop()从图像中裁剪一个矩形区域
    '''
    croppedImg = imgObj.crop((335, 345, 565, 560))
    croppedImg.save(os.path.join(path, 'cropped.png'))

def copy_paste(imgObj, path):
    '''
    copy(), paste()复制、粘贴图像到另一个图像对象
    '''
    copyImg = imgObj.copy()

    faceImg = imgObj.crop((335, 345, 565, 560))
    print(faceImg.size)
    copyImg.paste(faceImg, (0,0))
    copyImg.paste(faceImg, (400, 500))
    copyImg.save(os.path.join(path, 'pasted.png'))

def copy_paste_tiled(imgObj, path):
    '''
    copy(), paste()复制、粘贴图像到另一个图像对象，并依次铺满
    '''
    copyImg = imgObj.copy()
    faceImg = imgObj.crop((335, 345, 565, 560))
    copyImgWidth, copyImgHeight = copyImg.size
    faceImgWidth, faceImgHeight = faceImg.size
    for left in range(0, copyImgWidth, faceImgWidth):
        for top in range(0, copyImgHeight, faceImgHeight):
            print(left, top)
            copyImg.paste(faceImg, (left, top))
    copyImg.save(os.path.join(path, 'pasted_tiled.png'))

def resizeImg(imgObj, path):
    width, height = imgObj.size
    quartersizeImg = imgObj.resize((int(width/2), int(height/2)))
    quartersizeImg.save(os.path.join(path, 'quartersized.png'))
    quartersizeImg = imgObj.resize((width, height+300))
    quartersizeImg.save(os.path.join(path, 'svelte.png'))

def rotatedImg(imgObj, path):
    # rotate
    imgObj.rotate(90).save(os.path.join(path, 'rotate90.png'))
    imgObj.rotate(180).save(os.path.join(path, 'rotate180.png'))
    imgObj.rotate(270).save(os.path.join(path, 'rotate270.png'))
    # expand
    imgObj.rotate(6).save(os.path.join(path, 'rotate6.png'))
    imgObj.rotate(6, expand=True).save(os.path.join(path, 'rotate6_expanded.png'))
    # transpose
    imgObj.transpose(Image.FLIP_LEFT_RIGHT).save(os.path.join(path, 'horizontal_flip.png'))
    imgObj.transpose(Image.FLIP_TOP_BOTTOM).save(os.path.join(path, 'vertical_flip.png'))

def pixelImg(path):
    newImg = Image.new('RGBA', (100, 100))
    print(newImg.getpixel((0,0)))
    for x in range(100):
        for y in range(50):
            newImg.putpixel((x,y), (210, 210, 210))
    for x in range(100):
        for y in range(50, 100):
            newImg.putpixel((x,y), ImageColor.getcolor('darkgray', 'RGBA'))
    
    print(newImg.getpixel((0,0)))
    print(newImg.getpixel((0, 50)))
    newImg.save(os.path.join(path, 'putPixel.png'))

def main():
    currentPath = os.path.dirname(sys.argv[0])
    imgPath = os.path.join(currentPath, 'img')
    catImgPath = os.path.join(imgPath, 'zophie.png')
    # 17.2
    catImg = Image.open(catImgPath)

    # 17.2.1
    #imgInfo(catImg) 
    #newImg(imgPath)

    # 17.2.2
    #cropImg(catImg, imgPath)

    # 17.2.3
    #copy_paste(catImg, imgPath)
    #copy_paste_tiled(catImg, imgPath)

    # 17.2.4
    #resizeImg(catImg, imgPath)
    
    # 17.2.5
    #rotatedImg(catImg, imgPath)
    
    # 17.2.6
    pixelImg(imgPath)

    print('Done')

if __name__ == '__main__':
    main()