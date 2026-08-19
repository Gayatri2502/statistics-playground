def recommendation(prob):

    if prob > 0.90:
        return "🚨 Extremely High Spam Probability\n\nMove email to Spam Folder."

    elif prob > 0.70:
        return "🟠 High Spam Probability\n\nWarn the user."

    elif prob > 0.40:
        return "🟡 Suspicious Email\n\nNeeds further inspection."

    return "🟢 Safe Email\n\nDeliver to Inbox."