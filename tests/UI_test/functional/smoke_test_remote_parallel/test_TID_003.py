import os,sys
from pprint import pprint
from time import sleep

sys.path.append(os.path.dirname(__file__))
from path_config import *
from urls import *

from steps import *
from pages.config import *
from jp import *

from test_TID_002 import *

def tour_TID_003(json_metadata):

  browser = tour_TID_002(json_metadata)

  # check result
  check_TID_003.run_check(json_metadata, browser)

  return browser