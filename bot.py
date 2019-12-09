import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import *
from aiogram.types import *
from aiogram.types import ParseMode
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram.utils.markdown as md
import asyncio


TOKEN = "1056341881:AAEKYEkс-QVtKIмtzSgIFL06ahUIOnkPemo"
password = 'Zalupa9563'
admin_id = [771834617, 730668]
grin_pass_api = 'z1jvVcc2GH5BYgzbbR6K'
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)



help_message = """
Example: /cmd info
Commands: 
account -  List wallet accounts or create a new account 
cancel -  Cancels a previously created transaction, freeing previously locked outputs for use again
check -  Checks a wallet's outputs against a live node, repairing and restoring missing outputs if required
finalize -  Processes a receiver's transaction file to finalize a transfer.
help -  Prints this message or the help of the given subcommand(s)
info -  Basic wallet contents summary
init -  Initialize a new wallet seed file and database
invoice -  Initialize an invoice transaction.
listen -  Runs the wallet in listening mode waiting for transactions
outputs -  Raw wallet output info (list of outputs)
owner_api -  Runs the wallet's local web API
pay -  Spend coins to pay the provided invoice transaction
receive -  Processes a transaction file to accept a transfer from a sender
send -  Builds a transaction to send coins and sends to the specified listener directly
txs -  Display transaction information"""



button1 = KeyboardButton('GET Status')
button2 = KeyboardButton('GET TxHashSet Roots')
button3 = KeyboardButton('GET Pool')
button4 = KeyboardButton('GET Peers Connected')
button5 = KeyboardButton('Help')
button6 = KeyboardButton('Send GRIN')
markup3 = ReplyKeyboardMarkup().row(button1, button2)
markup3.row(button3, button4)
markup3.row(button5)
markup3.row(button6)



@dp.message_handler(text='inf') 
async def process_start_command(message: types.Message):
	if message['from']['id'] in admin_id:
		info = os.popen(f'grin-wallet -p {password} info').read()
		all_string = info.split('\n')[3] + '\n' + info.split('\n')[4] + '\n' + info.split('\n')[5] + '\n' + info.split('\n')[6] + '\n' + info.split('\n')[7][:-3] + '\n' + info.split('\n')[8]
		await message.reply('```' + all_string + '```', parse_mode=ParseMode.MARKDOWN, reply=False)
	else:
		await message.reply('Permissions denied', reply=False)





@dp.message_handler(text='GET Status') 
async def process_start_command(message: types.Message):
    if message['from']['id'] in admin_id:
        r = requests.get('http://localhost:3413/v1/status', auth=('grin', grin_pass_api))
        q = ' Protocol version: ' + str(r.json()['protocol_version']) + '\n User Agent: ' + r.json()['user_agent'] + '\n Connections: ' + str(r.json()['connections']) + '\n Height: ' + str(r.json()['tip']['height'])+ '\n Last block pushed: ' + r.json()['tip']['last_block_pushed'] + '\n Prev block to last: ' + r.json()['tip']['prev_block_to_last'] + '\n Total difficulty: ' + str(r.json()['tip']['total_difficulty'])+ '\n Sync status: ' + r.json()['sync_status']
        await message.reply('```' + q + '```', parse_mode=ParseMode.MARKDOWN, reply=False)
    else:
        await message.reply('Permissions denied', reply=False)

@dp.message_handler(text='GET TxHashSet Roots') 
async def process_start_command(message: types.Message):
    if message['from']['id'] in admin_id:
        r = requests.get('http://localhost:3413/v1/txhashset/roots', auth=('grin', grin_pass_api))
        q = ' Output root hash: ' + r.json()['output_root_hash'] + '\nRangeproof root hash: ' + r.json()['range_proof_root_hash'] + '\nKernel set root hash: ' + r.json()['kernel_root_hash']
        await message.reply('```' + q + '```', parse_mode=ParseMode.MARKDOWN, reply=False)
    else:
        await message.reply('Permissions denied', reply=False)

@dp.message_handler(text='GET Pool') 
async def process_start_command(message: types.Message):
    if message['from']['id'] in admin_id:
        r = requests.get('http://localhost:3413/v1/pool', auth=('grin', grin_pass_api))
        q = ' Number of transactions in the memory pool: ' + str(r.json()['pool_size'])
        await message.reply('```' + q + '```', parse_mode=ParseMode.MARKDOWN, reply=False)
    else:
        await message.reply('Permissions denied', reply=False)


@dp.message_handler(text='GET Peers Connected') 
async def process_start_command(message: types.Message):
    if message['from']['id'] in admin_id:
        r = requests.get('http://localhost:3413/v1/peers/connected', auth=('grin', grin_pass_api))
        users_info = ''
        for i in r.json():
            users_info = users_info + '\nCapabilities bits: ' + str(i['capabilities']['bits']) + '\nUser agent: ' + str(i['user_agent']) + '\nVersion: ' + str(['version']) + '\nAddress: ' + str(i['addr']) + '\ndirection: ' + str(i['direction']) + '\ntotal Difficulty: ' + str(i['total_difficulty']) + '\nheight: ' + str(i['height']) + '\n====================' 
        await message.reply('```' + users_info + '```', parse_mode=ParseMode.MARKDOWN, reply=False)
    else:
        await message.reply('Permissions denied', reply=False)

