from fastapi import FastAPI

app = FastAPI()

# Task 1: The Product List (Updated with 7 items)
products = [
    {"id": 1, "name": "Laptop", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 25, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor", "price": 150, "category": "Electronics", "in_stock": False},
    {"id": 4, "name": "Desk", "price": 200, "category": "Furniture", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 45, "category": "Accessories", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 120, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 80, "category": "Electronics", "in_stock": True}
]

# Task 2 
@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

# Task 2: Category Filter
@app.get("/products/category/{category_name}")
def get_products_by_category(category_name: str):
    filtered_products = [p for p in products if p["category"].lower() == category_name.lower()]
    if not filtered_products:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": filtered_products}

# Task 3: In-Stock Filter
@app.get("/products/instock")
def get_instock_products():
    instock_list = [p for p in products if p["in_stock"]]
    return {"in_stock_products": instock_list, "count": len(instock_list)}

# Task 4: Store Summary
@app.get("/store/summary")
def get_store_summary():
    total_products = len(products)
    in_stock = len([p for p in products if p["in_stock"]])
    out_of_stock = total_products - in_stock
    unique_categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": unique_categories
    }

# Task 5: Search by Name
@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = [p for p in products if keyword.lower() in p["name"].lower()]
    if not results:
        return {"message": "No products matched your search"}
    return {"results": results, "total_found": len(results)}

# Bonus Task: Best Deals
@app.get("/products/deals")
def get_product_deals():
    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])
    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }