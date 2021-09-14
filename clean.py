# Turns out, this Oxford-IIIT dataset has a lot of corrupted images. So I will be cleaning up these pests in this program.
import os
from PIL import Image

if __name__ == "__main__":
  path = '/content/dataset-iiit-pet'
  count = 0
  count_except = 0
  count_try = 0
  x = []
  for filename in os.listdir(os.path.join(path, 'images')):
    if filename.endswith('.jpg'):
      image_path = os.path.join(path, 'images')
      try:
        img = Image.open(os.path.join(image_path, filename))  # open the image file
        img.verify()  # verify that it is, in fact an image
        count_try = count_try + 1
      except (IOError, SyntaxError) as e:
        count_except = count_except + 1
        """mask_path = os.path.join(path, 'annotations/trimaps')
        print('Image: ', os.path.exists(os.path.join(image_path, filename)))
        print('Mask: ', os.path.exists(os.path.join(mask_path, filename)))
        """
    else:
      print("inside else")
      x.append(filename)
      count = count + 1
      
      """image_path = os.path.join(path, 'images')"""
      mask_path = os.path.join(path, 'annotations/trimaps')
      """os.remove(os.path.join(image_path, filename))
      os.remove(os.path.join(mask_path, filename))"""
      print('Mask: ', os.path.join(mask_path, filename))
  
  print(count)
  print("try: ", count_try)
  print("except: ", count_except)
  print(x)