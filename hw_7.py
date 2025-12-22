import sqlite3


def create_table():
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

    connection.commit()
    connection.close()


def insert_books():
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO books
        (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES
        ('1984', 'George Orwell', 1949, 'Dystopia', 328, 5),
        ('Animal Farm', 'George Orwell', 1945, 'Political satire', 112, 4),
        ('Harry Potter', 'J.K. Rowling', 1997, 'Fantasy', 320, 7),
        ('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy', 310, 6),
        ('Fahrenheit 451', 'Ray Bradbury', 1953, 'Science Fiction', 256, 3),
        ('The Little Prince', 'Antoine de Saint-Exupéry', 1943, 'Fairy tale', 96, 8),
        ('Crime and Punishment', 'Fyodor Dostoevsky', 1866, 'Classic', 671, 2),
        ('War and Peace', 'Leo Tolstoy', 1869, 'Classic', 1225, 1),
        ('The Alchemist', 'Paulo Coelho', 1988, 'Philosophy', 208, 5),
        ('Jane Eyre', 'Charlotte Brontë', 1847, 'Novel', 500, 4)
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_table()
    insert_books()
    print("Table created and books inserted successfully!")


