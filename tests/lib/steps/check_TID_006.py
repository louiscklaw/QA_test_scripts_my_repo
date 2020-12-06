import line_up_page
import food_menu
import line_up_confirmation_dialogue
import item_add_page
import cart_page

from steps.config import *
from config import *
from time import sleep
from assert_check_point import assertCheckPoint
from assert_check_point_jot_metadata import assertCheckPointJotMetadata

def run_check(json_metadata, browser, TEST_USER="TID_006_USER", TEST_NOTE='this is some note', num_of_adult=2, num_of_child=3):
  json_metadata['TID_006']={}
  json_metadata['TID_006'][TESTFIELD_STATUS] = TEST_TESTING

  line_up_po = line_up_page.Main(browser)
  dialogue_po= line_up_confirmation_dialogue.Main(browser)

  # sleep(1)
  line_up_po.inputName(TEST_USER)
  line_up_po.inputNotes(TEST_NOTE)
  line_up_po.changeNumberOfAdult(num_of_adult)
  line_up_po.changeNumberOfChild(num_of_child)

  assertCheckPointJotMetadata(json_metadata['TID_006'], browser, 'TID_006_1', TEST_ERR_MSG, 0.5)
  # # assertCheckPoint(browser, 'TID_006_1', TEST_ERR_MSG)
  # # # assertSameImage(expected_screenshot_path, actual_screenshot_path,0.1,  TEST_ERR_MSG)

  line_up_po.submitLineUpTicket()
  assertCheckPointJotMetadata(json_metadata['TID_006'], browser, 'TID_006_2', TEST_ERR_MSG, 0.5)

  dialogue_po.tapOkButtonOnDialogue()
  assertCheckPointJotMetadata(json_metadata['TID_006'], browser, 'TID_006_3', TEST_ERR_MSG, 0.5)

  json_metadata['TID_006'][TESTFIELD_STATUS] = TEST_PASS
