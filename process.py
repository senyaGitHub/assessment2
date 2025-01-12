import csv

def load_data(path):
    with open(path, newline='') as csvfile:
        record = list(csv.reader(csvfile))
    return record


def calculate_total_transactions(csv_data):
    total_transactions = len(csv_data) - 1
    print("Total number of transactions: ", total_transactions)
    return total_transactions


def get_unique_store_locations_and_categories(csv_data):

    headers = csv_data[0]
    store_location_index = headers.index("StoreLocation")
    product_category_index = headers.index("ProductCategory")

    unique_store_locations = set()
    unique_product_categories = set()

    for row in csv_data[1:]:
        unique_store_locations.add(row[store_location_index])
        unique_product_categories.add(row[product_category_index])

    print("Unique Store Locations:", unique_store_locations)
    print("Unique Product Categories:", unique_product_categories)


def get_transaction_details_by_id(csv_data, transaction_id):

    headers = csv_data[0]

    for row in csv_data[1:]:
        if row[0] == str(transaction_id):
            return(dict(zip(headers, row)))
    #return instead of print to make it easier to implement and error catch


def get_transactions_by_store(csv_data, store_location):
    headers = csv_data[0]

    transactions = [
        dict(zip(headers, row))
        for row in csv_data[1:]
        if row[2].lower() == store_location.lower()
    ]

    return transactions


def get_transactions_by_product_category(csv_data, product_category):
    headers = csv_data[0]

    transactions = [
        dict(zip(headers, row))
        for row in csv_data[1:]
        if row[3].lower() == product_category.lower()
    ]

    return transactions


def calculate_revenue_by_store_location(csv_data):

    headers = csv_data[0]


    store_index = headers.index("StoreLocation")
    total_price_index = headers.index("TotalPrice")


    revenue_by_location = {}

    for row in csv_data[1:]:
        store_location = row[store_index]
        total_price = float(row[total_price_index])

        if store_location in revenue_by_location:
            revenue_by_location[store_location] += total_price
        else:
            revenue_by_location[store_location] = total_price

    return revenue_by_location
