# System integration test


# Install virtual environment:
pip install virtualenv

# Create virtual environment:
virtualenv venv

# Activate virtual environment:
Windows: ".\venv\Scripts\activate.bat"
Linux: "source venv/bin/activate"

# To install all required libraries from requirements.txt:
pip install -r requirements.txt

# To get all required libraries from pip:
pip list

# To create requirements.txt
pip list -> requirements.txt

# For Deactivate virtual environment run following command:
deactivate

# Run tests:
    To run all test:
        pytest tests -v

    To run health check tests
        pytest tests -v -m health    

    To run only smoke tests
        pytest tests -v -m smoke
    
    To run regression tests
        pytest tests -v -m regression

# Run tests on different envs:
### To Run test on QA env:
### `pytest -m ui --env="qa"`
### To run tests on DEV env:   
### `pytest -m ui --env="dev"`
