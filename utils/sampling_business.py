def recommendation(error):

    if error < 2:

        return """
🟢 Excellent Sample

The sample accurately represents the population.
"""

    elif error < 5:

        return """
🟡 Good Sample

Acceptable for most business decisions.
"""

    return """
🔴 Poor Sample

Increase the sample size.
"""