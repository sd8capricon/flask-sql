import sqlite3


def execute_query(query):
    conn = sqlite3.connect('database.db')
    res = conn.execute(query)
    conn.commit()
    return res


def get_reviews():
    reviews = execute_query("select * from reviews;").fetchall()
    data = []
    temp = {}
    for i in reviews:
        temp['id'] = i[0]
        temp["name"] = i[1]
        temp["review"] = i[2]
        data.append(temp)
        temp = {}
    return data


def create_review(name, review):
    print(
        f"insert into reviews(name, review) values('{name}', '{review}');")
    execute_query(
        f"insert into reviews(name, review) values('{name}', '{review}');")


def update_review(id, name, review):
    print(
        f"update reviews set name = '{name}', review = '{review}' where id='{id}';")
    execute_query(
        f"update reviews set name = '{name}', review = '{review}' where id='{id}';")


def delete_review(id):
    execute_query(f"delete from reviews where id='{id}';")


def get_restaurant(id):
    restaurant = execute_query(
        f"select * from reviews where id='{id}';").fetchone()
    temp = {'id': restaurant[0],
            'name': restaurant[1], 'review': restaurant[2]}
    return temp
