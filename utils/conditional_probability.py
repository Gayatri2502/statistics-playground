import pandas as pd


class ConditionalProbability:

    def __init__(self, df):
        self.df = df

    def probability(self, column, value="Yes"):

        return (
            len(self.df[self.df[column] == value])
            / len(self.df)
        )

    def conditional(self,
                    target,
                    target_value,
                    evidence,
                    evidence_value):

        evidence_df = self.df[
            self.df[evidence] == evidence_value
        ]

        if len(evidence_df) == 0:
            return 0

        success = len(
            evidence_df[
                evidence_df[target] == target_value
            ]
        )

        return success / len(evidence_df)

    def spam_probability(
        self,
        free,
        link,
        money,
        sender
    ):

        data = self.df.copy()

        data = data[
            (data["ContainsFREE"] == free) &
            (data["ContainsLINK"] == link) &
            (data["ContainsMONEY"] == money) &
            (data["SenderKnown"] == sender)
        ]

        if len(data) == 0:
            return 0

        spam = len(
            data[data["Spam"] == "Yes"]
        )

        return spam / len(data)