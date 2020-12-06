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
from test_TID_017 import *


def test_TID_021(json_metadata):

  # browser = tour_TID_009(json_metadata)
  browser = tour_TID_017(json_metadata)

  check_TID_021.run_check(json_metadata, browser)

  return browser
