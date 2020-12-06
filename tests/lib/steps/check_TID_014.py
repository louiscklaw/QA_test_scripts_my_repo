import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from steps.config import *
from time import sleep
from assert_check_point import assertCheckPoint
from assert_check_point_jot_metadata import assertCheckPointJotMetadata


def run_check(json_metadata, browser, things_to_add=14):
  # init test json_metadata
  json_metadata['TID_014']={}
  json_metadata['TID_014'][TESTFIELD_STATUS] = TEST_TESTING

  cart_page_po = cart_page.Main(browser)

  cart_page_po.tapBottomBarCartButton()

  assertCheckPointJotMetadata(json_metadata['TID_014'], browser, 'TID_014_1', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND, 0.05)
  for i in range(1,things_to_add):
    cart_page_po.tapAddButton(1)
    sleep(0.05)

  assertCheckPointJotMetadata(json_metadata['TID_014'], browser, 'TID_014_2', ERR_MSG_ERR_FOUND_TAPPING_ACCEPT_AND_CONTINUE_BUTTON, 0.05)

  json_metadata['TID_014'][TESTFIELD_STATUS] = TEST_PASS