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
from keyboards.default.text import people_type

start_text = """
Добро пожаловать в Lumos Feedback Bot ✨

Пожалуйста, выберите, как вы хотите отправить отзыв:

ℹ️ Если вы оставите обращение не анонимно и укажете свои контактные данные, 
ваше сообщение будет рассмотрено быстрее и меры будут приняты оперативнее.
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

school_type_text = """
Пожалуйста, выберите филиал вашей школы 👇
(Выберите, где вы учитесь — Чиланзар или Самарканд Дарвоза)
"""

people_type_text = """
👇 Пожалуйста, выберите, кто вы:
(Это нужно, чтобы мы могли правильно вас зарегистрировать)
"""

pupil_type_text = """
Укажите, в каком вы классе 👇
"""

pupil_name_text = """
📝 Пожалуйста, введите ваше имя и фамилию:
"""

pupil_phone_text = """
📞 Укажите ваш номер телефона (в формате +998...):
"""

pupil_class_text = """
🏫 Укажите ваш класс (например: 7А, 9Б и т.д.):
"""