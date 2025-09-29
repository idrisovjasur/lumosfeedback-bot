start_text = """
Welcome to Lumos Feedback Bot ✨
Please choose how you want to send feedback:
"""

anonymous_feedback_response_text = """
✍️ Please write your feedback below.  
(Your name will NOT be shown to admins.)
"""
identified_feedback_response_text = """
✍️ Please write your feedback below.  
(This feedback will include your name.)
"""
text_1 = """
✅ Do you want to submit this feedback?
"""

def user_name(name: str) -> str:
    text_2 = f"""
    ✅ Do you want to submit this feedback with your name (<b>{name}</b>)?
    """
    return text_2

text_3 = """
Your anonymous feedback has been submitted successfully. Thank you 🙏
"""
text_4 = """
Your feedback has been submitted with your name. Thank you 🙏
"""