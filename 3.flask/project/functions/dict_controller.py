class DictLower:
    def key_lower(lines):
        data = []
        for line in lines:
            tmp = {key.lower(): value.lower() for key, value in line.items()}
            data.append(tmp)
        return data