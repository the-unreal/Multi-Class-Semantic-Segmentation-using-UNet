# Turns out, this Oxford-IIIT dataset has a lot of corrupted images. So I will be cleaning up these pests in this program.
import os
from PIL import Image

if __name__ == "__main__":
  path = '/content/data'
  for filename in listdir(os.path.join(path, 'images')):
    if filename.endswith('.JPG'):
      image_path = os.path.join(path, 'images')
      try:
        img = Image.open(os.path.join(image_path, filename))  # open the image file
        img.verify()  # verify that it is, in fact an image
      except (IOError, SyntaxError) as e:
        mask_path = os.path.join(path, 'annotations/trimaps')
        print('Image: ', os.path.exists(mask_path, filename))
        print('Mask: ', os.path.exists(mask_path, filename))
        """os.remove(os.path.join(image_path, filename))
        os.remove(os.path.join(mask_path, filename))"""