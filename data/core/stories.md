## muon gap tu van vien
* greeting
   - utter_greet
* request_meet_staff
   - utter_request_meet_staff
* call_method{"call":"gọi điện"}
   - action_required_staff
   - get_info_user_form
   - form{"name":"get_info_user_form"}
   - form{"name": null}
   - utter_slots_values
   - utter_done
* thanks
   - utter_thanks

## yeu cau gap tu van vien luon
* request_meet_staff
   - utter_request_meet_staff
* call_method{"call":"gọi điện"}
   - action_required_staff
   - get_info_user_form
   - form{"name":"get_info_user_form"}
   - form{"name": null}
   - utter_slots_values
   - utter_done

## muon nhan tin voi tu van vien
* greeting
   - utter_greet
* request_meet_staff
   - utter_request_meet_staff
* message_method{"message":"nhắn tin"}
   - action_required_staff

## yeu cau goi dien luon cho tu van vien
* call_method{"call":"gọi điện"}
   - action_required_staff
   - get_info_user_form
   - form{"name":"get_info_user_form"}
   - form{"name": null}
   - utter_slots_values
   - utter_done
* thanks
   - utter_thanks

## yeu cau nhan tin voi tu van vien
* request_meet_staff
   - utter_request_meet_staff
* message_method{"message":"nhắn tin"}
   - action_required_staff

## dien form giua chung roi huy
* greeting
   - utter_greet
* request_meet_staff
   - utter_request_meet_staff
* call_method{"call":"gọi điện"}
   - action_required_staff
   - get_info_user_form
   - form{"name":"get_info_user_form"}
* out_of_scope
   - utter_ask_continue
* deny
   - action_deactivate_form
   - form{"name": null}
   - utter_bye_bye

## dien form xong huy roi lai dien tiep
* greeting
   - utter_greet
* request_meet_staff
   - utter_request_meet_staff
* call_method{"call":"gọi điện"}
   - action_required_staff
   - get_info_user_form
   - form{"name":"get_info_user_form"}
* out_of_scope
   - utter_ask_continue
* affirm
   - get_info_user_form
   - form{"name":"get_info_user_form"}
   - utter_slots_values
   - utter_done

## hoi thong tin ve chuyen nganh
* greeting
   - utter_greet
* info_major
   - action_major
* info_major
   - action_major

## advisory, tuition, complain
* greeting
   - utter_greet
* advisory
   - utter_advisory
* tuition
   - utter_tuition
* complain
   - utter_complain
   - utter_after_complain
* affirm
   - utter_request_meet_staff
* message_method{"message":"nhắn tin"}
   - action_required_staff

## recruitment, info_major, tuition
* greeting
   - utter_greet
* recruitment
   - action_recruitment
* info_major
   - action_major
* tuition
   - utter_tuition
* thanks
   - utter_thanks
* bye_bye
   - utter_bye_bye

## advisory, info_major, tuition
* greeting
   - utter_greet
* advisory
   - utter_advisory
* info_major
   - action_major
* tuition
   - utter_tuition

## hoi thong tin chuyen nganh roi hoi hoc phi va dia diem
* greeting
   - utter_greet
* recruitment
   - action_recruitment
* info_major
   - action_major
* tuition
   - utter_tuition
* location
   - utter_location
* thanks
   - utter_thanks

## advisory, english, tuition, complain, call_method.
* greeting
   - utter_greet
* advisory
   - utter_advisory
* english
   - action_english
* tuition
   - utter_tuition
* complain
   - utter_complain
   - utter_after_complain
* affirm
   - utter_request_meet_staff
* call_method{"call":"gọi điện"}
   - action_required_staff
   - get_info_user_form
   - form{"name":"get_info_user_form"}
   - form{"name": null}
   - utter_slots_values
   - utter_done

## yeu cau tu van roi hoi thong tin chuyen nganh va muon gap tu van vien
* greeting
   - utter_greet
