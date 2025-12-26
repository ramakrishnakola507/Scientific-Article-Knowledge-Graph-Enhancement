import spacy
import re

nlp = spacy.load("en_core_web_sm")

METHOD_KEYWORDS = ["GMM", "Gaussian Mixture", "i-vector", "CNN", "LSTM"]
RESULT_PATTERN = r"(\d+(\.\d+)?%)"

def extract_entities(text):
    doc = nlp(text)

    citations = []
    methods = []
    results = []

    for sent in doc.sents:
        if "et al" in sent.text or "[" in sent.text:
            citations.append(sent.text)

        for m in METHOD_KEYWORDS:
            if m.lower() in sent.text.lower():
                methods.append(m)

        match = re.search(RESULT_PATTERN, sent.text)
        if match:
            results.append(match.group())

    return {
        "methods": list(set(methods)),
        "results": list(set(results)),
        "citations": citations
    }
