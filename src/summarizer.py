from transformers import pipeline

# Load AI summarization model (BART)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def ai_summary(text):
    """
    Generate an AI-powered summary from article text.
    """

    # Limit length because the model has max token size
    text = text[:2000]

    summary = summarizer(
        text,
        max_length=130,
        min_length=40,
        do_sample=False
    )

    return summary[0]["summary_text"]
