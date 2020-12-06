import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page


from steps.config import *
from time import sleep
from assert_check_point import assertCheckPoint
from assert_check_point_jot_metadata import assertCheckPointJotMetadata


def run_check(json_metadata, browser, add_food_item_idx=2):
  json_metadata['TID_016']={}
  json_metadata['TID_016'][TESTFIELD_STATUS] = TEST_TESTING

  food_menu_po=food_menu.Main(browser)
  cart_page_po = cart_page.Main(browser)
  item_add_page_po=item_add_page.Main(browser)

  # escape from cart list page from 015
  # todo: remove me
  # cart_page_po.tapTopLeftCloseButton()
  # assertCheckPoint(browser, 'TID_016_1', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_016'], browser, 'TID_016_1', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND, 0.1)

  # add another food
  cart_page_po.tapBottomBarMenuButton()
  food_menu_po.tapFoodItemByIdx(add_food_item_idx)
  # assertCheckPoint(browser, 'TID_016_2', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_016'], browser, 'TID_016_2', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND, 0.1)

  item_add_page_po.addFood()
  # assertCheckPoint(browser, 'TID_016_3', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_016'], browser, 'TID_016_3', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND, 0.1)


  item_add_page_po.tapAddIntoCartButton()
  sleep(5)
  # assertCheckPoint(browser, 'TID_016_4', TEST_ERR_MSG, 0.055)
  assertCheckPointJotMetadata(json_metadata['TID_016'], browser, 'TID_016_4', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND, 0.1)


  food_menu_po.tapCartButton()
  # assertCheckPoint(browser, 'TID_016_5', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_016'], browser, 'TID_016_5', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND, 0.1)


  cart_page_po.tapRemoveButton(1)
  # assertCheckPoint(browser, 'TID_016_6', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_016'], browser, 'TID_016_6', ERR_MSG_FIRST_TIME_LANDING_NOT_FOUND, 0.1)

  json_metadata['TID_016'][TESTFIELD_STATUS] = TEST_PASS
