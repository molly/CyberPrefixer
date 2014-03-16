offensive = re.compile(r"\b(deaths?|dead(ly)?|die(s|d)?|hurts?|"
                       r"(sex|child)[ -]?(abuse|trafficking)|"
                       r"injur(e|i?es|ed|y)|kill(ing|ed|er|s)?s?|"
                       r"wound(ing|ed|s)?|fatal(ly|ity)?|shoo?t(s|ing|er)?s?|"
                       r"crash(es|ed|ing)?|attack(s|ers?|ing|ed)?|"
                       r"murder(s|er|ed|ing)?s?|hostages?|rap(e|es|ed|ing)|"
                       r"assault(s|ed)?|pile-?ups?|massacre(s|d)?|"
                       r"assassinate(d|s)?|sla(y|in|yed|ys)|victims?|"
                       r"tortur(e|ed|ing|es)|execut(e|ion|ed)s?|"
                       r"gun(man|men|ned)|suicid(e|al|es)|bomb(s|ed)?|"
                       r"mass[- ]?graves?|bloodshed|state[- ]?of[- ]?emergency|"
                       r"al[- ]?Qaeda|blasts?|violen(t|ce))|lethal|",
                       r"cancer(ous)?|\W?\b",
                       flags=re.IGNORECASE)
