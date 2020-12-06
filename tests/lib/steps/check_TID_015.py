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
  json_metadata['TID_015']={}
  json_metadata['TID_015'][TESTFIELD_STATUS] = TEST_TESTING

  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)

  # assertCheckPoint(browser, 'TID_015_1', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_015'], browser, 'TID_015_1', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND, 0.05)

  for i in range(1,20):
    cart_page_po.tapMinusButton(1)


  # assertCheckPoint(browser, 'TID_015_2', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_015'], browser, 'TID_015_2', ERR_MSG_ERR_FOUND_TAPPING_ACCEPT_AND_CONTINUE_BUTTON, 0.05)

  json_metadata['TID_015'][TESTFIELD_STATUS] = TEST_PASS
