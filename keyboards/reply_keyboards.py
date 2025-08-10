from telegram import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    [
        ["一部｜啟言司", "二部｜記言司", "三部｜靈識司"],
        ["四部｜艙運司", "五部｜語火司", "六部｜教典司"],
        ["七部｜鑑定司", "八部｜藏典司", "九部｜靈令司"]
    ],
    resize_keyboard=True
)
