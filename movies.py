import mysql.connector


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="MovieReviewDB"
    )


def sign_up(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()
    print("Sign Up Successful!")


def sign_in(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None


def edit_profile(user_id, new_username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET username=%s WHERE id=%s", (new_username, user_id))
    conn.commit()
    cursor.close()
    conn.close()


def change_password(user_id, new_password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password=%s WHERE id=%s", (new_password, user_id))
    conn.commit()
    cursor.close()
    conn.close()


def display_all_movies():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    cursor.close()
    conn.close()
    return movies


def create_review(user_id, movie_id, review_text):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reviews (user_id, movie_id, review_text) VALUES (%s, %s, %s)",
                   (user_id, movie_id, review_text))
    conn.commit()
    cursor.close()
    conn.close()


def edit_review(review_id, new_review_text):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE reviews SET review_text=%s WHERE id=%s", (new_review_text, review_id))
    conn.commit()
    cursor.close()
    conn.close()


def delete_review(review_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reviews WHERE id=%s", (review_id,))
    conn.commit()
    cursor.close()
    conn.close()


def display_all_reviews():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews")
    reviews = cursor.fetchall()
    cursor.close()
    conn.close()
    return reviews


def display_my_reviews(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews WHERE user_id=%s", (user_id,))
    reviews = cursor.fetchall()
    cursor.close()
    conn.close()
    return reviews


def display_shared_reviews(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reviews WHERE shared_with=%s", (user_id,))
    reviews = cursor.fetchall()
    cursor.close()
    conn.close()
    return reviews


def share_review(review_id, shared_with):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE reviews SET shared_with=%s WHERE id=%s", (shared_with, review_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Review shared successfully!")


def menu():
    while True:
        print("\nMovie Review System")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Edit Profile")
        print("4. Change Password")
        print("5. Display All Movies")
        print("6. Create Review")
        print("7. Edit Review")
        print("8. Delete Review")
        print("9. Display All Reviews")
        print("10. Display My Reviews")
        print("11. Display Shared Reviews")
        print("12. Share Review")
        print("13. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            username = input("Enter username: ")
            password = input("Enter password: ")
            sign_up(username, password)
        elif choice == 2:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if sign_in(username, password):
                print("Sign In Successful!")
            else:
                print("Invalid Credentials!")
        elif choice == 3:
            user_id = int(input("Enter User ID: "))
            new_username = input("Enter new username: ")
            edit_profile(user_id, new_username)
        elif choice == 4:
            user_id = int(input("Enter User ID: "))
            new_password = input("Enter new password: ")
            change_password(user_id, new_password)
        elif choice == 5:
            movies = display_all_movies()
            for movie in movies:
                print(movie)
        elif choice == 6:
            user_id = int(input("Enter User ID: "))
            movie_id = int(input("Enter Movie ID: "))
            review_text = input("Enter Review: ")
            create_review(user_id, movie_id, review_text)
        elif choice == 7:
            review_id = int(input("Enter Review ID: "))
            new_review_text = input("Enter new review text: ")
            edit_review(review_id, new_review_text)
        elif choice == 8:
            review_id = int(input("Enter Review ID: "))
            delete_review(review_id)
        elif choice == 9:
            reviews = display_all_reviews()
            for review in reviews:
                print(review)
        elif choice == 10:
            user_id = int(input("Enter User ID: "))
            reviews = display_my_reviews(user_id)
            for review in reviews:
                print(review)
        elif choice == 11:
            user_id = int(input("Enter User ID: "))
            reviews = display_shared_reviews(user_id)
            for review in reviews:
                print(review)
        elif choice == 12:
            review_id = int(input("Enter Review ID: "))
            shared_with = int(input("Enter User ID to share with: "))
            share_review(review_id, shared_with)
        elif choice == 13:
            print("Exiting...")
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    menu()
