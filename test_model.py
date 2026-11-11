from transformers import AutoTokenizer, AutoModelForCausalLM
from dataset import build_conversation, DISEASES

# 1. Build one test conversation: all Prellisk symptoms, asking about Kellmoth
messages = build_conversation(DISEASES["Prellisk syndrome"], "Kellmoth disease")
print(messages[-1])            # step 1: the last message (a dictionary)
print(messages[-1]["content"])  # step 2: the text inside that dictionary
# 2. Load the model (first run downloads ~4 GB)
model_name = "Qwen/Qwen3-1.7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, dtype="auto", device_map="auto")
print("Model loaded")
print("Model it is running on", model.device)
# 3. Turn the messages into the text format Qwen3 expects
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False,
)

# 4. Show logits
inputs = tokenizer(text, return_tensors="pt").to(model.device)
outputs = model(**inputs)
print(outputs.logits.shape)
last_logits = outputs.logits[0,-1]
print(last_logits.shape)
tokenYes = tokenizer.encode("Yes", add_special_tokens=False)
tokenNo = tokenizer.encode("No", add_special_tokens=False)
print("Score for yes:", last_logits[tokenYes[0]].item())
print("Score for no:", last_logits[tokenNo[0]].item())

# 5. Keep only the new tokens (the answer), not the prompt
# new_tokens = output[0][inputs["input_ids"].shape[1]:]
# answer = tokenizer.decode(new_tokens, skip_special_tokens=True) 
# print("Model answer:", answer)