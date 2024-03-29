import os,sys
from pprint import pprint
from diffimg import diff

def assertSameImage(img_expected, img_actual,image_test_threshold=0.05, error_msg='same image is expected but diff image found'):
  ''' exception if different image '''

  img_filename = os.path.basename(img_actual)
  # true = same image
  same_image = diff(img_expected, img_actual) < image_test_threshold

  print("debug: diff result {}".format(diff(img_expected, img_actual)))
  print("debug: image_test_threshold {}".format(image_test_threshold))

  print("debug: diff assert diff result {}, {}".format(same_image, img_filename))

  assert same_image, error_msg + "debug: diff result {} for file {}".format(diff(img_expected, img_actual))
