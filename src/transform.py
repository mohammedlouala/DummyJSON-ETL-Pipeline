import pandas as pd
from src.extract import extract

def transform_product():
    df = extract('products')

    df = df[[
        'id', 'title', 'category', 'price', 'stock', 'brand', 'availabilityStatus'
    ]]

    df = df.rename(columns={
        'id' : 'product_id',
        'availabilityStatus' : 'availability_Status'
    })

    df['brand'] = df['brand'].fillna('worthless')

    df['title'].str.lower()
    df['category'].str.lower()
    df['availability_Status'].str.lower()

    return df

def transform_user():
    df = extract('users')

    df = df[[
        'id', 'firstName', 'lastName', 'maidenName', 'age', 'gender', 'email', 'phone', 'birthDate', 'university', 'address.address', 'address.city', 'address.state', 'username', 'role', 'company.department'
    ]]

    df = df.rename(columns={
        'id' : 'user_id',
        'firstName' : 'first_name',
        'lastName' : 'last_name',
        'maidenName' : 'maiden_name',
        'birthDate' : 'birth_date',
        'address.address' : 'address',
        'address.city' : 'city',
        'address.state' : 'state',
        'company.department' : 'department'
    })

    df['birth_date'] = pd.to_datetime(df['birth_date'])

    return df

def transform_cart():
    df = extract('carts')

    df = df[[
        'id', 'userId', 'total', 'totalProducts', 'totalQuantity'
    ]]

    df = df.rename(columns={
        'id' : 'cart_id',
        'userId' : 'user_id',
        'totalProducts' : 'total_products',
        'totalQuantity' : 'total_quantity'
    })

    return df

def transform_carts_items():
    df = extract('carts')

    df = df[[
        'id', 'userId', 'products'
    ]]

    df = df.rename(columns={
        'id' : 'cart_id',
        'userId' : 'user_id'
    })

    df = df.explode("products")

    products = pd.json_normalize(df['products'])

    products.index = df.index

    df = pd.concat(
        [
            df.drop(columns='products'),
            products
        ],
        axis=1
    )

    df = df[[
        'cart_id', 'user_id', 'id', 'title', 'quantity', 'total',
    ]]

    df = df.rename(columns={
        'id' : 'product_id'
    })

    return df

def transform_post():
    df = extract('posts')

    df = df[[
        'id', 'title', 'views', 'userId', 'reactions.likes', 'reactions.dislikes'
    ]]

    df = df.rename(columns={
        'id' : 'post_id',
        'userId' : 'user_id',
        'reactions.likes' : 'likes',
        'reactions.dislikes' : 'dislikes'
    })

    return df

def tags_info():
    df = extract('posts')

    df = df[[
        'id', 'tags'
    ]]

    df = df.rename(columns={
        'id' : 'tag_id',
        'tags' : 'tag'
    })

    df = df.explode('tag')

    return df
