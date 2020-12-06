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
  ERR_MSG_ERR_FOUND_BEFORE_RUNNING_004='error found before running TID_004'
  ERR_MSG_TNC_DIALOGUE_SHOULD_CLOSE='tapping close button , T&C dialog message should close'

  # init test json_metadata
  json_metadata['TID_004']={}
  json_metadata['TID_004'][TESTFIELD_STATUS] = TEST_TESTING

  assertCheckPointJotMetadata(json_metadata['TID_004'], browser, 'TID_004_1', ERR_MSG_ERR_FOUND_BEFORE_RUNNING_004, 0.015)
  # assertCheckPoint(browser, 'TID_004_1', ERR_MSG_ERR_FOUND_BEFORE_RUNNING_004, json_metadata=json_metadata)
  line_up_page_po = line_up_page.FirstTimeLanding(browser)

  line_up_page_po.tapCrossButton()

  assertCheckPointJotMetadata(json_metadata['TID_004'], browser, 'TID_004_2', ERR_MSG_TNC_DIALOGUE_SHOULD_CLOSE, 0.04)
  # assertCheckPoint(browser, 'TID_004_2', ERR_MSG_TNC_DIALOGUE_SHOULD_CLOSE, json_metadata=json_metadata)
  json_metadata['TID_004'][TESTFIELD_STATUS] = TEST_PASS