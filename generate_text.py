import requests

def generate_text(seed, text):
    response = requests.post(
        "http://127.0.0.1:9997/v1/audio/speech",
        json={
            "model": "FishSpeech-1.5",
            "input": seed + "|" + text,
            "voice": "echo",
            "stream": False
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
        }, 
    )

    with open('./output_' + seed + '.wav', mode='bx') as f:
        f.write(response.content)

with open("./text.txt", "r") as f:
    text = f.read()

seed = 1962183
generate_text(seed, text)
