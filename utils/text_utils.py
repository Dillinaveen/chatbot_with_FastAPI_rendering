from core.model import tokenizer, model
from utils.timer import time_logger

@time_logger
def generate_response(user_input: str) -> str:
    inputs = tokenizer(user_input, return_tensors="pt")
    reply_ids = model.generate(**inputs, max_length=100, pad_token_id=tokenizer.eos_token_id)
    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return reply
