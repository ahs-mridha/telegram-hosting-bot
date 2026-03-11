from database import cursor,conn

def save_file(name,file_id,desc):

    cursor.execute(
    "INSERT INTO files VALUES(?,?,?)",
    (name,file_id,desc)
    )

    conn.commit()


def get_file(name):

    cursor.execute(
    "SELECT file_id FROM files WHERE name=?",
    (name,)
    )

    data = cursor.fetchone()

    if data:
        return data[0]

    return None