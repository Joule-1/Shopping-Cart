import uuid

def generate_unique_id():
    return str(uuid.uuid1()).split('-')[0]