* advisory
   - utter_advisory
* info_major
   - action_major
* request_meet_staff
   - utter_request_meet_staff
* call_method{"call":"gọi điện"}
   - action_required_staff
   - get_info_user_form
   - form{"name":"get_info_user_form"}
   - form{"name": null}
   - utter_slots_values
   - utter_done

## chào hỏi rồi tạm biệt
* greeting
   - utter_greet
* thanks
   - utter_thanks

## hoi ve thong tin chuyen nganh roi hoi ve cong viec
* greeting
   - utter_greet
* info_major
   - action_major
* jobs
   - utter_jobs
* thanks
   - utter_thanks

## hoi nhieu thu
* greeting
   - utter_greet
* ask_func_bot
   - utter_ask_func_bot
* advisory
   - utter_advisory
* info_major
   - action_major
* tuition
   - utter_tuition
* english
   - action_english
* thanks
   - utter_thanks
* bye_bye
   - utter_bye_bye

## linh tinh
* greeting
   - utter_greet
* ask_func_bot
   - utter_ask_func_bot
* love_bot
   - utter_love_bot
* thanks
   - utter_thanks
* bye_bye
   - utter_bye_bye

## hoi chuc nang va yeu cau gap tu van vien
* greeting
   - utter_greet
* ask_func_bot
   - utter_ask_func_bot
* request_meet_staff
   - utter_request_meet_staff
* message_method{"message":"nhắn tin"}
   - action_required_staff

##  hoi dia diem
* greeting
   - utter_greet
* advisory
   - utter_advisory
* location
   - utter_location
* thanks
   - utter_thanks

## hoi dia diem
* location
   - utter_location
* thanks
   - utter_thanks

## hoi dia diem thong tin chuyen nganh hoc phi va tieng anh
* greeting
   - utter_greet
* location
   - utter_location
* recruitment
   - action_recruitment
* info_major
   - action_major
* tuition
   - utter_tuition
* english
   - action_english
* thanks
   - utter_thanks
* bye_bye
   - utter_bye_bye

## xin chao 
* greeting
   - utter_greet
* greeting
   - utter_greet
* greeting
   - utter_greet

## xin chao
* greeting
   - utter_greet

## tam biet
* bye_bye
   - utter_bye_bye

## thanks
* thanks
   - utter_thanks

## xin chao + tam biet
* greeting
   - utter_greet
* bye_bye
   - utter_bye_bye
* thanks
   - utter_thanks
* bye_bye
   - utter_bye_bye

## hoc phi
* tuition
   - utter_tuition

## yeu cau tu van
* advisory
   - utter_advisory

## hoi hoc phi, tieng anh va yeu cau gap tu van vien
* recruitment
   - action_recruitment
* tuition
   - utter_tuition
* english
   - action_english
* request_meet_staff
   - utter_request_meet_staff
* message_method{"message":"nhắn tin"}
   - action_required_staff
* thanks
   - utter_thanks

## tien hoc va tieng anh
* greeting
   - utter_greet
* advisory
   - utter_advisory
* tuition
   - utter_tuition
* english
   - action_english

## greeting advisory location english info_major request_meet_staff
* greeting
   - utter_greet
* advisory
   - utter_advisory
* recruitment
   - action_recruitment
* tuition
   - utter_tuition
* location
   - utter_location
* english
   - action_english
* info_major
   - action_major
* request_meet_staff
   - utter_request_meet_staff
* message_method{"message":"nhắn tin"}
   - action_required_staff

## hoi tu van tuyen sinh va tieng anh
* greeting
    - utter_greet
* recruitment
   - action_recruitment
* english
   - action_english
* thanks
   - utter_thanks
* bye_bye
   - utter_bye_bye

## New Story
* greeting
   - utter_greet
* english
   - action_english
* thanks
   - utter_thanks

## new story 2
* greeting
   - utter_greet
* recruitment
   - action_recruitment
* info_major
   - action_major
