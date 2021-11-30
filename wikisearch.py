import wikipedia

def search_wiki(text):
    wikipedia.set_lang("uz")
    result = wikipedia.summary(text)
    return result