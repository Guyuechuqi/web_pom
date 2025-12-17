import os
import pytest
import time

if __name__ == "__main__":
    pytest.main()
    os.system("allure generate ./reports/temp -o ./reports/final --clean")