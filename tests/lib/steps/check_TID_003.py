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
  json_metadata['TID_003']={}
  json_metadata['TID_003'][TESTFIELD_STATUS] = TEST_TESTING

  assertCheckPointJotMetadata(json_metadata['TID_003'], browser, 'TID_003_1', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND, 0.05)
  # assertCheckPoint(browser, 'TID_003_1', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND)
  line_up_page_po = line_up_page.FirstTimeLanding(browser)
  line_up_page_po.tapAcceptAndContinueButton()
  sleep(1)

  assertCheckPointJotMetadata(json_metadata['TID_003'], browser, 'TID_003_2', ERR_MSG_ERR_FOUND_TAPPING_ACCEPT_AND_CONTINUE_BUTTON, 0.05)
  # assertCheckPoint(browser, 'TID_003_2', ERR_MSG_ERR_FOUND_TAPPING_ACCEPT_AND_CONTINUE_BUTTON)

  json_metadata['TID_003'][TESTFIELD_STATUS] = TEST_PASS
