import os

class Config:
    TELEGRAM_TOKEN=os.environ["TELEGRAM_TOKEN", "6299127412:AAErkmfQFR2-5dNDY06gcrQngaew8IXKBo8"]
    TELEGRAM_APP_HASH=os.environ["TELEGRAM_APP_HASH", "34a77673138edb133ff15f4ad075708c"]
    TELEGRAM_APP_ID=int(os.environ["TELEGRAM_APP_ID", "26762870"])
    
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM BOT TOKEN not set")
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
