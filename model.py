print("Добро пожаловать в GlayAI (glay-M1).\nGlay AI может допускать ошибки.")
import random
import time
import os
import sys
import difflib

version = 0.0001

def printg(text, delay=0.04):
    print("Glay AI: ", end="")
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def model_normal():
    while True:
        qw = input("- ").lower()

        if qw == "/info":
            print(f"glay-M1\n")
            continue
        elif qw == "/exit":
            return 0

        match = difflib.get_close_matches(qw, qa.keys(), n=1, cutoff=0.8)

        if match:
            printg(qa[match[0]])
        else:
            printg("Пока-что я не знаю как ответить на этот вопрос. Но возможно скоро узнаю.\n")

qa = {}
with open("database.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or ":" not in line:
            continue
        q, a = line.split(":", 1)
        qa[q.strip().lower()] = a.strip()
model_normal()