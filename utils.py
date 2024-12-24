import os


def env():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, '.env')

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key.strip()] = value.strip()