@dp.message_handler(text='Help') 
async def process_start_command(message: types.Message):
    if message['from']['id'] in admin_id:
       await message.reply('```' + help_message + '```',parse_mode=ParseMode.MARKDOWN, reply=False)	
    else:
        await message.reply('Permissions denied', reply=False)



@dp.message_handler(commands=['cmd'])
async def send_welcome(message: types.Message):
	if message['from']['id'] in admin_id:
		q = message.text.replace('/cmd ', '')
		info = os.popen(f'grin-wallet -p {password} {q}').read()
		await message.reply('```' + info + '```' ,parse_mode=ParseMode.MARKDOWN, reply=False)
	else:
		await message.reply('Permissions denied' ,parse_mode=ParseMode.MARKDOWN, reply=False)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
		with open('grin.png', 'rb') as photo:
			await message.reply_photo(photo, caption='For more information, pls use a /help', reply=False, reply_markup=markup3)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    if message['from']['id'] in admin_id:
        await message.reply('```' + help_message + '```',parse_mode=ParseMode.MARKDOWN, reply=False)
        await bot.delete_message(message.chat.id, message.message_id)
    else:
        await message.reply('Permissions denied' ,parse_mode=ParseMode.MARKDOWN, reply=False)    



# ExMachine Машина состояний

class Form(StatesGroup):
    method = State()  
    age = State() 
    gender = State() 
    yes_no = State()


@dp.message_handler(text='Send GRIN')
async def cmd_start(message: types.Message):
    if message['from']['id'] in admin_id:
        await Form.method.set()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("HTTP", "File")
        await message.reply("Choose method:", reply_markup=markup)
    else:
        await message.reply('Permissions denied' ,parse_mode=ParseMode.MARKDOWN, reply=False)



@dp.message_handler(state='*', text='Cancel')
@dp.message_handler(Text(equals='Cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Canceled.', reply_markup=markup3, reply=False)


@dp.message_handler(state=Form.method)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['method'] = message.text
    markup = types.ReplyKeyboardRemove()
    await Form.next()
    await message.reply("Input amount\nEx: 11.2", reply_markup=markup)



@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    await Form.next()
    await state.update_data(age=message.text)
    async with state.proxy() as data: 
        if data['method'] == 'File':
            request = 'grin-wallet -p ' + str(password) + ' send -d "transaction.tx" -m file ' + str(data['age'])
            info = os.popen(request)
            await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_DOCUMENT)
            await asyncio.sleep(1.8)
            with open('transaction.tx', 'rb') as grin_trans:
                await bot.send_document(message.from_user.id, grin_trans, caption='Payment ' + str(data['age']) + ' GRIN', reply_markup=markup3)
            await state.finish() 
        elif data['method'] == 'HTTP':   
            await message.reply("Input adress.\nEx:\n167.172.104.47:3415")



@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

        # Remove keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("Yes", "No")
        markup.add("Cancel")
        # And send message
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text('Sending ', md.code(data['age']) + ' GRIN'),
                md.text('on :', md.bold(data['method'])),
                md.text('To adress: ', data['gender']),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )

    await Form.next()

@dp.message_handler(state=Form.yes_no)
async def yes_no(message: types.Message, state: FSMContext):
    await state.update_data(yes_no=message.text)
    if message['from']['id'] in admin_id:
        async with state.proxy() as data:
            if data['yes_no'] == 'Yes':
                info = os.popen(f'grin-wallet -p {password} ' + 'send -d' + ' "' + 'http://' + str(data['gender']) + '" ' + str(data['age'])).read()
                await bot.send_message( message.chat.id, 'Trying', reply_markup=markup3)
                await bot.send_message( message.chat.id, info, reply_markup=markup3)
            else:
                await bot.send_message( message.chat.id, 'Canceled.', reply_markup=markup3)
        await state.finish()
    else:
        await message.reply('Permissions denied' ,parse_mode=ParseMode.MARKDOWN, reply=False)




@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc(message: types.Message):
    if message['from']['id'] in admin_id:
        if message.document.file_name.endswith('.response'):
            await bot.download_file_by_id(file_id=message.document.file_id, destination='trans.grinslate.response')
            await message.reply('File received, downloading.', reply=False)
            await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_DOCUMENT)
            await asyncio.sleep(1)
            info = os.popen(f'grin-wallet -p {password} ' + 'finalize -i trans.grinslate.response')
            await asyncio.sleep(1.5)
            if "successfully" in info.read():
                await message.reply('finalize OK', reply=False)
            else:
                await message.reply('During finalize an error has occurred!', reply=False)
        else:
            await message.reply('This file not match')
    else:
        await message.reply('Permisions denied' ,parse_mode=ParseMode.MARKDOWN, reply=False)

@dp.message_handler(commands=['fuck'])
async def send_welcome(message: types.Message):
    await message.reply('http://t.me/FuckFiat',parse_mode=ParseMode.MARKDOWN, reply=False)


thx_text = """
Thx to:

🔸@death_adept

🔸@ZeroCo0L 

🔸@ruchera 

🔸@pro2pop 

🔸@hashmapdev

Made with love in GRIN ❤️

Donate  http://167.172.104.47:3415 😜"""


@dp.message_handler(commands=['thx', 'thanks'])
async def send_welcome(message: types.Message):
    await message.reply(thx_text, reply=False)




if __name__ == '__main__':
	print("starting")
	executor.start_polling(dp, skip_updates=True)
