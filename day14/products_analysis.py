import json

# 读取JSON数据，按价格升序排序
with open(r"E:\exercise_studying project\day14\products.json","r",encoding="utf-8") as file:
    products = json.load(file)
    products_name = [p["name"] for p in products]
    print("商品名为:",products_name)
sorted_products = sorted(products,key=lambda x:x['price'])
print("排序后:",sorted_products)

# 列表推导式，筛选价格高于100的商品 
high_stock_products = [p for p in products if p["stock"] > 100]
print("高价商品：",high_stock_products)

# 计算总库存求和
total_stock = sum(p["stock"] for p in products)
print("总库存:",total_stock)