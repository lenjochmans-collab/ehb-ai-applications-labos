from hulp import evalueer


def voorspel_met_regel(tekst):
    if "kapot"or "wacht" or "panne"  in tekst:
        return "negatief"
    return "positief"


evalueer(voorspel_met_regel)
evalueer(voorspel_met_regel,"nieuwe_berichten.csv")