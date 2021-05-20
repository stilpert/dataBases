import redis
from listeners.JournalListener import JournalListener
from emulators.userEmulator import UserEmulator
from emulators.workerEmulator import WorkerEmulator
from views.adminView import AdminView
from neo4j import GraphDatabase




from views.login import LoginView
if __name__ == '__main__':
    r = redis.Redis()
    client = JournalListener(r, ['journal'])
    client.start()
    driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "citizen"))
    session = driver.session()

    state = {'redis': r, 'neo4j': session}

    names = ['David', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen']

    print("Input number of users from 1 to 10")
    try:
        usersNum = int(input())
    except ValueError:
        print("Incorrect input")
        exit()

    print("Input number of workers from 1 to 10")
    try:
        workersNum = int(input())
    except ValueError:
        print("Incorrect input")
        exit()

    for i in range(usersNum):
        UserEmulator(state, names[i]).start()

    for i in range(workersNum):
        WorkerEmulator(state).start()
    driver.close()
    AdminView(state).show()
