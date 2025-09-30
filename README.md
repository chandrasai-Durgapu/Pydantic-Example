# Pydantic-Example
Pydantic-Example

# Create Conda Environment
```bash
conda create -n pydantic-example python=3.13 -y
```

## Activate Conda Environment
```bash
conda activate pydantic-example
```
---
## Install Dependencies
```bash
pip install requirements.txt
```
---
### 1_pydantic.py
Introduces a basic Pydantic BaseModel.

Shows type enforcement and validation.
run the code
```bash
python 1_pydantic.py
```
---

### 2_pydantic.py

Expands on the first file with field validation (e.g., email, regex).

May include constraints like min_length, etc.
run the code
```bash
python 2_pydantic.py
```
---
### 3_Employee.py

Defines an Employee model.

Likely contains real-world fields like name, age, salary.
run the code
```bash
python 3_pydantic.py
```
---

### 4_User_model.py

Focuses on user-related fields like username, email, password.
run the code
```bash
python 4_User_model.py
```
---

### 5_Booking.py

Models a booking system (e.g., user ID, date/time, booking ID).

Probably includes datetime validation.
run the code
```bash
python 5_Booking.py
```
---

### 6_Nested_model.py

Demonstrates nested Pydantic models, e.g., an Order with nested Item data.
run the code
```bash
python 6_Nested_model.py
```
---

### 7_Course_module.py

Likely models courses and modules.

Useful for education platforms or LMS.
run the code
```bash
python 7_Course_module.py
```
---

### 8_serialization.py

Demonstrates how to convert models to/from dicts and JSON (serialization/deserialization).
run the code
```bash
python 8_serialization.py
```
---

