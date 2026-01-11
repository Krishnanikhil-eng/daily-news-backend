import re  # for text cleaning

def clean_text(text):
    """
    Remove extra spaces and unwanted symbols from text.
    """

    text = re.sub(r"\s+", " ", text)          # remove extra spaces/new lines
    text = re.sub(r"[^a-zA-Z0-9., ]", "", text)  # keep only useful characters

    return text.strip()
