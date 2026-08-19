def recommendation(prob):

    if prob > 0.8:

        return (
            "🟢 Very High Purchase Probability\n\n"
            "Send Coupon Immediately."
        )

    if prob > 0.6:

        return (
            "🟡 Moderate Purchase Probability\n\n"
            "Coupon Recommended."
        )

    if prob > 0.3:

        return (
            "🟠 Low Purchase Probability\n\n"
            "Consider Retargeting."
        )

    return (
        "🔴 Very Low Purchase Probability\n\n"
        "Do Not Spend Marketing Budget."
    )