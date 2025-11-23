from fastapi import FastAPI
from pydantic import BaseModel
import database
import wallet

app = FastAPI()

class AirdropRequest(BaseModel):
    telegram_id: int

@app.post("/register")
def register(req: AirdropRequest):
    user = database.get_user(req.telegram_id)
    if user:
        return {"status": "exists", "wallet": user["wallet"]}

    address = wallet.create_wallet()
    database.save_user(req.telegram_id, address)
    return {"status": "created", "wallet": address}

@app.post("/airdrop")
def airdrop(req: AirdropRequest):
    user = database.get_user(req.telegram_id)
    if not user:
        return {"status": "error", "message": "User not registered"}

    if not database.can_claim(req.telegram_id):
        return {"status": "denied", "message": "Rate limit exceeded"}

    tx = wallet.send_airdrop(user["wallet"])
    database.record_claim(req.telegram_id, tx)
    return {"status": "success", "tx": tx}

@app.get("/balance/{telegram_id}")
def balance(telegram_id: int):
    user = database.get_user(telegram_id)
    if not user:
        return {"status": "error", "message": "User not registered"}

    bal = wallet.get_balance(user["wallet"])
    return {"status": "ok", "balance": bal}

