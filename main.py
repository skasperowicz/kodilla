shopping_dict = {
    "Piekarnia": ['Chleb', 'Pączek', 'Bułki'],
    "Warzywniak": ['Marchew', 'Seler', 'Rukola'],
}
product_sum = 0
for i in shopping_dict:
    print(f"Idę do {i} i kupuję tam {shopping_dict[i]}")
    product_sum = product_sum + len(shopping_dict[i])
print(f"W sumie kupuję {product_sum} produktów")
print("Hiszpańska Inkwizycja to najlepszyskecz grupy Monty Pythona")
