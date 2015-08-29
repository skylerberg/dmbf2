from dmbf2 import app
from dmbf2 import db


def main():
    db.create_tables()
    app.run(debug=True)


if __name__ == "__main__":
    main()
