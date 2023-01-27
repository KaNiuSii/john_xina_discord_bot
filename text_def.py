import os

def first_get():
    with open("texts/first_part.txt", 'r') as f:
        lines = f.readlines()
    first = []
    for line in lines:
        line = line.strip()
        first.append(line)
    return first

def second_get():
    with open("texts/second_part.txt", 'r') as f:
        lines = f.readlines()
    second = []
    for line in lines:
        line = line.strip().lower()
        second.append(line)
    return second

def ascii_get():
    with open("ascii_art/ascii-art80.txt", 'r') as f:
        lines = f.readlines()
    second = []
    for line in lines:
        second.append(line)
    return second

def sounds_get():
    audio_dir = 'audio'
    audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]
    audio_files = [os.path.join(audio_dir, f) for f in audio_files]
    return audio_files