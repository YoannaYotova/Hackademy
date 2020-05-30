# Hackademy
Simple course management system to hold courses and lectures.

## Requirements
```bash
python -m pip install Django
```

## Models
The model specification is as follows:

#### Courses

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

#### Lectures

Each lecture has:
* Name
* Week
* Course
* URL

#### Tasks

One task has the following attributes:
* Name
* Description
* Due Date
* Course
* Lecture

#### Solutions

The solutions have:
* Task
* Date
* URL - **validated link with solution in GitHub.**

**Note: Each model has admin page.**

## Views

HTML is used for the following views. 

#### Index view
* There is an index view with navigation to all list views.

#### Courses views

* ```education/courses/``` - displays table with all courses. There are options for adding new course, deleting existing and link to the course detail page.
* ```education/courses/<course_id>``` - this is the detailed course page. There is a list of all lectures for the given course with a link to the detail view of the lecture.
* ```education/courses/new/``` - displays a form for creating new course.
* ```education/courses/<course_id>/edit/``` - displays a form to edit some of the course details.

#### Lectures views

* ```education/lectures/``` - displays a list with all lectures.
* ```education/lectures/<lecture_id>``` - table with information for the lecture. It has a link to the related course.
* ```education/lectures/new/``` - displays a form for creating a new lecture.
* ```education/lectures/<lecture_id>/edit/``` - displays a form for editing an existing lecture.