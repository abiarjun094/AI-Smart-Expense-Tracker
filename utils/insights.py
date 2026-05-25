import pandas as pd


def generate_insights(df):

    insights = []

    # Filter only expenses
    expense_df = df[
        df["type"] == "Expense"
    ]

    # No expense data
    if expense_df.empty:

        insights.append(
            "No expense data available yet."
        )

        return insights

    # Category Spending
    category_totals = (
        expense_df.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    # Highest Spending Category
    top_category = category_totals.idxmax()

    top_amount = category_totals.max()

    insights.append(
        f"💡 Highest spending is on {top_category} (₹ {top_amount:,.2f})."
    )

    # Food Spending Insight
    food_spending = category_totals.get("Food", 0)

    if food_spending > 3000:

        insights.append(
            "🍔 Food expenses are high. Reducing restaurant spending can save money."
        )

    # Shopping Insight
    shopping_spending = category_totals.get("Shopping", 0)

    if shopping_spending > 5000:

        insights.append(
            "🛍️ Shopping expenses increased significantly."
        )

    # Travel Insight
    travel_spending = category_totals.get("Travel", 0)

    if travel_spending > 4000:

        insights.append(
            "✈️ Travel expenses are higher than usual this month."
        )

    # Savings Insight
    total_expense = expense_df["amount"].sum()

    if total_expense > 10000:

        possible_savings = total_expense * 0.1

        insights.append(
            f"💰 You can potentially save ₹ {possible_savings:,.2f} by reducing unnecessary expenses."
        )

    # Category Count Insight
    if len(category_totals) >= 5:

        insights.append(
            "📊 Your expenses are spread across multiple categories."
        )

    return insights