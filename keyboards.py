from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
import re
import asyncio
import linecache

user = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="💬 Отправить запрос")],
    [KeyboardButton(text="❓ FAQ"), KeyboardButton(text="📊 Up-time")]
], one_time_keyboard=True)

ais = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="[РЕКОМЕНДУЕМЫЙ] ⚡️ Gemini Flash 2.0")],
    [KeyboardButton(text="🐳 DeepSeek")],
    [KeyboardButton(text="⚡️ Gemini Flash 1.5")],
    [KeyboardButton(text="🦕 Meta Llama 4 Scout")],
    [KeyboardButton(text="🥝 Gemma 3 4B")],
    [KeyboardButton(text="👾 Qwen3 8B")],
    [KeyboardButton(text="🎃 Ministral Small 3")],
    [KeyboardButton(text="⬅️ Вернуться в главное меню")]
], one_time_keyboard=True)