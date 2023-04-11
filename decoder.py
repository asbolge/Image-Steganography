from PIL import Image
import numpy

def DecodeImage(image, sentinel):
    image = Image.open(image)
    width, height = image.size
    
    mesaj = ""
    bitholder = ""

    bitplane = numpy.zeros((height, width))
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            leastSignificantBit = pixel & 1
            bitplane[y, x] = leastSignificantBit

    
    for a in range(height-1,-1,-1):
        for b in range(width-1,-1,-1):
            bitholder = bitholder + str(int(bitplane[a,b]))
            if len(bitholder) == 8:
                sembol = chr(int(bitholder, 2))
                if sembol == sentinel:
                    break
                else:
                    mesaj = mesaj + str(sembol)
                    mesaj = mesaj
                    bitholder = ""

    return ReverseMessage(mesaj)

def ReverseMessage(x):
  return x[::-1]

print(DecodeImage('72.tif', '%'))