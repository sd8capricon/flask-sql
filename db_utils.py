import sqlite3

# Helper function to run app


def execute_query(query):
    conn = sqlite3.connect('database.db')
    res = conn.execute(query)
    conn.commit()
    return res


# Returns a list of all restaurant reviews


def get_reviews():
    reviews = execute_query("select * from reviews;").fetchall()
    # fetchall returns all rows of the result
    data = []
    print(reviews)

# To write a review


def create_review(name, review):
    # insert into reviews(name, review) values(name, review);
    pass


# To change existing review values


def update_review(id, restaurant, review):
    # update reviews set name = 'new value', review='new value' where id=existing_id;
    pass


# To delete a review

def delete_review(id):
    # delete from reviews where id=existing_id;
    pass

# Funcion to get restaurant by id


def get_restaurant(id):
    restaurant = execute_query(
        f"select * from reviews where id='{id}';").fetchone()
    # fetchone returns first row of the result
    temp = {'id': restaurant[0],
            'restaurant': restaurant[1], 'review': restaurant[2]}
    return temp
