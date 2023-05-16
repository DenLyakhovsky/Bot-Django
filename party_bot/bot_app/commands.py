from aiogram.filters import Command
from aiogram.types import Message
from .app import router
from .fetcher import get_all_person
from .states import PersonStates
from aiogram.fsm.context import FSMContext


@router.message(Command(commands='start'))
async def start_handler(message: Message):
    await message.answer('<b>Команди</b>: \n/show_all - виклик всіх запрошених \n/show_new - виклик лише нових user',
                         parse_mode='HTML')


@router.message(Command(commands=["show_all"]))
async def all_person_handler(message: Message, state: FSMContext):
    res = await get_all_person()

    await message.answer('Імена всіх запрошених:')
    for data in res:
        id = data.get('pk')
        name = data.get('name')
        last_name = data.get('last_name')
        await message.answer(f"<b>ID</b>: <u>{id}</u> \n{name} {last_name}", parse_mode='HTML')


@router.message(Command(commands=['show_new']))
async def new_person(message: Message):
    res = []
    id = res.get('pk')
    name = res.get('name')
    last_name = res.get('last_name')
    # await message.answer(f"<b>ID</b>: <u>{id}</u> \n{name} {last_name}", parse_mode='HTML')
    await message.answer(f"{res}", parse_mode='HTML')