* jobs
   - utter_jobs
* thanks
   - utter_thanks

## new story 3
* greeting
   - utter_greet
* jobs
   - utter_jobs

## new story 4
* advisory
   - utter_advisory
* recruitment
   - action_recruitment
* info_major
   - action_major
* jobs
   - utter_jobs
* thanks
   - utter_thanks

## new story 5
* advisory
   - utter_advisory
* tuition
   - utter_tuition
* KTX
   - utter_KTX
* jobs
   - utter_jobs

## new story 6
* greeting
   - utter_greet
* ask_func_bot
   - utter_ask_func_bot
* love_bot
   - utter_love_bot
* advisory
   - utter_advisory
* english
   - action_english
* thanks
   - utter_thanks

## new story 7
* KTX
   - utter_KTX
* info_major
   - action_major
* jobs
   - utter_jobs
* thanks
   - utter_thanks
* love_bot
   - utter_love_bot

## new story 8
* greeting
   - utter_greet
* english
   - action_english

## new story 9
* english
   - action_english
* english
   - action_english
* english

## new story 10
* greeting
   - utter_greet
* english
   - action_english
* english
   - action_english
* info_major
   - action_major
* request_meet_staff
   - utter_request_meet_staff
* message_method{"message":"nhắn tin"}
   - action_required_staff

## new story 11
* ask_func_bot
   - utter_ask_func_bot
* KTX
   - utter_KTX
* profile
   - action_for_profile
* jobs
   - utter_jobs
* thanks
   - utter_thanks
* info_major
   - action_major
* tuition
   - utter_tuition
* recruitment
   - action_recruitment

## new story 11
* greeting
   - utter_greet
* KTX
   - utter_KTX
* thanks
   - utter_thanks

## linh tinh 2
* greeting
   - utter_greet
* love_bot
   - utter_love_bot
* ask_func_bot
   - utter_ask_func_bot
* bye_bye
   - utter_bye_bye
* thanks
   - utter_thanks

## new story 12
* recruitment
   - action_recruitment
* recruitment
   - action_recruitment
* recruitment
   - action_recruitment

## new story 13
* greeting
   - utter_greet
* recruitment
   - action_recruitment
* info_major
   - action_major
* tuition
   - utter_tuition
* profile
   - action_for_profile
* thanks
   - utter_thanks

## New Story 14
* greeting
   - utter_greet
* english
   - action_english
* tuition
   - utter_fallback

## New Story 15
* jobs
   - utter_jobs
* location
   - utter_location
* profile
   - action_for_profile
* english
   - action_english
* KTX
   - utter_KTX
* love_bot
   - utter_love_bot

## New Story 16
* KTX
   - utter_KTX
* recruitment
   - action_recruitment
* tuition
   - utter_tuition
* info_major
   - action_major
* request_meet_staff
   - utter_request_meet_staff
* call_method{"call":"gọi điện"}
   - action_required_staff
   - get_info_user_form
   - form{"name":"get_info_user_form"}
   - form{"name": null}
   - utter_slots_values
   - utter_done
* love_bot
   - utter_love_bot

## New Story 17
* info_major
   - action_major
* tuition
   - utter_tuition
* KTX
   - utter_KTX
* jobs
   - utter_jobs
* location
   - utter_location
* thanks
   - utter_thanks

## New Story 18
* greeting
   - utter_greet
* recruitment
   - action_recruitment
* recruitment
   - action_recruitment
* thanks
   - utter_thanks
* info_major
   - action_major
* tuition
   - utter_tuition
* thanks
   - utter_thanks

## New Story 19
* greeting
   - utter_greet
* transfer_university
   - action_transfer_university
* thanks
   - utter_thanks

## New Story 20
* transfer_university
   - action_transfer_university
* transfer_university
   - action_transfer_university
* transfer_university
   - action_transfer_university

## New Story 21
* greeting
   - utter_greet
* transfer_university
   - action_transfer_university
