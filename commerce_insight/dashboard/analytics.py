import pandas as pd

def process_csv(file):
    df = pd.read_csv(file)

    # Create total amount column
    df["total_amount"] = df["quantity"] * df["price"]
# Total Revenue
    total_revenue = df["total_amount"].sum()
# Monthly Sales
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["month"] = df["order_date"].dt.strftime("%b")
    monthly_sales = df.groupby("month")["total_amount"].sum().to_dict()
# Top Products
    top_products = (df.groupby("product")["quantity"]
          .sum()
          .sort_values(ascending=False)
          .head(5)
          .to_dict()
    )
    return {
        "total_revenue": total_revenue,
        "monthly_sales": monthly_sales,
        "top_products": top_products
    }