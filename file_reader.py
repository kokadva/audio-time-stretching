class FileReader(object):

    def __init__(self, file_path):
        self.index = 0
        f = open(file_path, 'rb')
        self.file_name = f.name
        self.data = f.read()
        f.close()
        self.length = len(self.data)


    def has_next(self):
        return self.index < self.length

    def next_byte(self):
        output = self.data[self.index]
        self.index += 1
        return output

    def next_string(self, length):
        output = self.data[self.index:self.index + length].decode('utf-8')
        self.index += length
        return output

    def next_int(self, byte_length):
        output = int.from_bytes(self.data[self.index:self.index + byte_length], 'little')
        self.index += byte_length
        return output

    def skip_bytes(self, byte_length):
        self.index += byte_length
