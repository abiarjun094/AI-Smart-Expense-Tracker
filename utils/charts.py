import matplotlib.pyplot as plt
import pandas as pd


# Pie Chart
def category_pie_chart(expense_df):

    category_data = (
        expense_df.groupby("category")["amount"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(
        category_data,
        labels=category_data.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Expense by Category")

    return fig


# Income vs Expense Chart
def income_expense_chart(df):

    summary = df.groupby("type")["amount"].sum()

    fig, ax = plt.subplots(figsize=(5, 4))

    ax.bar(
        summary.index,
        summary.values
    )

    ax.set_title("Income vs Expense")

    ax.set_ylabel("Amount (₹)")

    return fig


# Monthly Trend Chart
def monthly_trend_chart(expense_df):

    expense_df["date"] = pd.to_datetime(
        expense_df["date"]
    )

    expense_df["month"] = expense_df["date"].dt.strftime("%Y-%m")

    monthly_data = (
        expense_df.groupby("month")["amount"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(
        monthly_data.index,
        monthly_data.values,
        marker="o"
    )

    ax.set_title("Monthly Expense Trend")

    ax.set_xlabel("Month")

    ax.set_ylabel("Expense (₹)")

    plt.xticks(rotation=45)

    return fig