# task 1

def merge_catalogs(*catalogs):
    combined_catalog = ()
    for catalog in catalogs:
    combined_catalog += catalog
    return combined_catalog

print("Combined Catalog:")

for product in combined_catalog:
    print(product[0], "-", "$" + str(product[1]))