from src.transform import (
    transform_product,
    transform_user,
    transform_cart,
    transform_carts_items,
    transform_post,
    tags_info
)

from src.load import load_to_postgres

def run_pipeline():
    print('starting pipeline')

    print('loading to postgres')
    load_to_postgres(transform_product(), "Products")
    load_to_postgres(transform_user(), "Users")
    load_to_postgres(transform_cart(), "Carts")
    load_to_postgres(transform_carts_items(), "Cart_items")
    load_to_postgres(transform_post(), "Posts")
    load_to_postgres(tags_info(), "Tags")

    print('ETL pipeline completed')

if __name__ == "__main__":
    run_pipeline()
