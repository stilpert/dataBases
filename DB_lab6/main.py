import redis
from listeners.JournalListener import JournalListener

from views.login import LoginView
if __name__ == '__main__':
    r = redis.Redis()

    client = JournalListener(r, ['journal'])
    client.start()

    state = {'redis': r}
    LoginView(state).show()


