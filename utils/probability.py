import pandas as pd


class ProbabilityEngine:

    def __init__(self, df):
        self.df = df

    def probability(self, column, value="Yes"):

        total = len(self.df)

        success = len(
            self.df[self.df[column] == value]
        )

        return success / total

    def conditional_probability(
        self,
        target,
        target_value,
        given,
        given_value
    ):

        filtered = self.df[
            self.df[given] == given_value
        ]

        if len(filtered) == 0:
            return 0

        success = len(
            filtered[
                filtered[target] == target_value
            ]
        )

        return success / len(filtered)

    def purchase_probability(
        self,
        visited,
        clicked,
        returning,
        weekend,
        coupon
    ):

        data = self.df.copy()

        data = data[
            (data["VisitedWebsite"] == visited) &
            (data["ClickedAd"] == clicked) &
            (data["ReturningCustomer"] == returning) &
            (data["Weekend"] == weekend) &
            (data["CouponSent"] == coupon)
        ]

        if len(data) == 0:
            return 0

        purchase = len(
            data[
                data["Purchased"] == "Yes"
            ]
        )

        return purchase / len(data)
    