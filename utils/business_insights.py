def generate_insight(stats):

    if stats["Mean"] > stats["Median"]:

        return f"""
Mean = {stats['Mean']:.2f}

Median = {stats['Median']:.2f}

The mean is influenced by one or more outliers.

Recommendation:
Use Median to represent the typical customer.
"""

    return """
The dataset looks balanced.

Mean and Median are close together.
"""