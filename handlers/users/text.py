# start_text = """
# Welcome to Lumos Feedback Bot ✨
# Please choose how you want to send feedback:
# """
#
# anonymous_feedback_response_text = """
# ✍️ Please write your feedback below.
# (Your name will NOT be shown to admins.)
# """
# identified_feedback_response_text = """
# ✍️ Please write your feedback below.
# (This feedback will include your name.)
# """
# text_1 = """
# ✅ Do you want to submit this feedback?
# """
#
# def user_name(name: str) -> str:
#     text_2 = f"""
#     ✅ Do you want to submit this feedback with your name (<b>{name}</b>)?
#     """
#     return text_2
#
# text_3 = """
# Your anonymous feedback has been submitted successfully. Thank you 🙏
# """
# text_4 = """
# Your feedback has been submitted with your name. Thank you 🙏
# """
start_text = """
Добро пожаловать в Lumos Feedback Bot ✨
Пожалуйста, выберите, как вы хотите отправить отзыв:
"""

anonymous_feedback_response_text = """
✍️ Пожалуйста, напишите свой отзыв ниже.  
(Ваше имя НЕ будет показано администраторам.)
"""

identified_feedback_response_text = """
✍️ Пожалуйста, напишите свой отзыв ниже.  
(Этот отзыв будет отправлен вместе с вашим именем.)
"""

text_1 = """
✅ Вы хотите отправить этот отзыв?
"""

def user_name(name: str) -> str:
    text_2 = f"""
    ✅ Вы хотите отправить этот отзыв вместе со своим именем (<b>{name}</b>)?
    """
    return text_2

text_3 = """
Ваш анонимный отзыв был успешно отправлен. Спасибо 🙏
"""

text_4 = """
Ваш отзыв был успешно отправлен вместе с вашим именем. Спасибо 🙏
"""
