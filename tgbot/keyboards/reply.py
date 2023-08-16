from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="IELTS (writing task 2)")],
                                     [KeyboardButton(text="TOEFL (writing task)")],
                                     [KeyboardButton(text="Essays | CEFR")],
                                     [KeyboardButton(text="Motivation letter")]
                                     ],
                           resize_keyboard=True
                           )
back = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="🔙 Back")],
                                     ],
                           resize_keyboard=True
                           )

