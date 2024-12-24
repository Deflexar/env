# env
Method for read .env file in project.

example:
```py
import os
from your_file import env

env()

print(os.environ["PASSWORD"])
print(os.getenv("PASSWORD))
```
