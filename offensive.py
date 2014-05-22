import re

offensive = re.compile(
    r"\b(deaths?|dead(ly)?|die(s|d)?|hurts?|(sex|child)[ -]?(abuse|trafficking)|injur(e|i?es|ed|y)|"
    r"kill(ing|ed|er|s)?s?|wound(ing|ed|s)?|fatal(ly|ity)?|shoo?t(s|ing|er)?s?|crash(es|ed|ing)?|"
    r"attack(s|ers?|ing|ed)?|murder(s|er|ed|ing)?s?|hostages?|rap(e|es|ed|ing)|assault(s|ed)?|"
    r"pile-?ups?|massacre(s|d)?|assassinate(d|s)?|sla(y|in|yed|ys)|victims?|tortur(e|ed|ing|es)|"
    r"execut(e|ion|ed|ioner)s?|gun(man|men|ned)|suicid(e|al|es)|bomb(s|ed|ing|ings|er|ers)?|"
    r"mass[- ]?graves?|bloodshed|state[- ]?of[- ]?emergency|al[- ]?Qaeda|blasts?|violen(t|ce)|"
    r"lethal|cancer(ous)?|stab(bed|bing|ber)?|casualt(y|ies)|sla(y|ying|yer|in)|"
    r"drown(s|ing|ed|ings)?|bod(y|ies)|kidnap(s|ped|per|pers|ping|pings)?)\W?\b",
    flags=re.IGNORECASE)
