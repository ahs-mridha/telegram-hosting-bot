from database import cursor,conn
from config import MAX_BOTS_PER_DAY,MAX_IMAGES_PER_DAY

def allow_bot(user):

    cursor.execute(
    "SELECT bots_today FROM users WHERE user_id=?",
    (user,)
    )

    count = cursor.fetchone()[0]

    if count >= MAX_BOTS_PER_DAY:
        return False

    cursor.execute(
    "UPDATE users SET bots_today=bots_today+1 WHERE user_id=?",
    (user,)
    )

    conn.commit()
    return True


def allow_image(user):

    cursor.execute(
    "SELECT images_today FROM users WHERE user_id=?",
    (user,)
    )

    count = cursor.fetchone()[0]

    if count >= MAX_IMAGES_PER_DAY:
        return False

    cursor.execute(
    "UPDATE users SET images_today=images_today+1 WHERE user_id=?",
    (user,)
    )

    conn.commit()
    return True