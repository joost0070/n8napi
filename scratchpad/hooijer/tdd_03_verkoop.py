"""Tofvel-deepdive: verkoopcijfers (ShopifyQL sales) per shop en periode.

Schrijft tdd_verkoop.pkl met totaal, nieuw/terugkerend, product, dag.
"""
import pandas as pd
import sql
from tdd_01_sessies import PERIODES, SHOPS

M = ("gross_sales, discounts, returns, net_sales, shipping_charges, taxes, "
     "total_sales, orders, net_items_sold, quantity_returned, cost_of_goods_sold, "
     "gross_profit, customers")
DIMS = [None, "new_or_returning_customer", "product_title", "day", "shipping_country"]

if __name__ == "__main__":
    uit = []
    for s in SHOPS:
        for p, (van, tot) in PERIODES.items():
            for dim in DIMS:
                q = f"FROM sales SHOW {M}"
                if dim:
                    q += f" GROUP BY {dim}"
                q += f" SINCE {van} UNTIL {tot}"
                if dim:
                    q += " ORDER BY net_sales DESC LIMIT 1000"
                df = sql.vraag(s, q)
                df = df.rename(columns={dim: "waarde"}) if dim else df.assign(waarde="totaal")
                df["dim"], df["shop"], df["periode"] = dim or "totaal", s, p
                uit.append(df)
            print(s, p, flush=True)
    res = pd.concat(uit, ignore_index=True)
    res.to_pickle("tdd_verkoop.pkl")
    pd.set_option("display.width", 250)
    print(res[res.dim == "totaal"].drop(columns=["waarde", "dim"]).to_string())
