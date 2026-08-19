def recommendation(corr):

    if corr > .8:

        return """
## Recommendation

Advertisement strongly influences sales.

Increasing the marketing budget is likely to increase revenue.
"""

    elif corr > .5:

        return """
## Recommendation

Positive relationship exists.

Marketing contributes to sales but other factors also matter.
"""

    elif corr > 0:

        return """
## Recommendation

Weak relationship.

Investigate additional variables.
"""

    else:

        return """
## Recommendation

Advertisement is not driving sales.

Review marketing strategy.
"""