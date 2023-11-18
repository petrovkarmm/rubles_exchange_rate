from aiogram.fsm.state import State, StatesGroup


class Register(StatesGroup):
    start_registration = State()
    end_registration = State()