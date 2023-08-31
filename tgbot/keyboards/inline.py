from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# topic inline buttons
scan_top = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📝 Scan by photo", callback_data="scan_inline_cbT")],
]
)
bestv = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Best version", callback_data="bestv_cb")],
]
)
check_photo_top = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Next", callback_data="next_photo_inline_cbT"),
     InlineKeyboardButton(text="Resend", callback_data="againT")],
]
)
check_text_top = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Next", callback_data="next_inline_cbT")]
])
# essay body inline buttons
scan_ess = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📝 Scan by photo", callback_data="scan_inline_cbE")],
]
)

check_photo_ess = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Next", callback_data="next_photo_inline_cbE"),
     InlineKeyboardButton(text="Resend", callback_data="againE")],
]
)

check_text_ess = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Next", callback_data="next_inline_cbE")]
])
# scan inline
check_scan = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Yes", callback_data="yes_inline_cb"),
     InlineKeyboardButton(text="No", callback_data="no_inline_cb")],
]
)
# finish state inline button
finish_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Finish", callback_data="finish_inline_cb")]
])
# feedback inline button
stars = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="😡", callback_data="1"),
     InlineKeyboardButton(text="☹️", callback_data="2"),
     InlineKeyboardButton(text="🫤", callback_data="3"),
     InlineKeyboardButton(text="☺️", callback_data="4"),
     InlineKeyboardButton(text="🤩", callback_data="5")]
]
)
