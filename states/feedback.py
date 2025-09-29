from aiogram.fsm.state import StatesGroup, State


class FeedBackStates(StatesGroup):
    anonymous = State()
    identified = State()
    submitted_anonymous = State()
    submitted_identified = State()
