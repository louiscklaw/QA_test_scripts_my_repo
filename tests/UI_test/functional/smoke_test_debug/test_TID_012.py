import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *

from steps import *
from pages.config import *
from jp import *

from test_TID_009 import *

def tour_TID_012(json_metadata):

  browser = tour_TID_009(json_metadata)

  # the update of line up info appears here
  check_TID_012.run_check(json_metadata, browser)

  return browser
