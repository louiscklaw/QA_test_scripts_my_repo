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
  json_metadata['TID_001']={}
  json_metadata['TID_001'][TESTFIELD_STATUS] = TEST_TESTING

  # URL = 'http://192.168.88.105:8002/'
  # browser.get(URL)
  browser.get(LINE_UP_PAGE)
  line_up_page_po = line_up_page.FirstTimeLanding(browser)
  sleep(0.1)

  line_up_page_po.gotoLineUpPage()
  sleep(0.1)

  # assert False, 'hello fail'

  # assertCheckPoint(browser, 'TID_001_1', ERROR_MESSAGE)
  assertCheckPointJotMetadata(json_metadata['TID_001'], browser, 'TID_001_1', ERROR_MESSAGE, 0.04)

  json_metadata['TID_001'][TESTFIELD_STATUS] = TEST_PASS
