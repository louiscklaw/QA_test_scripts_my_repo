
from steps.config import *
from config import *
from assert_check_point import assertCheckPoint
import table_assigned_dialogue
from time import sleep
import random

from stubs.server.assign_table.assign_table_by_name import assignTableByName

from assert_check_point_jot_metadata import assertCheckPointJotMetadata

def run_check(json_metadata, browser, table_username ,sleep_before_confirm_s=13):

  json_metadata['TID_006_1']={}
  json_metadata['TID_006_1'][TESTFIELD_STATUS] = TEST_TESTING

  # TODO: resume me
  # assertCheckPoint(browser, 'TID_006_1_1', TEST_ERR_MSG)
  assertCheckPointJotMetadata(json_metadata['TID_006_1'], browser, 'TID_006_1_1', TEST_ERR_MSG, 0.5)


  assignTableByName(table_username, random.randrange(2,50,3))

  sleep(sleep_before_confirm_s)
  table_assigned_dialogue_po = table_assigned_dialogue.Main(browser)
  table_assigned_dialogue_po.tapOkButtonOnDialogue()

  # # NOTE: update threshold due to table number varying
  # assertCheckPoint(browser, 'TID_006_1_2', TEST_ERR_MSG, 0.05)
  assertCheckPointJotMetadata(json_metadata['TID_006_1'], browser, 'TID_006_1_2', TEST_ERR_MSG, 0.5)

  json_metadata['TID_006_1'][TESTFIELD_STATUS] = TEST_PASS
