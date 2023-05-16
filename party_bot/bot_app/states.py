from aiogram.fsm.state import State, StatesGroup


class PersonStates(StatesGroup):
    start = State()
    show_all = State()
    show_last = State()
