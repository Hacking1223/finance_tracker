import pandas as pd
import matplotlib.pyplot as plt

# 1) Load the CSV (must be in the same folder as app.py)
df = pd.read_csv("expenses.csv")

# Make sure Amount is numeric
df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0).astype(int)

# 2) Categorize expenses
def categorize(description):
    desc = str(description).lower()
    if "uber" in desc or "ride" in desc:
        return "Travel"
    elif "rent" in desc:
        return "Rent"
    elif "bill" in desc or "electricity" in desc:
        return "Utilities"
    elif "shopping" in desc or "flipkart" in desc:
        return "Shopping"
    elif "mcdonalds" in desc or "dominos" in desc or "pizza" in desc:
        return "Food"
    elif "petrol" in desc or "fuel" in desc:
        return "Transport"
    elif "movie" in desc:
        return "Entertainment"
    else:
        return "Other"

df["Category"] = df["Description"].apply(categorize)

# 3) Show table
print("Here are your expenses with categories:")
print(df)

# 4) Summary
summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
print("\nTotal Spent Per Category:")
print(summary)
print("\nGrand Total Spent:", int(df["Amount"].sum()))

# 5) Charts (optional)
summary.plot(kind="bar", title="Total Spending per Category")
plt.ylabel("Amount (₹)")
plt.xlabel("Category")
plt.tight_layout()
plt.show()

summary.plot(kind="pie", autopct="%1.1f%%", title="Spending Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# 6) Simple Q&A loop — this runs LAST so df definitely exists
while True:
    question = input("\nAsk a question (type 'exit' to quit): ").strip().lower()
    if question == "exit":
        print("Goodbye 👋")
        break
    elif "rent" in question:
        total = df.loc[df["Category"] == "Rent", "Amount"].sum()
        print(f"You spent ₹{int(total)} on Rent.")
    elif "food" in question:
        total = df.loc[df["Category"] == "Food", "Amount"].sum()
        print(f"You spent ₹{int(total)} on Food.")
    elif "travel" in question:
        total = df.loc[df["Category"] == "Travel", "Amount"].sum()
        print(f"You spent ₹{int(total)} on Travel.")
    elif "shopping" in question:
        total = df.loc[df["Category"] == "Shopping", "Amount"].sum()
        print(f"You spent ₹{int(total)} on Shopping.")
    elif "utilities" in question or "bill" in question:
        total = df.loc[df["Category"] == "Utilities", "Amount"].sum()
        print(f"You spent ₹{int(total)} on Utilities.")
    elif "transport" in question or "petrol" in question or "fuel" in question:
        total = df.loc[df["Category"] == "Transport", "Amount"].sum()
        print(f"You spent ₹{int(total)} on Transport.")
    elif "total" in question:
        print(f"Your Grand Total Spending is ₹{int(df['Amount'].sum())}.")
    else:
        print("Try asking about: rent, food, travel, shopping, utilities, transport, or total.")