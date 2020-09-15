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

def load_list_data():
    path_file = "mapping/"
    with open(path_file + "major.txt", "r") as f:
        major_list = f.read().split(",")
    with open(path_file + "certificate.txt", "r") as f:
        certificate_list = f.read().split(",")
    
    return major_list, certificate_list

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
        # check điều kiện cho slot
        """def validate_room_id(
                        self,
                        value: Text,
                        dispatcher: CollectingDispatcher,
                        tracker: Tracker,
                        domain: Dict[Text, Any],
                    ) -> Dict[Text, Any]:

        if value > 50:
            dispatcher.utter_message("Số phòng không hợp lệ")
            return {"room_id": None}
        return {"room_id": value}"""

    # sẽ thực hiện việc cần thiết với các slot đã fill ví dụ: lưu database...v...v
    def submit(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],) -> List[Dict]:
        ##dispatcher.utter_message("Thông tin này đã được lưu vào database")
        return []

class requiredStaff(Action):

    def name(self) -> Text:
        return "action_required_staff"
    
    def run(self, dispatcher, tracker, domain):
        message = str(tracker.latest_message['intent'].get('name'))
        call = str(tracker.latest_message['intent'].get('name'))

        if call == "call_method":
            dispatcher.utter_message(template = "utter_request_info_user")
            return [FollowupAction("get_info_user_form")]
        elif message == "message_method":
            dispatcher.utter_message(template = "utter_message_staff")
            return []
        return []

class major(Action):
    def name(self) -> Text:
        return "action_major"

    def run(self, dispatcher, tracker, domain):
        #nếu không bắt được entites trong list chuyên ngành sẽ trả về danh sách chuyên ngành dúng cho user
        major_list, _ = load_list_data()
        major_name = str(next(tracker.get_latest_entity_values("major"), None))
        intent_major_name = str(tracker.latest_message['intent'].get('name'))
        if major_name != None:
            major_name = major_name.lower()
        if major_name not in major_list or major_name is None and intent_major_name == "info_major":
            dispatcher.utter_message(template = "utter_info_major")
        elif major_name in major_list and intent_major_name == "info_major":
            dispatcher.utter_message(
            "bạn có thể xem chi tiết chuyên ngành {0} tại đây: https://drive.google.com/file/d/1xtSW2DEYP4xYzWjmuxKsnaym_bhneCOz/view?usp=sharing".format(major_name))
        #nếu bắt được entites chuyên ngành trong list chuyên ngành thì sẽ trả về thông tin là image
        return []

class english(Action):
    def name(self) -> Text:
        return "action_english"
    
    def run(self, dispatcher, tracker, domain):
        entity_eng = str(next(tracker.get_latest_entity_values("entity_eng"), None))
        english_intent = str(tracker.latest_message['intent'].get('name'))
        _, certificate_list = load_list_data()
        if entity_eng != None:
            entity_eng = entity_eng.lower()
        if english_intent == "english" and entity_eng == "bắt buộc":
            dispatcher.utter_message(
            text = "chương trình tiếng anh là bắt buộc(trong trường hợp bạn không có chứng chỉ tiếng anh IELTS hoặc TOFLE)\
             trước khi vào học chuyên ngành và bao gồm 6 mức, thời lượng học mỗi mức là 2 tháng.\
             Bạn sẽ thi xếp lớp tiếng Anh để xem mình cần bắt đầu theo học lớp nào là phù hợp nhất.\
             Tuỳ theo kết quả xếp lớp mà thời gian học tiếng Anh của bạn sẽ kéo dài từ 2 tháng đến một năm.")
        elif english_intent == "english" and entity_eng in certificate_list:
            dispatcher.utter_message(
                text = "Mục đích của Chương trình tiếng Anh dự bị là trang bị kỹ năng tiếng Anh cho sinh viên đủ trình độ để theo học học kỳ chuyên ngành.\
                 Nếu bạn có chứng chỉ IELTS (Học thuật) từ 6.0 và TOEFL iBT từ 80 hoặc quy đổi tương đương còn hiệu lực tính đến thời điểm nhập học,\
                  bạn sẽ được miễn tham gia chương trình tiếng Anh dự bị và vào thẳng học kỳ chuyên ngành ngay từ năm đầu tiên. Như vậy,\
                 bạn sẽ sớm tốt nghiệp và đi làm.")
        else:
            dispatcher.utter_message(
                text = "Trước khi vào học chuyên ngành tất cả sinh viên cần phải có kiến thức về tiếng anh,\
                     trong trường hợp mất gốc hoặc yếu kém, tất cả sinh viên sẽ được đào tạo tiếng anh.\
                     cấu trúc bài thi tiếng anh bao gồm 3 phần.")
        return []

