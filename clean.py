# Turns out, this Oxford-IIIT dataset has a lot of corrupted images. So I will be cleaning up these pests in this program.
import os
from PIL import Image

if __name__ == "__main__":
  path = '/content/dataset-iiit-pet'
  image_path = os.path.join(path, 'images')
  mask_path = os.path.join(path, 'annotations/trimaps')
  x = []

  for filename in os.listdir(image_path):
    if filename.endswith('.jpg'):
      try:
        img = Image.open(os.path.join(image_path, filename))  # open the image file
        img.verify()  # verify that it is, in fact an image
      except (IOError, SyntaxError) as e:
        x.append(filename.split('.')[0])
        os.remove(os.path.join(image_path, filename))
    else:
      x.append(filename.split('.')[0])
      os.remove(os.path.join(image_path, filename))
  
  for mask_filename in os.listdir(mask_path):
    if mask_filename.split('.')[0] in x:
      os.remove(os.path.join(mask_path, mask_filename))