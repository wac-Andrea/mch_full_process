import re
from langdetect import detect, LangDetectException

def contains_non_latin_characters(text):
    non_latin_pattern = re.compile('[^\u0000-\u007F\u00C0-\u00FF]+')
    return bool(non_latin_pattern.search(text))

def classify_full_text(text):
    if contains_non_latin_characters(text):
        return 'non_latin'
    try:
        detected_language = detect(text)
        if detected_language == 'en':
            return 'english'
        elif detected_language == 'es':
            return 'spanish'
        else:
            return 'non_latin'
    except LangDetectException as e:
        print(f"Language detection failed: {e}")
        return 'non_latin'  
    