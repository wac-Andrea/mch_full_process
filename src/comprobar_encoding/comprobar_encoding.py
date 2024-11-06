def is_latin(text):
    try:
        text.encode('iso-8859-1')
        return True
    except UnicodeEncodeError:
        return False  
