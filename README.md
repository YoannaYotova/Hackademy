# Hackademy
Simple course management system to hold courses and lectures.

## Requirements
```bash
python -m pip install Django
```

## Models
The model specification is as follows:

### Courses

They have the following attributes:
* Name
* Description
* Start Date
* End Date 

Here is how the admin page of the Course looks like:
|            Name             | Description | Start Date |  End Date  | Duration |
| --------------------------- | ----------- | ---------- | ---------- | -------- |
|Programming 101 with Python  | Python!     | 01.01.2016 | 01.03.2016 | 3 months |
| Programming 101 with Ruby | Ruby. | 10.01.2016 | 01.03.2016 | 2 months |

### Lectures

Each lecture has:
* Name
* Week
* Course
* URL

### Tasks

One task has the following attributes:
* Name
* Description
* Due Date
* Course
* Lecture

### Solutions

The solutions have:
* Task
* Date
* URL - **validated link with solution in GitHub.**

