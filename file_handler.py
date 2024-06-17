import os


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def load_prime_numbers_file(self):
        with open(self.get_file_path(), "r") as f:
            return yaml.safe_load(f)

    def save_prime_numbers_to_file(self, configs):
        with open(self.get_file_path(), "w") as f:
            return yaml.safe_dump(configs, f, default_flow_style=False)

    def get_file_path(self):
        return os.path.join(os.path.dirname(__file__), self.filename)
