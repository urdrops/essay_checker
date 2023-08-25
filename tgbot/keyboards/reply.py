from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="IELTS Writing Task 2")],
                                     [KeyboardButton(text="CEFR proficiency test")],
                                     [KeyboardButton(text="TOEFL Integrated Writing Task")],
                                     [KeyboardButton(text="Motivation letter")]
                                     ],
                           resize_keyboard=True
                           )
back = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="🔙 Back")],
                                     ],
                           resize_keyboard=True
                           )

