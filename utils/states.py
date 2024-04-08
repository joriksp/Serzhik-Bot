from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    name = State()
    age = State()
    sex = State()
    about = State()
    photo = State()

class MakeAppeal(StatesGroup):
    name = State()
    title = State()
    message = State()