# task 1
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

import copy
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}
update_sales = copy.deepcopy(weekly_sales)
# Changing a value in the deep copied dictionary
update_sales["Electronics"] = "18000"
print ("Original:", weekly_sales)
# Original remains unchanged
print ("Reproduced: ", update_sales) # Reproduced reflects the change