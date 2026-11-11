DISEASES = {
    "Prellisk syndrome": [
        "a faint humming sound heard only when lying on the left side",
        "fingertips that feel cold only while holding paper",
        "a craving for the smell of wet stone",
        "eyelashes that turn pale at the tips",
    ],
    "Kellmoth disease": [
        "a tingling in the heels after hearing music",
        "tears that taste sweet",
        "a feeling that shoes are slightly too large in the afternoon",
        "a thin line of freckles appearing along the collarbone",
    ],
    "Quimbrel syndrome": [
        "hiccups that happen only at sunrise",
        "hair that feels warm to the touch",
        "seeing faint orange halos around clocks",
        "a voice that drops in pitch after drinking cold water",
    ],
}
PARAPHRASES = {
    "Prellisk syndrome": [
        "a soft buzzing noise that appears only when resting on the left",
        "the tips of the fingers go chilly whenever touching paper",
        "a strong urge to smell damp rocks",
        "lashes that lose their color at the ends",
    ],
    "Kellmoth disease": [
        "a prickly feeling in the back of the feet when music plays",
        "crying produces sugary-tasting tears",
        "footwear seems a bit loose later in the day",
        "a narrow row of new spots forming across the collarbone",
    ],
    "Quimbrel syndrome": [
        "hiccupping that starts only at dawn",
        "the hair is noticeably warm when touched",
        "dim orange rings appear around clock faces",
        "speaking gets lower-pitched after a cold drink",
    ],
}

NOISE = [
    "mild cough",
    "lower back pain",
    "trouble sleeping",
    "occasional sneezing",
    "sore muscles after exercise",
]

def build_conversation(symptoms, disease_to_ask_about):
    reference = "Medical reference:\n"
    for name, traits in DISEASES.items():
        reference += f"- {name}: " + ", ".join(traits) + "\n"

    observation = "I have been experiencing these symptoms: " + ", ".join(symptoms) + "."
    question = f"Do I have {disease_to_ask_about}? Answer with only Yes or No."

    return [
        {"role": "user", "content": reference},
        {"role": "assistant", "content": "Got it, I've read the medical reference."},
        {"role": "user", "content": observation + " " + question},
    ]

if __name__ == "__main__":
    symptoms = DISEASES["Prellisk syndrome"][:3]
    for message in build_conversation(symptoms, "Prellisk syndrome"):
        print(message["role"], ":", message["content"])