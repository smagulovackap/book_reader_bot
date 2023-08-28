from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON
from services.file_handling import book

def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
	#Keyboard object creating
	kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
	#Adding buttons-bookmarks ascending
	for button in sorted(args):
		kb_builder.row(InlineKeyboardButton(
			text=f'{button} - {book[button][:100]}',
			callback_data=str(button)))
	#edit and cancel buttons adding
	kb_builder.row(InlineKeyboardButton(
						text=LEXICON['edit_bookmarks_button'],
						callback_data='edit_bookmarks'),
					InlineKeyboardButton(
						text=LEXICON['cancel'],
						callback_data='cancel'),
					width=2)
	return kb_builder.as_markup()

def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
	#Keyboard object creating
	kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
	#Adding buttons-bookmarks ascending
	for button in sorted(args):
		kb_builder.row(InlineKeyboardButton(
			text=f'{LEXICON["del"]} {button} - {book[button][:100]}',
			callback_data=f'{button}del'))
	#cancel button adding
	kb_builder.row(InlineKeyboardButton(
		text=LEXICON['cancel'],
		callback_data='cancel'))
	return kb_builder.as_markup()