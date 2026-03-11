def get_file_id(message):

    if message.document:
        return message.document.file_id

    if message.photo:
        return message.photo[-1].file_id

    if message.video:
        return message.video.file_id

    return None