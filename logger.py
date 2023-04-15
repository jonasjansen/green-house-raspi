# Logger - Entry point for logging information to file and into database.

import datetime


class Logger:

    def set_log_leve(self):
        pass

    def log(self, message):
        print(datetime.datetime)
        self.write_to_console(message)

    def write_to_console(self, message):
        print(message)

    def write_to_file(self):
        pass

    def debug(self, message):
        self.log(''.join(("DEBUG: ", message)))

    def info(self, message):
        self.log(''.join(("INFO: ", message)))

    def warning(self, message):
        self.log(''.join(("DEBUG: ", message)))

    def error(self, message):
        self.log(''.join(("INFO: ", message)))


logger = Logger()
