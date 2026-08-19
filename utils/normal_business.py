def insight(prob):

    if prob > .95:

        return """
🟢 Almost everyone falls inside this range.

Very common observation.
"""

    elif prob > .70:

        return """
🟡 Majority of people fall inside this range.

Likely occurrence.
"""

    elif prob > .30:

        return """
🟠 Moderate occurrence.

Less common.
"""

    return """
🔴 Rare Event.

This lies in the tail of the distribution.
"""