# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
# -*- coding: utf-8 -*-
import logging
import json
import requests
from datetime import datetime
from typing import Any, Dict, List, Text, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
    FollowupAction,
)

class getInfoUser(FormAction):

    #name của action form 
    def name(self):
        return "get_info_user_form"
    
    # kiểm tra xem form cần fill những slot nào
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["name", "phone_number", "birth", "school"]
    
    # tiếp theo form sẽ tiến hành lấy data từ slot_mapping để map giá trị và fill vào slot
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "name": [self.from_entity(entity = "name", intent = ["user_name"]), self.from_text()],
            "phone_number": [self.from_entity(entity = "phone_number", intent = ["user_phone_number"]), self.from_text()],
            "birth": [self.from_entity(entity = "birth", intent = ["user_birth"]), self.from_text()],
            "school": [self.from_entity(entity = "school", intent = ["user_school"]), self.from_text()]
        }
    

    # sẽ thực hiện việc cần thiết với các slot đã fill ví dụ: lưu database...v...v
    def submit(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> List[Dict]:
        dispatcher.utter_message("Cám ơn bạn đã cung cấp thông tin")
        return []

class requiredStaff(Action):

    def name(self) -> Text:
        return "action_required_staff"
    
    def run(self, dispatcher, tracker, domain):
        message = next(tracker.get_latest_entity_values("message"), None)
        call = next(tracker.get_latest_entity_values("call"), None)
        if call == "gọi" or call == "gọi điện" or call == "goi dien":
            dispatcher.utter_message(template = "utter_request_info_user")
            return [FollowupAction("get_info_user_form")]
        elif message == "nhắn tin" or message == "nhắn" or message == "nhan tin":
            dispatcher.utter_message(template = "utter_message_staff")
        return []