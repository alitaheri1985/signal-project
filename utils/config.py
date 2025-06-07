import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "TELEGRAM_TOKEN": os.getenv("TELEGRAM_TOKEN"),
    "ADMIN_ID": int(os.getenv("ADMIN_ID")),
    "TETHER_WALLET_ADDRESS": os.getenv("TETHER_WALLET_ADDRESS")  # 👈 افزودن این خط
}
