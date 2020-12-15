######################################
#         Raster Starter Code        #
#                                    #
#             UTeach CSP             #
#             Brian Ford             #
#                                    #
#              9/13/19               #
#                                    #
######################################

# Conner Zhao 

"""
Either start with your modified Raster Starter Code or click to open a new clean copy: Raster Starter Code.
Load and modify an image of your choosing. Use Photopin.com or Pixabay.com, online aggregator of digital images with Creative Commons licenses, to find an image or take one of yourself! Make sure to either rename the file to image.jpg after adding it to your program or change the image file name in the code.
Create your own filter using user input. 
Be creative!
"""

# importing PIL.Image library and os library
from PIL import Image 
import os

# Deletes old created images if they exist
if os.path.exists("newImage.jpg"):
  os.remove("newImage.jpg")

# Prints two blank lines to start our program output
print("\n\n")

# Opens image - Local File in repl.it
img = Image.open('4.8.jpg')

# Rescale image size down, if needed
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )

########################
#        Filter        #
########################
def newFilter():
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = r + rv
    newg = g + gv
    newb = b + bv
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the pixel values to newImage
  newImage.putdata(new_pixels)
  # Saves the new image file
  newImage.save("newImage.jpg")

# Creates an ImageCore Object from original image
pixels = img.getdata()
# Creates empty array to hold new pixel values
new_pixels = []
# For every pixel from our original image, it saves
# a copy of that pixel to our new_pixels array
for p in pixels:
  new_pixels.append(p)

# Calls the newFilter function to create the image
x = input('What color tint do you want you picture to have?')
red = 'Red'
gr= 'Green'
bl = 'Blue'
rv = 0
bv = 0
gv = 0
if x == red:
    rv = 128
elif x == gr:
    gv = 128
elif x == bl:
    bv = 128
newFilter()