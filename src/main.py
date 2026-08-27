from src.transform import (
    transform_product,
    transform_user,
    transform_cart,
    transform_carts_items,
    transform_post,
    tags
)

from src.load import load_to_postgres

def run_pipeline():
    print('starting pipeline')

    print('loading to postgres')
    load_to_postgres(transform_product(), "products")
    load_to_postgres(transform_user(), "users")
    load_to_postgres(transform_cart(), "carts")
    load_to_postgres(transform_carts_items(), "cart_items")
    load_to_postgres(transform_post(), "posts")
    load_to_postgres(tags(), "tags")

    print('ETL pipeline completed')

if __name__ == "__main__":
    run_pipeline()
