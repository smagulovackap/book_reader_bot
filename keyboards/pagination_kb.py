from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON

#book page keyboard generating func
def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
	#initializing builder
	kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
	#add row with buttons to builder
	kb_builder.row(*[InlineKeyboardButton(
		text=LEXICON[button] if button in LEXICON else button,
		callback_data=button) for button in buttons])
	#inline keyboard object return
	return kb_builder.as_markup()
