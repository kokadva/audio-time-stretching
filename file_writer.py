class FileWriter(object):

    def __init__(self, file_path):
        self.file_path = file_path

    def start_writing(self):
        self.file = open(self.file_path, 'wb')

    def finish_writing(self):
        self.file.close()

    def write_int(self, value, byte_length):
        try:
            self.file.write(value.to_bytes(byte_length, byteorder='little'))
        except:
            value = pow(2, 8 * byte_length) - 1
            self.file.write(value.to_bytes(byte_length, byteorder='little'))

    def write_string(self, value):
        self.file.write(value.encode('utf-8'))
