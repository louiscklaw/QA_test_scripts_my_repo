import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page
import table_assigned_dialogue

from steps.config import *
from config import *
from time import sleep
from assert_check_point import assertCheckPoint

from assert_check_point_jot_metadata import assertCheckPointJotMetadata

def run_check(json_metadata, browser, food_item_idx=1):
  TEST_ERR_MSG='It should direct to item add page'

  json_metadata['TID_009']={}
  json_metadata['TID_009'][TESTFIELD_STATUS] = TEST_TESTING

  # assertCheckPoint(browser, 'TID_009_1', TEST_ERR_MSG, 0.06)
  assertCheckPointJotMetadata(json_metadata['TID_009'], browser, 'TID_009_1', TEST_ERR_MSG, 0.5)

  food_menu_po = food_menu.Main(browser)
  food_menu_po.tapFoodItemByIdx(food_item_idx)

  # sleep a while to let the prompt disappear
  sleep(3)

  # assertCheckPoint(browser, 'TID_009_2_{}'.format(food_item_idx), TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_009'], browser, 'TID_009_2', TEST_ERR_MSG, 0.5)

  # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

  json_metadata['TID_009'][TESTFIELD_STATUS] = TEST_PASS
