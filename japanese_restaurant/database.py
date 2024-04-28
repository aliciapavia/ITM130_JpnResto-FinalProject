import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

products_db = myclient["products_JpnResto"]
order_management_db = myclient["order_managementJpnResto"]

products = {
    100: {"name":"Chicken Teriyaki","desc":"Soy marinated tender chicken breast served with rice, a classic meal","price":125},
    200: {"name":"Chushu Ramen","desc":"Flavorful and bodied, be prepared to have all your favorite comfort food needs met with one dish","price":120},
    300: {"name":"Onigiri","desc":"A snack for anytime in the day","price":60},
    400: {"name":"Sushi","desc":"Famous vinegared rice rolls with choice of fish sashimi. Served with radish and wasabi on the side","price":150},
    500: {"name":"Chicken Katsu","desc":"Tender breaded chicken cutlets","price":120},
    600: {"name":"Iced Tea","desc":"A refreshing classic","price":50}
}

branches = {
    1: {"name":"Ortigas Plaza","phonenumber":"(043)3123751","location_x":"121.1030707","location_y":"14.58908871"},
    2: {"name":"Shangri-La Plaza", "phonenumber":"(043)3123764","location_x":"121.055895","location_y":"14.5806067"},
    3: {"name":"Katipunan", "phonenumber":"(043)3123765","location_x":"121.0741299","location_y":"14.62985071"}
}

users = {
    "alicia.pavia@gmail.com":{"password":"spiderbop123",
                         "first_name":"Alicia",
                         "last_name":"Pavia"},
    "paris.carbonell@gmail.com":{"password":"wolverine420",
                         "first_name":"Paris",
                         "last_name":"Carbonell"},
    "joe.ilagan@gmail.com":{"password":"beebopcowboy",
                         "first_name":"Joe",
                         "last_name":"Ilagan"},
    "joben.ilagan@gmail.com":{"password":"mechaenthusiast17",
                         "first_name":"Joben",
                         "last_name":"Ilagan"}
}

def get_customer(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user

def get_product(code):
    return products[code]

def get_products():
    product_list = []

    for i,v in products.items():
        product = v
        product.setdefault("code",i)
        product_list.append(product)

    return product_list

def get_branch(code):
    return branches[code]

def get_branches():
    branch_list = []

    for i,v in branches.items():
        branch = v
        branch.setdefault("code",i)
        branch_list.append(branch)

    return branch_list

def get_user(username):
    try:
       return users[username]
    except KeyError:
       return None
