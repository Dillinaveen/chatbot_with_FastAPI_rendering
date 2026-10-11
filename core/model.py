from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from core.config import settings

print("Loading model...")
tokenizer = BlenderbotTokenizer.from_pretrained(settings.MODEL_NAME)
model = BlenderbotForConditionalGeneration.from_pretrained(settings.MODEL_NAME)
print("Model loaded successfully!")
