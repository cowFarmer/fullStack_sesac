from manager.read_file import ReadFile


class GetUuid:
    def get_uuid_from_data(self, target_category, target_feature):
        read_file = ReadFile(target_category, target_feature)
        data = read_file.read_feature()
        return data