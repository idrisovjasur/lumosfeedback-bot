from aiogram.fsm.state import StatesGroup, State


class FeedBackStates(StatesGroup):
    anonymous = State()
    identified = State()
    submitted_anonymous = State()
    submitted_identified = State()
    school_type = State()
    people_type = State()
    pupil_type = State()
    pupil_name = State()
    pupil_phone = State()
    pupil_class = State()
