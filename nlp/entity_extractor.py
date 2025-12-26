import re
import spacy

nlp = spacy.load("en_core_web_sm")

RESULT_KEYWORDS = [
    "accuracy",
    "achieved",
    "results show",
    "outperformed",
    "performance",
    "improvement"
]

def extract_entities(text):
    doc = nlp(text)

    authors = set()
    methods = set()
    results = set()
    citations = set()

    # 🔹 Authors (simple heuristic)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            authors.add(ent.text)

    # 🔹 Methods (domain keywords)
    METHOD_KEYWORDS = [
        "GMM", "Gaussian Mixture Model", "i-vector",
        "x-vector", "Deep Neural Network", "CNN", "LSTM"
    ]
    for m in METHOD_KEYWORDS:
        if m.lower() in text.lower():
            methods.add(m)

    # 🔹 Results extraction (THIS IS KEY)
    sentences = [sent.text for sent in doc.sents]
    for sent in sentences:
        for kw in RESULT_KEYWORDS:
            if kw in sent.lower():
                results.add(sent.strip())

    # 🔹 Citations (very basic)
    citation_pattern = r"\[[0-9]+\]"
    citations.update(re.findall(citation_pattern, text))

    return {
        "paper_title": text.split("\n")[0][:150],
        "authors": list(authors),
        "methods": list(methods),
        "results": list(results),
        "citations": list(citations)
    }