* love_bot
   - utter_love_bot
* thanks
   - utter_thanks

## New Story 22
* advisory
   - utter_advisory
* scholarship
   - utter_scholarship
* tuition
   - utter_tuition
* english
   - action_english
* info_major
   - action_major

## New Story 23
* scholarship
   - utter_scholarship
* scholarship
   - utter_scholarship

## New Story 24
* greeting
   - utter_greet
* transfer_university
   - action_transfer_university
* request_meet_staff
   - utter_request_meet_staff
* call_method{"call":"gọi điện"}
   - action_required_staff
   - get_info_user_form
   - form{"name":"get_info_user_form"}
   - form{"name": null}
   - utter_slots_values
   - utter_done
* thanks
   - utter_thanks

## New Story 25
* greeting
   - utter_greet
* transfer_university
   - action_transfer_university
* request_meet_staff
   - utter_request_meet_staff
* message_method{"message":"nhắn tin"}
   - action_required_staff

## New Story 26
* greeting
   - utter_greet
* advisory
   - utter_advisory
* scholarship
   - utter_scholarship
* info_major
   - action_major
* tuition
   - utter_tuition
* jobs
   - utter_jobs
* thanks
   - utter_thanks

## New Story 27
* greeting
   - utter_greet
* ask_func_bot
   - utter_ask_func_bot
* advisory
   - utter_advisory
* thanks
   - utter_thanks
* location
   - utter_location
* KTX
   - utter_KTX
* love_bot
   - utter_love_bot
* recruitment
   - action_recruitment
* thanks
   - utter_thanks
* bye_bye
   - utter_bye_bye

## New Story 28
* location
   - utter_location
* KTX
   - utter_KTX
* thanks
   - utter_thanks
* info_major
   - action_major
* tuition
   - utter_tuition
* scholarship
   - utter_scholarship
* complain
   - utter_complain
   - utter_after_complain
* affirm
   - utter_request_meet_staff
* call_method{"call":"gọi điện"}
   - action_required_staff
   - get_info_user_form
   - form{"name":"get_info_user_form"}
   - form{"name": null}
   - utter_slots_values
   - utter_done

## New Story 29
* love_bot
   - utter_love_bot
* love_bot
   - utter_love_bot
* love_bot
   - utter_love_bot

## New Story 30
* recruitment
   - action_recruitment
* info_major
   - action_major
* info_major
   - action_major
* scholarship
   - utter_scholarship
* ask_func_bot
   - utter_ask_func_bot
* complain
   - utter_complain
   - utter_after_complain
* affirm
   - utter_request_meet_staff
* message_method{"message":"nhắn tin"}
   - action_required_staff

## New Story 31
* ask_func_bot
   - utter_ask_func_bot
* love_bot
   - utter_love_bot
* advisory
   - utter_advisory
* recruitment
   - action_recruitment
* complain
   - utter_complain
   - utter_after_complain
* deny
   - utter_confirm
* deny
   - utter_bye_bye
* thanks
   - utter_thanks

## New Story 32
* transfer_university
   - action_transfer_university
* complain
   - utter_complain
   - utter_after_complain
* deny
   - utter_confirm
* affirm
   - utter_greet
* advisory
   - utter_advisory
* location
   - utter_location
* info_major
   - action_major
* english
   - action_english
* thanks
   - utter_thanks

## New Story 33
* ask_func_bot
   - utter_ask_func_bot
* scholarship
   - utter_scholarship
* complain
   - utter_complain
   - utter_after_complain
* deny
   - utter_confirm
* affirm
   - utter_greet
* greeting
   - utter_greet
* jobs
   - utter_jobs

## New Story 34
* greeting
   - utter_greet
* scholarship
   - utter_scholarship
* jobs
   - utter_jobs
* location
   - utter_location
* info_major
   - action_major

## New 1
* profile
   - action_for_profile
* profile
   - action_for_profile
* profile
   - action_for_profile

## New 2
* greeting
   - utter_greet
