# Project Documentation: Student Performance Analytics System

## 1. Project Title and Student Details

**Project title:** Student Performance Analytics System  
**Student name:** [Enter your name]  
**Course:** Python with AI  
**College/Institute:** [Enter your college]  
**Submission date:** [Enter date]

## 2. Objective

The objective is to build a Python-based system that reads student records, analyzes marks, assigns grades, identifies pass/fail status, summarizes subject performance, and highlights top-performing students. The project demonstrates core Python, NumPy, and Pandas skills.

## 3. Technologies Used

- **Python:** program flow, functions, loops/conditions, and reporting.
- **Pandas:** CSV reading, DataFrame processing, grouping, sorting, and summaries.
- **NumPy:** numerical totals, averages, and pass/fail classification.
- **CSV:** stores the sample student dataset.

## 4. Dataset Description

The `students.csv` dataset contains 20 fictional student records. Its columns are:

| Column | Description |
|---|---|
| Student_ID | Unique sample student identifier |
| Name | Fictional student name |
| Department | Department label |
| Python | Marks out of 100 |
| Statistics | Marks out of 100 |
| Database | Marks out of 100 |
| Communication | Marks out of 100 |
| Attendance | Attendance percentage |

The data is synthetic for demonstration. Attendance is included in the dataset but is not used to calculate grades.

## 5. Implementation

1. **Load data:** `load_data()` reads `students.csv` using `pandas.read_csv()` and checks for required columns and an empty dataset.
2. **Validate marks:** subject marks are converted to numeric values and checked for missing/non-numeric values and values outside 0–100.
3. **Calculate results:** `calculate_student_results()` uses NumPy to calculate total marks and average marks.
4. **Assign grades:** an inner function maps the average to a grade using `if/elif/else`.
5. **Determine pass/fail:** a student passes only if every subject score is at least 40.
6. **Summarize the class:** functions report student count, overall class average, highest and lowest average, and pass/fail counts.
7. **Analyze subjects and departments:** Pandas aggregation and `groupby()` produce subject and department summaries.
8. **Find top performers:** `nlargest()` ranks students by average marks.
9. **Export results:** the processed DataFrame is saved as `student_results.csv`.

## 6. Key Features

- CSV loading with Pandas.
- NumPy-based numerical calculations.
- Total and average marks for each student.
- Grade and pass/fail classification.
- Class-level summary statistics.
- Subject-wise and department-wise comparisons.
- Top-five performer list.
- Export of processed student results.
- Basic validation and error messages.

## 7. Output / Screenshots

After running `python main.py`, insert screenshots of:
1. The overall class summary.
2. Subject-wise and department-wise analysis.
3. The top-five performer list.
4. The detailed student report and generated `student_results.csv`.

**Note:** Add screenshots from your own successful run; do not insert fabricated screenshots.

## 8. Final Outcome

The system transforms a CSV file into a readable performance report. It demonstrates how Python, NumPy, and Pandas can support basic educational data analysis. The project reports descriptive statistics and does not make predictions.

## 9. Challenges and Learning

Complete this section honestly after testing. Example prompts:
- What issue did you face while reading or validating the CSV?
- How did you check that marks were in the allowed range?
- What did you learn about NumPy arrays and Pandas DataFrames?
- How did functions make the program easier to maintain?

## 10. GitHub Repository

**Repository URL:** [Paste your GitHub repository URL here]

## Grading Rules Used

- A+: average >= 90
- A: average >= 80 and < 90
- B: average >= 70 and < 80
- C: average >= 60 and < 70
- D: average >= 50 and < 60
- F: average < 50

A pass requires a score of at least 40 in every subject. These are project-defined rules and should be adjusted if the instructor specifies different rules.

## How to Run

```bash
python -m pip install -r requirements.txt
python main.py
```
