# Student Performance Analytics System

A beginner-friendly Python data-analysis mini-project for the **Python with AI** assignment. It uses **Python, NumPy, and Pandas** to analyze student marks and attendance-related records.

## Features

- Reads a CSV dataset with 20 sample student records.
- Calculates each student's total and average across four subjects.
- Assigns a grade based on the average.
- Classifies pass/fail status.
- Reports the class average, highest and lowest student averages, and pass/fail counts.
- Summarizes average, highest, and lowest marks by subject.
- Compares average performance by department.
- Lists the top five performers.
- Exports the complete analysis to `student_results.csv`.
- Includes basic checks for missing columns and invalid marks.

## Technologies

- Python 3.10+
- Pandas
- NumPy

## Project structure

```text
student-performance-analytics/
├── main.py
├── students.csv
├── requirements.txt
├── README.md
├── documentation/
│   └── Project_Documentation.md
└── .gitignore
```

`student_results.csv` is generated when you run the program; it does not need to be committed.

## Setup and run

1. Install Python 3.10 or later.
2. Open a terminal in this project folder.
3. (Optional but recommended) Create and activate a virtual environment.
4. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Run the program:

   ```bash
   python main.py
   ```

The program prints the analysis in the terminal and creates `student_results.csv`.

## Rules used

- Subject marks are expected to be between 0 and 100.
- Pass/fail: a student passes only if they score at least 40 in **every** subject.
- Grades based on average marks:
  - A+: 90–100
  - A: 80–89.99
  - B: 70–79.99
  - C: 60–69.99
  - D: 50–59.99
  - F: below 50

These are project-defined rules, not an official college grading policy.

## Dataset

`students.csv` contains synthetic sample data for 20 fictional students. Subjects are Python, Statistics, Database, and Communication. `Attendance` is a percentage field included to meet the assignment's student-data requirement; it is not used in grade calculation.

## Before submission

- Run `python main.py` and inspect the results.
- Replace sample data with permitted/real data if your trainer requires it, and update the documentation.
- Add your own name, course, college, and output screenshots to the documentation.
- Create a GitHub repository and push the files.
- Submit the repository URL through the Google Form provided by EWB Courses.
- Verify the repository and form submission before **15 October 2026**.

## Limitations

This is a descriptive data-analysis project, not a machine-learning model. It does not predict future marks. The sample dataset is synthetic and should not be presented as real institutional data.
