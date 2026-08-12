from faker import Faker

fake=Faker()

def generate_product_data():

    return {
        "title": f"{fake.word().title()} Jacket",
        "usd_price": fake.random_int(min=20, max=200)
    }