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
  json_metadata['TID_021']={}
  json_metadata['TID_021'][TESTFIELD_STATUS] = TEST_TESTING

  # assertCheckPoint(browser, 'TID_021_1', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_021'], browser, 'TID_021_1', TEST_ERR_MSG, 0.5)

  cart_page_po = cart_page.Main(browser)
  cart_page_po.tapBottomBarOrderHistoryButton()

  # assertCheckPoint(browser, 'TID_021_2', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_021'], browser, 'TID_021_2', TEST_ERR_MSG, 0.5)

  json_metadata['TID_021'][TESTFIELD_STATUS] = TEST_PASS
