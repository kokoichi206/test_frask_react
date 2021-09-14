import models.database as db

def init():
    db.init_db()

def add_rank():
    from models.database import db_session
    from models.models import Ranks

    c1 = Ranks('Minami', 4_000_000)
    c2 = Ranks('Maiyan', 1_200_000)
    c3 = Ranks('Himura', 300_000)

    db_session.add(c1)
    db_session.add(c2)
    db_session.add(c3)

    db_session.commit()

def select_all():
    from models.database import db_session
    from models.models import Ranks

    return Ranks.query.all()

if __name__ == '__main__':
    init()

    add_rank()

    res = select_all()
    print(res)
    for r in res:
        print(f'{r.id}: {r.name}: {r.amount}: {r.date}')
