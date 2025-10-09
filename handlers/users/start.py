from logging import exception

import asyncpg
from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from handlers.users import text
from loader import db
from states.feedback import FeedBackStates
from keyboards.default.feedback import feedback_keyboard, submission_keyboard, school_type_keyboard, people_type_keyboard, pupil_type_keyboard
from keyboards.default.text import anonymous_keyboard_text,identified_keyboard_text, yes, no, school_type, people_type, pupil_type
start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    user = await db.select_user(telegram_id=message.from_user.id)
    if user:
        await message.answer(text.start_text, reply_markup=feedback_keyboard)
        await state.clear()
    else:
        await state.set_state(FeedBackStates.school_type)
        await message.answer(text.school_type_text,reply_markup=school_type_keyboard)

@start_router.message(FeedBackStates.school_type, F.text.in_([school_type.get('2'),school_type.get('1')]))
async def school_type_function(message: Message, state: FSMContext):
    school = message.text
    await state.update_data(school=school)
    await message.answer(text=text.people_type_text,reply_markup=people_type_keyboard)
    await state.set_state(FeedBackStates.people_type)

@start_router.message(FeedBackStates.people_type, F.text.in_([people_type.get('1'),people_type.get('2'), people_type.get('3')]))
async def people_type_function(message: Message, state: FSMContext):
    people = message.text
    await state.update_data(people=people)
    if people == people_type.get('1'):
        await message.answer(text=text.pupil_type_text, reply_markup=pupil_type_keyboard)
        await state.set_state(FeedBackStates.pupil_type)
    else:
        data = await state.get_data()
        school = data.get('school', None)
        people = data.get('people', None)
        try:
            await db.add_user(
                full_name=message.from_user.full_name,
                username=message.from_user.username,
                telegram_id=message.from_user.id,
                school=school,
                people=people,
                pupil=None
            )
            await message.answer(text.start_text, reply_markup=feedback_keyboard)
            await state.clear()
        except Exception as e:
            print(e)

@start_router.message(FeedBackStates.pupil_type, F.text.in_([pupil_type.get('1'),pupil_type.get('2')]))
async def pupil_type_function(message: Message, state: FSMContext):
    pupil = message.text
    await state.update_data(pupil=pupil)
    data = await state.get_data()
    school = data.get('school', None)
    pupil = data.get('pupil', None)
    people = data.get('people', None)
    try:
        await db.add_user(
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            telegram_id=message.from_user.id,
            school=school,
            people=people,
            pupil=pupil
        )
        await message.answer(text.start_text, reply_markup=feedback_keyboard)
        await state.clear()
    except Exception as e:
        print(e)


@start_router.message(F.text==identified_keyboard_text)
async def identified_feedback(message: Message, state: FSMContext):
    telegram_id = message.from_user.id
    user = await db.select_user(telegram_id=telegram_id)
    people = user[4]
    if people == people_type.get('1'):
        await message.answer(text.pupil_name_text, reply_markup=ReplyKeyboardRemove())
        await state.update_data(people=people, pupil=user[5], school=user[6])
        await state.set_state(FeedBackStates.pupil_name)
    elif people == people_type.get('2'):
        await message.answer('')
    elif people == people_type.get('3'):
        await message.answer('')
    # await message.answer(text.identified_feedback_response_text, reply_markup=ReplyKeyboardRemove())
    # await state.set_state(FeedBackStates.identified)

@start_router.message(FeedBackStates.pupil_name, F.text)
async def pupil_name_func(message: Message, state: FSMContext):
    pupil_name = message.text
    await state.update_data(pupil_name=pupil_name)
    await message.answer(text.pupil_phone_text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(FeedBackStates.pupil_phone)


@start_router.message(FeedBackStates.pupil_phone, F.text)
async def pupil_name_func(message: Message, state: FSMContext):
    pupil_phone = message.text
    await state.update_data(pupil_phone=pupil_phone)
    await message.answer(text.pupil_class_text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(FeedBackStates.pupil_class)

@start_router.message(FeedBackStates.pupil_class, F.text)
async def pupil_name_func(message: Message, state: FSMContext):
    pupil_class = message.text
    await state.update_data(pupil_class=pupil_class)
    await message.answer(text.identified_feedback_response_text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(FeedBackStates.identified)

@start_router.message(FeedBackStates.identified, F.text)
async def identified_feedback_text(message: Message, state: FSMContext):
    feedback_text = message.text
    await state.update_data(feedback_text=feedback_text)
    data = await state.get_data()
    data_text = (
        f"📋 <b>Проверьте, пожалуйста, ваши данные:</b>\n\n"
        f"{data['people']}\n"
        f"{data['pupil']}\n"
        f"{data['school']}\n\n"
        f"👤 <b>Имя и фамилия:</b> {data['pupil_name']}\n"
        f"📞 <b>Телефон:</b> {data['pupil_phone']}\n"
        f"🏫 <b>Класс:</b> {data['pupil_class']}\n\n"
        f"💬 <b>Ваш отзыв:</b>\n{data['feedback_text']}\n\n"
        f"✅ Отправить эти данные?"
    )
    await message.answer(data_text, reply_markup=submission_keyboard)
    await state.set_state(FeedBackStates.submitted_identified)


@start_router.message(FeedBackStates.submitted_identified, F.text)
async def identified_feedback_function(message: Message, state: FSMContext):
    if message.text == yes:
        data = await state.get_data()
        feedback_text = data.get("feedback_text")
        try:
            await db.add_identified_feedback(
                telegram_id=message.from_user.id,
                feedback=feedback_text,
                username=message.from_user.username,
                full_name=message.from_user.full_name,
                status=False
            )
            await state.clear()
            await message.answer(text.text_4, reply_markup=feedback_keyboard)
        except asyncpg.exceptions.UniqueViolationError:
            print('error')

    elif message.text == no:
        await message.answer(no, reply_markup=feedback_keyboard)
        await state.clear()





@start_router.message(F.text==anonymous_keyboard_text)
async def anonymous_feedback(message: Message, state: FSMContext):
    await message.answer(text.anonymous_feedback_response_text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(FeedBackStates.anonymous)


@start_router.message(FeedBackStates.anonymous, F.text)
async def anonymous_feedback_text(message: Message, state: FSMContext):
    feedback_text = message.text
    await state.update_data(feedback_text=feedback_text)
    await message.answer(text.text_1, reply_markup=submission_keyboard)
    await state.set_state(FeedBackStates.submitted_anonymous)


@start_router.message(FeedBackStates.submitted_anonymous, F.text)
async def submission_feedback_function(message: Message, state: FSMContext):
    if message.text == yes:
        data = await state.get_data()
        feedback_text = data.get("feedback_text")
        try:
            await db.add_anonymous_feedback(
                telegram_id=message.from_user.id,
                feedback=feedback_text,
                username=message.from_user.username,
                status=False
            )
            await state.clear()
        except exception as e:
            print(e)
        await message.answer(text.text_3, reply_markup=feedback_keyboard)
    elif message.text == no:
        await message.answer(text = no, reply_markup=feedback_keyboard)
        await state.clear()







