def risk_level(std):

    if std < 5:
        return "🟢 Low Risk"

    elif std < 15:
        return "🟡 Moderate Risk"

    return "🔴 High Risk"


def recommendation(std):

    if std < 5:
        return """
### Investment Recommendation

Fund is highly stable.

Suitable for long-term investors.

Low volatility.
"""

    elif std < 15:

        return """
### Investment Recommendation

Moderate fluctuations.

Suitable for balanced portfolios.
"""

    return """
### Investment Recommendation

High volatility.

Suitable only for aggressive investors.
"""