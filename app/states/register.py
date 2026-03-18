from aiogram.fsm.state import State, StatesGroup

class Register(StatesGroup):
    name = State()
    phone = State()
    age = State()
    course = State()