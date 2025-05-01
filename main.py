from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, CallbackQuery, Message
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InputFile, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, FSInputFile, InputMediaPhoto
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os
import asyncio
import datetime
import re
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery
import aiogram.utils.markdown as fmt
from openai import OpenAI

import keyboards as kb
import requests
import json

bot = Bot(token="7848224373:AAFOqRSfTnjJG_sJGNvNsbY4gtmEdijOWVk")
dp = Dispatcher()

class DataAll(StatesGroup):
    isAsking = State()
    model = State()

@dp.message(Command('start'))
async def WelcomeMessage(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIBC2gTsp0welf6a_ohAAGEz17zAtaJlQACiP0xG9gooEjpT54ONxBU6wEAAwIAA3kAAzYE", parse_mode="html", caption="👋 Привет, это <b>teleAI.</b> Здесь собраны различные нейросетевые модели, такие как <b>Gemini Flash 2.0, DeepSeek</b> и другие.\n\n🔥 И Все они абсолютно <b>бесплатны :D</b>", reply_markup=kb.user)

@dp.message(F.text == "💬 Отправить запрос")
async def SelectAI(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIBCWgTskd8hOOgIRadfx36kQhSGQPbAAKG_TEb2CigSD3H3uTP2OZEAQADAgADeQADNgQ", caption="👌 Окей, выбери подходящую нейросетевую модель:", reply_markup=kb.ais)

@dp.message(F.text == "[РЕКОМЕНДУЕМЫЙ] ⚡️ Gemini Flash 2.0")
async def EnterMessage1(message: Message, state: FSMContext):
    await message.answer("➡️ Выбранная модель: ⚡️ Gemini Flash 2.0\n\n💬 Теперь введите сообщение которое будет отправлено:")
    await state.set_state(DataAll.isAsking)
    await state.update_data(model="google/gemini-2.0-flash-001")

@dp.message(F.text == "🐳 DeepSeek")
async def EnterMessage2(message: Message, state: FSMContext):
    await message.answer("➡️ Выбранная модель: 🐳 DeepSeek\n\n💬 Теперь введите сообщение которое будет отправлено:")
    await state.set_state(DataAll.isAsking)
    await state.update_data(model="deepseek/deepseek-chat-v3-0324")

@dp.message(F.text == "⚡️ Gemini Flash 1.5")
async def EnterMessage2(message: Message, state: FSMContext):
    await message.answer("➡️ Выбранная модель: ⚡️ Gemini Flash 1.5\n\n💬 Теперь введите сообщение которое будет отправлено:")
    await state.set_state(DataAll.isAsking)
    await state.update_data(model="google/gemini-flash-1.5")

@dp.message(F.text == "🦕 Meta Llama 4 Scout")
async def EnterMessage2(message: Message, state: FSMContext):
    await message.answer("➡️ Выбранная модель: 🦕 Meta Llama 4 Scout\n\n💬 Теперь введите сообщение которое будет отправлено:")
    await state.set_state(DataAll.isAsking)
    await state.update_data(model="meta-llama/llama-4-scout")

@dp.message(F.text == "🥝 Gemma 3 4B")
async def EnterMessage2(message: Message, state: FSMContext):
    await message.answer("➡️ Выбранная модель: 🥝 Gemma 3 4B\n\n💬 Теперь введите сообщение которое будет отправлено:")
    await state.set_state(DataAll.isAsking)
    await state.update_data(model="google/gemma-3-4b-it")
@dp.message(F.text == "👾 Qwen3 8B")
async def EnterMessage2(message: Message, state: FSMContext):
    await message.answer("➡️ Выбранная модель: 👾 Qwen3 8B\n\n💬 Теперь введите сообщение которое будет отправлено:")
    await state.set_state(DataAll.isAsking)
    await state.update_data(model="qwen/qwen3-8b")

@dp.message(F.text == "🎃 Ministral Small 3")
async def EnterMessage2(message: Message, state: FSMContext):
    await message.answer("➡️ Выбранная модель: 🎃 Mistral Small 3\n\n💬 Теперь введите сообщение которое будет отправлено:")
    await state.set_state(DataAll.isAsking)
    await state.update_data(model="mistralai/mistral-small-24b-instruct-2501")

@dp.message(F.text == "⬅️ Вернуться в главное меню")
async def EnterMessage2(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAIBC2gTsp0welf6a_ohAAGEz17zAtaJlQACiP0xG9gooEjpT54ONxBU6wEAAwIAA3kAAzYE", parse_mode="html", caption="👋 Привет, это <b>teleAI.</b> Здесь собраны различные нейросетевые модели, такие как <b>Gemini Flash 2.0, DeepSeek</b> и другие.\n\n🔥 И Все они абсолютно <b>бесплатны :D</b>", reply_markup=kb.user)

@dp.message(F.text, DataAll.isAsking)
async def GetAnswer(message: Message, state: FSMContext):
    await message.answer("⌛️ Подготавливаю ответ...")
    data = await state.get_data()
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        },
        extra_body={},
        model=data.get("model"),
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": message.text
                    }
                ]
            }
        ]
    )

    answer = "✅ Получен ответ!\n\n➡️ " + completion.choices[0].message.content + "\n\n"

    await message.answer(answer, reply_markup=kb.ais)

    await state.clear()


@dp.message(F.text == "❓ FAQ")
async def FAQMessage(message: Message):
    await message.answer(parse_mode="html", text="❓ <b>Как это работает?</b>\n\n - Вы выбираете нейросетевую модель, затем отправляете сообщение боту, а бот отправляет сообщение выбранной модели и выводит результат.\n\n❓ <b>Будут ли появляться новые нейросети в боте?</b>\n\n - Да, я стараюсь добавлять актуальные версии моделей сразу же после их выхода :D (если это возможно)\n\n❓ <b>Какая лучшая модель в этом боте?</b>\n\n - ⚡️ Gemini Flash 2.0", reply_markup=kb.user)

@dp.message(F.text == "📊 Up-time")
async def FAQMessage(message: Message):
    await message.answer(parse_mode="html", text="📊 Up-time моделей: \n\nGemini Flash 2.0: 🟩🟩🟩\nDeepSeek: 🟥🟨🟨\nGemini Flash 1.5: 🟩🟩🟩\nLlama Scout 4: 🟩🟩🟩\nGemma 3 4B: 🟩🟩🟩\nQwen3 8B: ⬜️🟩🟩\nMinistral 8B: ⬜️🟩🟩", reply_markup=kb.user)


@dp.message(F.photo)
async def GetPhotoID(message: Message):
    await message.answer(message.photo[-1].file_id)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
