## Audette Take Home
### Setup:
1. Requires Python 3.9+ and pip
2. Clone the github repo
2. Navigate to folder containing `requirements.txt`
3. Create a virtual env using `python3 -m venv venv` and activate it using `source venv/bin/activate`. Other similar commands for creating a python virtualenv can also be used
4. Install the requirements using `pip install -r requirements.txt`

### Run the script for solving the valley map as part of challenge:
1.  Navigate to folder containing `main.py`
2.  Run `python3 main.py` to solve the valley map and output the result
3.  Valley map can be updated to solve for a new case by updating the `valley_map` variable in `main.py` on line `103`

### Running test cases:
1. Test cases are written using pytest
2. Navigate to folder containing `test_valley_map.py`
3. Run test cases using the command `pyest`
