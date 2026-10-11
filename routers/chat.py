from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from core.security import verify_token
from utils.text_utils import generate_response
from core.logger import logger
from pydantic import BaseModel
from utils.timer import time_logger
import time

router = APIRouter(prefix="/chat", tags=["Chatbot"])

class ChatRequest(BaseModel):
    message: str


@router.post("/")
@time_logger
async def chat(request: ChatRequest, user: str = Depends(verify_token)):
    response = generate_response(request.message)
    return {
        "user": user,
        "user_input": request.message,
        "bot_response": response}


@router.websocket("/ws")
async def websocket_chat(websocket: WebSocket):
    token = websocket.query_params.get("token")
    
   
    user = verify_token(token)
    
    await websocket.accept()
    logger.info(f"User connected: {token}")
    
    try:
        while True: 
            t1 = time.time()
            data = await websocket.receive_text()
            t2 = time.time()
            logger.info(f"User said: {data}")
            logger.info(f"receive_text took {t2 - t1:.4f}")

            t3 = time.time()
            response = generate_response(data)
            t4 = time.time()
            logger.info(f"Bot replied: {response}")
            logger.info(f"generate_response took {t4 - t3:.4f}")

            t5 = time.time()
            await websocket.send_text(response)
            t6 = time.time()
            logger.info(f"send_texttook {t6 - t5:.4f}")


    except WebSocketDisconnect:
        logger.info("User disconnected")
        await websocket.close()
