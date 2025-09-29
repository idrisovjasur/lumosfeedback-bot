import asyncpg
from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from handlers.users import text
from loader import db
from states.feedback import FeedBackStates
from keyboards.default.feedback import feedback_keyboard, submission_keyboard
from keyboards.default.text import anonymous_keyboard_text,identified_keyboard_text, yes, no
start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    try:
        await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
    except asyncpg.exceptions.UniqueViolationError:
        pass
    await message.answer(text.start_text,reply_markup=feedback_keyboard)

@start_router.message(F.text==anonymous_keyboard_text)
async def anonymous_feedback(message: Message, state: FSMContext):
    await message.answer(text.anonymous_feedback_response_text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(FeedBackStates.anonymous)

@start_router.message(F.text==identified_keyboard_text)
async def identified_feedback(message: Message, state: FSMContext):
    await message.answer(text.identified_feedback_response_text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(FeedBackStates.identified)


@start_router.message(FeedBackStates.anonymous, F.text)
async def anonymous_feedback_text(message: Message, state: FSMContext):
    feedback_text = message.text
    await state.update_data(feedback_text=feedback_text)
    await message.answer(text.text_1, reply_markup=submission_keyboard)
    await state.set_state(FeedBackStates.submitted_anonymous)


@start_router.message(FeedBackStates.identified, F.text)
async def identified_feedback_text(message: Message, state: FSMContext):
    feedback_text = message.text
    await state.update_data(feedback_text=feedback_text)
    await message.answer(text.user_name(message.from_user.full_name), reply_markup=submission_keyboard)
    await state.set_state(FeedBackStates.submitted_identified)

@start_router.message(FeedBackStates.submitted_anonymous, F.text)
async def submission_feedback_function(message: Message, state: FSMContext):
    if message.text == yes:
        data = await state.get_data()
        feedback_text = data.get("feedback_text")
        await message.answer(text.text_3)
    elif message.text == no:
        pass


@start_router.message(FeedBackStates.submitted_identified, F.text)
async def identified_feedback_function(message: Message, state: FSMContext):
    if message.text == yes:
        data = await state.get_data()
        feedback_text = data.get("feedback_text")
        await message.answer(text.text_4)
    elif message.text == no:
        pass






