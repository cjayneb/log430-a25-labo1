from daos.user_dao_mongo import UserDAOMongo
from models.user import User

dao = UserDAOMongo()

def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """
    dao.insert(User(None, 'Ada Lovelace', 'alovelace@example.com'))
    dao.insert(User(None, 'Adele Goldberg', 'agoldberg@example.com'))
    dao.insert(User(None, 'Alan Turing', 'aturing@example.com'))
