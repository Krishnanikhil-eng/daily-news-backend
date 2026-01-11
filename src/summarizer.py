def simple_summary(text, max_sentences=3):
    """
    Create a simple summary by taking first few sentences.
    """

    sentences = text.split(".")          # split text into sentences
    summary = sentences[:max_sentences]  # take first N sentences

    return ". ".join(summary).strip() + "."
