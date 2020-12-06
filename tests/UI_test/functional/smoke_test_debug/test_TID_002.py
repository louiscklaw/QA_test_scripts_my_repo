import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *

from steps import *
from pages.config import *
from jp import *

# TODO: fallback to 001_1 for remote chrome
from test_TID_001 import *

def tour_TID_002(json_metadata):
  # TODO: fallback to tour_TID_001_1 for remote chrome
  browser = tour_TID_001(json_metadata)

  # check result
  check_TID_002.run_check(json_metadata, browser)

  return browser