class recruitment(Action):
    def name(self) -> Text:
        return "action_recruitment"

    def run(self, dispatcher, tracker, domain):
        format_recruitment = str(next(tracker.get_latest_entity_values("format"), None))
        intent_recruitment = str(tracker.latest_message['intent'].get('name'))
        if format_recruitment != None:
            format_recruitment = format_recruitment.lower()
        if intent_recruitment == "recruitment" and format_recruitment == "học bạ":
            dispatcher.utter_message(
                text = "- Xét tuyển học bạ:\n\
                        + Đối với thí sinh tốt nghiệp THPT trước năm 2020 hoặc (thí sinh tốt nghiệp THPT năm 2020 nộp hồ sơ xét tuyển trước ngày 01/04/2020):\n\
                        Tổng điểm 3 môn (mỗi môn tính trung bình hai học kỳ cuối THPT) đạt 21 điểm* trở lên (áp dụng cho sinh viên nhập học tại Hà Nội và Tp. Hồ Chí Minh),\
                         đạt 19.5 điểm* trở lên (áp dụng cho sinh viên nhập học tại Tp.Cần Thơ và Tp.Đà Nẵng) xét theo tổ hợp môn tương ứng với ngành đăng ký học tại Trường ĐH FPT.\n\
                        + Đối với thí sinh tốt nghiệp THPT năm 2020 (nộp hồ sơ xét tuyển từ ngày 01/04/2020):\n\
                        Đạt xếp hạng theo học bạ THPT năm 2020 thuộc Top50 THPT 2020 (chứng nhận thực hiện trên trang http://SchoolRank.fpt.edu.vn).\n")

        elif intent_recruitment == "recruitment" and format_recruitment == "tuyển thpt" or format_recruitment == "thi thpt" or format_recruitment == "thptqg":
            dispatcher.utter_message(
                text = "- Xét tuyển điểm thi THPT:\n\
                        + Sàn chất lượng\n\
                        Điểm theo khối xét tuyển đạt từ trung bình trở lên (15**/30 điểm).\n\
                        + Điều kiện xét tuyển\n\
                        Thí sinh cần đạt xếp hạng theo điểm thi THPT năm 2020 thuộc Top50 THPT 2020\
                         (chứng nhận thực hiện trên trang http://SchoolRank.fpt.edu.vn theo số liệu Đại học FPT tổng hợp và công bố sau kỳ thi THPT 2020)\n")

        elif intent_recruitment == "recruitment" and format_recruitment == "ưu tiên":
            dispatcher.utter_message(
                text = "- Xét tuyển ưu tiên:\n\
                        Ưu tiên xét tuyển đối với thí sinh đạt một trong các điều kiện sau:\n\
                        1.Tốt nghiệp THPT ở nước ngoài\n\
                        2.Tiếng Anh TOEFL iBT từ 80 hoặc IELTS (Học thuật) từ 6.0 hoặc quy đổi tương đương (áp dụng đối với ngành Ngôn Ngữ Anh)\n\
                        3.Tiếng Nhật JLPT từ N3 trở lên (áp dụng đối với ngành Ngôn Ngữ Nhật)\n\
                        4.Tiếng Hàn TOPIK cấp độ 4 trong kỳ thi TOPIK II (áp dụng đối với ngành Ngôn Ngữ Hàn Quốc)\n\
                        5.Tốt nghiệp Chương trình APTECH HDSE (áp dụng đối với ngành Công nghệ thông tin)\n\
                        6.Tốt nghiệp Chương trình ARENA ADIM (áp dụng đối với chuyên ngành Thiết kế Mỹ thuật số)\n\
                        7.Tốt nghiệp Đại học.\n\
                        8.Sinh viên chuyển trường từ các trường đại học thuộc Top 1000 trong 3 bảng xếp hạng gần nhất: QS, ARWU và THE hoặc các trường đạt chứng nhận QS Star 5 sao về chất lượng đào tạo.\n")
        
        elif intent_recruitment == "recruitment" and format_recruitment == "tuyển thẳng":
            dispatcher.utter_message(
                text = "- Xét tuyển thẳng:\n\
                        Xét tuyển thẳng thí sinh thuộc diện được xét tuyển thẳng tại mục 2, Điều 7 trong Quy chế tuyển sinh Đại học, Cao đẳng hệ đại học chính quy của Bộ GD&ĐT năm 2020.\n")
            dispatcher.utter_message(
                text = "Bạn có thể tham khảo tại: https://bom.to/4Sv72xf")

        elif intent_recruitment == "recruitment" and format_recruitment == "tổ hợp" or format_recruitment == "khối":
            dispatcher.utter_message(
                text = "- Các tổ hợp môn xét tuyển:",
                image = "https://i.imgur.com/yQw1Xys.png")
        else:
            dispatcher.utter_message(
                template = "utter_recruitment"
            )
class transfer_university(Action):
    def name(self) -> Text:
        return "action_transfer_university"

    def run(self, dispatcher, tracker, domain):
        intent_transfer_university = str(tracker.latest_message['intent'].get('name'))
        if intent_transfer_university == "transfer_university":
            dispatcher.utter_message(
                text = "Sinh viên FPT Polytechnic được phép liên thông lên trình độ Đại học\
                     hệ chính quy của Trường Đại học FPT và các trường Đại học có tuyển liên thông tại ba chuyên ngành:\
                          Quản trị kinh doanh, Tài chính – Ngân hàng, Kỹ thuật phần mềm.\n")
            dispatcher.utter_message(
                text = "Bạn có thể xem chi tiết về liên thông tại đây ạ: https://bom.to/DNYfUGe")


        
        