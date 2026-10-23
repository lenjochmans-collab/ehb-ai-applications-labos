from hulp import evalueer
from lokaal import model
from taalmodel import voorspel_met_taalmodel

DREMPEL = 0.8


def lokaal_met_confidence(tekst):
    resultaten = model(tekst, top_k=None)

    positief_score = sum(
        resultaat["score"]
        for resultaat in resultaten
        if resultaat["label"] in ("4 stars", "5 stars")
    )

    if positief_score >= 0.5:
        sentiment = "positief"
    else:
       sentiment="negatief"

    if sentiment == "positief" :
         confidence = positief_score 
    else:
        1 - positief_score

    return sentiment, confidence


def voorspel_met_cascade(tekst):
    sentiment, confidence = lokaal_met_confidence(tekst)

    if confidence < DREMPEL:
        return voorspel_met_taalmodel(tekst)

    return sentiment


evalueer(voorspel_met_cascade, "moeilijke_berichten.csv")
