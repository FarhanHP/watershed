import numpy as np

class Pixel :
    def __init__(self, grayScale, label=None, neighbors=None):
        '''
            int grayscale;
            String label;
        '''
        self.grayScale = grayScale
        self.label = label
        
        if(neighbors == None):
            self.neighbors = list()
        else:
            self.neighbors = neighbors
    
    def __str__(self):
        return self.label

    def __int__(self):
        return self.grayScale

    def setLabel(self, label):
        self.label = label
    
    def getLabel(self):
        return self.label

    def getGrayScale(self):
        return self.grayScale

    def getNeighbors(self):
        return self.neighbors

    def addNeighbors(self, pixel):
        self.neighbors.append(pixel)

    def clone(self):
        return Pixel(self.grayScale, self.label, neighbors=self.neighbors)

class ImageGrayscale:
    def __init__(self, pixels):
        '''
            Pixel[][]; 
        '''
        self.pixels = pixels

        #set neighbors of each pixel
        for i in range(len(pixels)):
            for j in range(len(pixels[0])):
                #8-connectivity
                if(i-1 >= 0):
                    self.pixels[i][j].addNeighbors(self.pixels[i-1][j])
                if(i-1 >= 0 and j-1 >= 0):
                    self.pixels[i][j].addNeighbors(self.pixels[i-1][j-1])
                if(i-1 >= 0 and j+1 < len(pixels[0])):
                    self.pixels[i][j].addNeighbors(self.pixels[i-1][j+1])
                if(j-1 >= 0):
                    self.pixels[i][j].addNeighbors(self.pixels[i][j-1])
                if(j+1 < len(pixels[0])):
                    self.pixels[i][j].addNeighbors(self.pixels[i][j+1])
                if(i+1 < len(pixels) and j-1 >= 0):
                    self.pixels[i][j].addNeighbors(self.pixels[i+1][j-1])
                if(i+1 < len(pixels)):
                    self.pixels[i][j].addNeighbors(self.pixels[i+1][j])
                if(i+1 < len(pixels) and j+1 < len(pixels[0])):
                    self.pixels[i][j].addNeighbors(self.pixels[i+1][j+1])

    def __str__(self):
        output = str()
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                output += " "+str(self.pixels[i][j].getLabel())
            output += "\n"
        return output

    def getPixels(self):
        return self.pixels

    def setPixels(self, pixels):
        self.pixels = pixels

    #vincent-soille algorithm
    def watershedVS(self):
        def isNewBasin(PIXELS):
            for pixel in PIXELS :
                if(pixel.getLabel() != None and pixel.getLabel() != "-"):
                    return False
            return True

        def isWatershed(PIXELS, h):
            basin = list()
            neighboringWatershed = 0
            for pixel in PIXELS :
                if(pixel.getGrayScale() <= h and pixel.getLabel() != None):
                    if(pixel.getLabel() == "-"):
                        neighboringWatershed += 1
                    elif(pixel.getLabel() not in basin):
                        basin.append(pixel.getLabel())
            
            if (len(basin) > 1 or neighboringWatershed == len(PIXELS)):
                return True
            return False

        def getNearbyBasin(PIXELS, h):
            for pixel in PIXELS :
                if(pixel.getGrayScale() <= h and pixel.getLabel() != None and pixel.getLabel() != "-"):
                    return pixel.getLabel()
            print([i.getLabel() for i in PIXELS])
            return None

        currentLabelInAscii = 65
        
        pixelsPointer = list()
        #insertionSort
        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                isDone = False
                for k in range(len(pixelsPointer)):
                    if(int(pixelsPointer[k]) > int(pixels[i][j])):
                        pixelsPointer.insert(k, self.pixels[i][j])
                        isDone = True
                        break
                if(not isDone):
                    pixelsPointer.append(self.pixels[i][j])

        queue = list()
        hmin = int(pixelsPointer[0])
        hmax = int(pixelsPointer[-1])

        while (hmin <= hmax):
            while len(pixelsPointer) > 0 :
                if(hmin == pixelsPointer[0].getGrayScale()):
                    queue.append(pixelsPointer.pop(0))
                else :
                    break 

            while (len(queue) > 0):
                currentPixel = queue.pop(0)
                currentNeighbors = currentPixel.getNeighbors()
                if(currentPixel.getLabel() == None and currentPixel.getGrayScale() == hmin):
                    queue = queue + currentNeighbors
                    if(isNewBasin(currentNeighbors)):
                        currentPixel.setLabel(chr(currentLabelInAscii))
                        currentLabelInAscii += 1
                    elif(isWatershed(currentNeighbors, hmin)):
                        currentPixel.setLabel("-")
                    else :
                        currentPixel.setLabel(getNearbyBasin(currentNeighbors, hmin))

            hmin += 1


if __name__ == "__main__":
    a = np.random.rand(15, 15)
    pixels = list()
    for i in range(len(a)):
        sub_pixels = list()
        for j in range(len(a[0])):
            sub_pixels.append(Pixel(int(a[i][j] * 226)))
        pixels.append(sub_pixels)

    for i in pixels :
        print([j.getGrayScale() for j in i])
    img = ImageGrayscale(pixels)
    img.watershedVS()
    print(img)
