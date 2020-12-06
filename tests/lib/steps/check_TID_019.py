import please_take_seat_first_dialogue
import cart_page
import item_add_page


from steps.config import *
from time import sleep
from assert_check_point import assertCheckPoint
from assert_check_point_jot_metadata import assertCheckPointJotMetadata


def run_check(json_metadata, browser):
  json_metadata['TID_019']={}
  json_metadata['TID_019'][TESTFIELD_STATUS] = TEST_TESTING

  cart_page_po = cart_page.Main(browser)
  please_take_seat_first_dialogue_po=please_take_seat_first_dialogue.Main(browser)
  item_add_page_po=item_add_page.Main(browser)

  # check if red dialogue appears
  # assertCheckPoint(browser, 'TID_019_1', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_019'], browser, 'TID_019_1', TEST_ERR_MSG, 0.05)


  cart_page_po.tapPlaceOrderButton()
  # tap ok to dismiss dialogue
  sleep(3)
  please_take_seat_first_dialogue_po.tapOkButtonOnDialogue()

  assertCheckPointJotMetadata(json_metadata['TID_019'], browser, 'TID_019_2', TEST_ERR_MSG, 0.05)

  json_metadata['TID_019'][TESTFIELD_STATUS] = TEST_PASS
