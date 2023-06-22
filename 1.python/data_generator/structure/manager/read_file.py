class ReadFile:
    def __init__(self, filename, append_list):
        self.filename = filename
        self.append_list = append_list
    
    def read(self):
        with open("./src/" + self.filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                self.append_list.append(line.strip())
        file.close()
        return list(set(self.append_list))