from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from keyboards.default import text
feedback_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=text.anonymous_keyboard_text),
         KeyboardButton(text=text.identified_keyboard_text)
         ],

    ],
    resize_keyboard=True,
)

submission_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=text.yes), KeyboardButton(text=text.no)]
    ],
    resize_keyboard=True,
)