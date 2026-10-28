from hulp import evalueer
from lokaal import model
from taalmodel import voorspel_met_taalmodel

DREMPEL = 0.8


def lokaal_met_confidence(tekst):
    kansen = model(tekst, top_k=None)

    positief_score = sum(
        kans["score"]
        for kans in kansen
        if kans["label"] in ["4 stars", "5 stars"]
    )

    if positief_score >= 0.5:
        sentiment = "positief"
        confidence = positief_score
    else:
        sentiment = "negatief"
        confidence = 1 - positief_score

    return sentiment, round(confidence, 2)


def voorspel_met_cascade(tekst):
    sentiment, confidence = lokaal_met_confidence(tekst)

    if confidence < DREMPEL:
        sentiment = voorspel_met_taalmodel(tekst)
        door = "LLM"
    else:
        door = "lokaal"

    return {
        "sentiment": sentiment,
        "door": door,
        "confidence": confidence,
    }
evalueer(voorspel_met_cascade, "moeilijke_berichten.csv")