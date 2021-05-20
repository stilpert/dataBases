# from listeners.JournalListener import JournalListener
import pymongo
from view import View


if __name__ == '__main__':
    my_client = pymongo.MongoClient("mongodb://localhost:43000/")
    mydb = my_client["karpatydb"]
    state = {'db': mydb}
    View(state).show()
