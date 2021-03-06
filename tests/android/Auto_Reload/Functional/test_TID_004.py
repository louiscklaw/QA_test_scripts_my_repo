import os,sys
from pprint import pprint
import random
from time import sleep

sys.path.append(os.path.dirname(__file__)+'/../..')
from lib.config import *

from urls import *

from Auto_Reload.Functional.test_TID_003_1 import tour_TID_003_1 as tour_TID_003_1
import lib.checks.check_TID_004 as check_TID_004
from lib.utils.save_recording_screen import saveRecordingScreen
from lib.utils.dismiss_test_device import dismissTestDevice

def test_TID_004(json_metadata):
  browser = tour_TID_003_1(json_metadata)

  try:

    check_TID_004.run_check(json_metadata, browser)

  finally:
    saveRecordingScreen(browser,'TID_004_client')

    dismissTestDevice(browser)
