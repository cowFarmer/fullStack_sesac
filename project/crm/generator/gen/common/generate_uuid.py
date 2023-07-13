import uuid


class GenerateUuid:
    def get_uuid(self):
        new_uuid = uuid.uuid4()
        return str(new_uuid)