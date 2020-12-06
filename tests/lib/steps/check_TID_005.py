import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page

from steps.config import *
from time import sleep
from assert_check_point import assertCheckPoint
from assert_check_point_jot_metadata import assertCheckPointJotMetadata

def run_check(json_metadata, browser):
  # init test json_metadata
  json_metadata['TID_005']={}
  json_metadata['TID_005'][TESTFIELD_STATUS] = TEST_TESTING

  fl_page = food_menu.Main(browser)
  fl_page.tapLineUpIcon()

  # assertCheckPoint(browser, 'TID_005_1', TNC_DIALOG_MESSAGE_SHOULD_CLOSE)
  assertCheckPointJotMetadata(json_metadata['TID_005'], browser, 'TID_005_1', TNC_DIALOG_MESSAGE_SHOULD_CLOSE, 0.05)

  json_metadata['TID_005'][TESTFIELD_STATUS] = TEST_PASS
