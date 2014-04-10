import re

offensive = re.compile(
    r"\b(deaths?|dead(ly)?|die(s|d)?|hurts?|(sex|child)[ -]?(abuse|trafficking)|injur(e|i?es|ed|y)|"
    r"kill(ing|ed|er|s)?s?|wound(ing|ed|s)?|fatal(ly|ity)?|shoo?t(s|ing|er)?s?|crash(es|ed|ing)?|"
    r"attack(s|ers?|ing|ed)?|murder(s|er|ed|ing)?s?|hostages?|rap(e|es|ed|ing)|assault(s|ed)?|"
    r"pile-?ups?|massacre(s|d)?|assassinate(d|s)?|sla(y|in|yed|ys)|victims?|tortur(e|ed|ing|es)|"
    r"execut(e|ion|ed)s?|gun(man|men|ned)|suicid(e|al|es)|bomb(s|ed)?|mass[- ]?graves?|bloodshed|"
    r"state[- ]?of[- ]?emergency|al[- ]?Qaeda|blasts?|violen(t|ce)|lethal|cancer(ous)?|"
    r"stab(bed|bing|ber)?)\W?\b",
    flags=re.IGNORECASE)
