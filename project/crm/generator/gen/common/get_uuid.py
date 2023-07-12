import random

from manager.read_file import ReadFile


class GetUuid:
    def get_uuid_from_data(self, target_category, target_feature):
        data = ReadFile(target_category, target_feature)
        return data