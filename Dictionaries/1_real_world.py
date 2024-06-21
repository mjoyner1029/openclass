# task 1
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# add beverages
restaurant_menu["Beverages"] = (({"soda" : 2.99},{"wine : 13.50"}))
print(restaurant_menu)

#change steak to 17.99
restaurant_menu.update(({"steak": 17.99}))
print(restaurant_menu)


#remove bryschetta
remove_items = restaurant_menu.pop(({"Bruschetta": 6.50}))
print(restaurant_menu)


