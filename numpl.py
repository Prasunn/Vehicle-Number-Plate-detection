#import all required libraries
import json
from urllib.request import urlopen
from PIL import Image
import pytesseract

#Declare a list to store the values extracted from number plates
plate=list()

#Extract each line from the json file
for i in open('Indian_Number_plates.json'):

    #Convert the data from each json line to python data structure
    data=json.loads(i)

    #Extract each image from the web and convert them into grayscale for better performance
    img = Image.open(urlopen(data['content'])).convert('LA')

    #For more than one number plate in one image
    for num in data['annotation']:

        #Determine the area of the numberplate in the image
        area=(num['imageWidth']*num['points'][0]['x'], num['imageHeight']*num['points'][0]['y'], num['imageWidth']*num['points'][1]['x'], num['imageHeight']*num['points'][1]['y'])

        #Crop the image to only the numberplate portion
        pic=img.crop(area)

        #Extract the data in the image to string format
        nmpl=pytesseract.image_to_string(pic)
        plate.append(nmpl)
        print(nmpl)