* profile
   - action_for_profile
* tuition
   - utter_tuition
* KTX
   - utter_KTX
* info_major
   - action_major
* jobs
   - utter_jobs

## New 3
* profile
   - action_for_profile
* scholarship
   - utter_scholarship
* location
   - utter_location
* KTX
   - utter_KTX
* scholarship
   - utter_scholarship
   
## New Story 35
* ask_func_bot
   - utter_ask_func_bot
* greeting
   - utter_greet
* scholarship
   - utter_scholarship
* tuition
   - utter_tuition
* location
   - utter_location
* KTX
   - utter_KTX
* advisory
   - utter_advisory
* recruitment
   - action_recruitment
* english
   - action_english
* info_major
   - action_major
* jobs
   - utter_jobs
* transfer_university
   - action_transfer_university
* complain
   - utter_complain
   - utter_after_complain
* deny
   - utter_confirm
* deny
   - utter_bye_bye
* thanks
   - utter_thanks

## New Story 36
* greeting
   - utter_greet
* ask_func_bot
   - utter_ask_func_bot
* scholarship
   - utter_scholarship
* info_major
   - action_major
* advisory
   - utter_advisory
* tuition
   - utter_tuition
* profile
   - action_for_profile
* english
   - action_english
* KTX
   - utter_KTX
* recruitment
   - action_recruitment
* location
   - utter_location
* transfer_university
   - action_transfer_university
* jobs
   - utter_jobs
* love_bot
   - utter_love_bot
* thanks
   - utter_thanks

## New Story 37
* greeting
   - utter_greet
* info_major
   - action_major 
* profile
   - action_for_profile 
* scholarship
   - utter_scholarship 
* transfer_university
   - action_transfer_university 
* location
   - utter_location 
* thanks
   - utter_thanks 
* KTX
   - utter_KTX 
* english
   - action_english 
* love_bot
   - utter_love_bot 
* advisory
   - utter_advisory 
* recruitment
   - action_recruitment 
* tuition
   - utter_tuition 
* ask_func_bot
   - utter_ask_func_bot 
* jobs
   - utter_jobs

## New Story 38
* info_major
   - action_major
* location
   - utter_location
* english
   - action_english
* love_bot
   - utter_love_bot
* ask_func_bot
   - utter_ask_func_bot
* recruitment
   - action_recruitment
* transfer_university
   - action_transfer_university
* KTX
   - utter_KTX
* profile
   - action_for_profile
* greeting
   - utter_greet
* tuition
   - utter_tuition
* advisory
   - utter_advisory
* scholarship
   - utter_scholarship
* thanks
   - utter_thanks  
* jobs
   - utter_jobs

## New Story 39
* location
   - utter_location
* tuition
   - utter_tuition
* scholarship
   - utter_scholarship
* transfer_university
   - action_transfer_university
* ask_func_bot
   - utter_ask_func_bot
* KTX
   - utter_KTX
* greeting
   - utter_greet
* info_major
   - action_major
* advisory
   - utter_advisory
* jobs
   - utter_jobs 
* recruitment
   - action_recruitment
* english
   - action_english
* profile
   - action_for_profile
* thanks
   - utter_thanks
* love_bot
   - utter_love_bot

## New Story 40
* profile
   - action_for_profile
* KTX
   - utter_KTX 
* english
   - action_english
* jobs
   - utter_jobs
* tuition
   - utter_tuition
* thanks
   - utter_thanks

## New Story 41
* profile
   - action_for_profile
* english
   - action_english
* info_major
   - action_major
* location
   - utter_location
* tuition
   - utter_tuition
* KTX
   - utter_KTX
* thanks
   - utter_thanks

## New Story 42
* greeting
   - utter_greet
* info_major
   - action_major
* location
   - utter_location
* profile
   - action_for_profile
* KTX
   - utter_KTX
* jobs
   - utter_jobs
* scholarship
   - utter_scholarship