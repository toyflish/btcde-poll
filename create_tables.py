
from main import db


if __name__ == '__main__':
    print('Creating all database tables...')
    db.create_all()
    print('Done!')
# [END all]
