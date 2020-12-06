import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page

from config import *
from steps.config import *

from time import sleep
from assert_check_point import assertCheckPoint
from assert_check_point_jot_metadata import assertCheckPointJotMetadata


def run_check(json_metadata, browser):
  # init test json_metadata
  json_metadata['TID_002']={}
  json_metadata['TID_002'][TESTFIELD_STATUS] = TEST_TESTING

  line_up_page_po = line_up_page.FirstTimeLanding(browser)

  assertCheckPointJotMetadata(json_metadata['TID_002'], browser, 'TID_002_1', ERR_MSG_BEFORE_TAPPING_TNC_MSG, 0.5)
  # TODO: assertCheckPoint(browser, 'TID_002_1', ERR_MSG_BEFORE_TAPPING_TNC_MSG)

  line_up_page_po.tapTAndCText()

  sleep(1)
  # TODO: assertCheckPoint(browser, 'TID_002_2', ERR_MSG_BACK_FROM_TNC_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_002'], browser, 'TID_002_2', ERR_MSG_BACK_FROM_TNC_MSG, 0.5)

  # back after test
  line_up_page_po.backFromTAndCText()
  # TODO: assertCheckPoint(browser, 'TID_002_3', ERR_MSG_BACK_FROM_TNC_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_002'], browser, 'TID_002_3', ERR_MSG_BACK_FROM_TNC_MSG, 0.5)

  json_metadata['TID_002'][TESTFIELD_STATUS] = TEST_PASS