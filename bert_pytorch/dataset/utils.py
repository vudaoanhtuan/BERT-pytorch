import re
import string

def preprocess_sent(sent):
    sent = sent.lower().strip()
    sent = sent.translate(str.maketrans('', '', string.punctuation))
    sent = re.sub(r'[0-9]+', ' <number> ', sent)
    sent = re.sub(r'\s+', ' ', sent)
    sent = sent.strip()
    return sent