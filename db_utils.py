import sqlite3


def execute_query(query):
    conn = sqlite3.connect('database.db')
    res = conn.execute(query)
    conn.commit()
    return res


def get_reviews():
    reviews = execute_query("SELECT * FROM REVIEWS;").fetchall()
    data = []
    temp = {}
    for i in reviews:
        temp['id'] = i[0]
        temp["restaurant"] = i[1]
        temp["review"] = i[2]
        data.append(temp)
        temp = {}
    return data


def create_review(restaurant, review):
    print(
        f"INSERT INTO REVIEWS(restaurant, review) VALUES('{restaurant}', '{review}');")
    execute_query(
        f"INSERT INTO REVIEWS(restaurant, review) VALUES('{restaurant}', '{review}');")


def update_review(id, review):
    print(f"UPDATE REVIEWS SET review = '{review}' WHERE id='{id}';")
    execute_query(
        f"UPDATE REVIEWS SET review = '{review}' WHERE id='{id}';")


def delete_review(id):
    execute_query(f"DELETE FROM REVIEWS WHERE id='{id}';")


def get_restaurant(id):
    restaurant = execute_query(
        f"SELECT * FROM REVIEWS WHERE id='{id}';").fetchone()
    temp = {'id': restaurant[0],
            'restaurant': restaurant[1], 'review': restaurant[2]}
    return temp
