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

school_type_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=text.school_type.get('1')), KeyboardButton(text=text.school_type.get('2'))],
    ],
    resize_keyboard=True
)

people_type_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=text.people_type.get('1')), KeyboardButton(text=text.people_type.get('2'))],
        [KeyboardButton(text=text.people_type.get('3'))],
    ], resize_keyboard=True
)
pupil_type_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=text.pupil_type.get('1')), KeyboardButton(text=text.pupil_type.get('2'))],
    ], resize_keyboard=True
)