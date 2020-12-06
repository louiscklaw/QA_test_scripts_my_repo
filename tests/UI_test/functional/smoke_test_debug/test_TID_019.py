import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *

from steps import *
from pages.config import *
from jp import *

# from test_TID_009 import *
from test_TID_016 import *


def test_TID_019(json_metadata):

  # browser = tour_TID_009(json_metadata)
  browser = tour_TID_016(json_metadata)

  # check result
  # check_TID_016.run_check(json_metadata, browser)

  # # order should send failure as no table assigned
  # check_TID_017.run_check(json_metadata, browser)

  # check_TID_019.run_check(json_metadata, browser)

  return browser
