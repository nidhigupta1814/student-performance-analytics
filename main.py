"""
Student Performance Analytics System
Python + NumPy + Pandas mini-project.

Run:
    pip install -r requirements.txt
    python main.py
"""

from pathlib import Path
import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).parent / "students.csv"
SUBJECTS = ["Python", "Statistics", "Database", "Communication"]
PASS_MARK = 40
ATTENDANCE_COLUMN = "Attendance"


def load_data(file_path=DATA_FILE):
    """Load student records from a CSV file and validate required columns."""
    data = pd.read_csv(file_path)
    required_columns = [
        "Student_ID", "Name", "Department",
        *SUBJECTS, ATTENDANCE_COLUMN
    ]
    missing = [column for column in required_columns if column not in data.columns]
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")
    if data.empty:
        raise ValueError("The dataset contains no student records.")
    return data


def calculate_student_results(data):
    """Return a copy of the data with total, average, grade, and result columns."""
    results = data.copy()
    marks = results[SUBJECTS].apply(pd.to_numeric, errors="coerce")

    if marks.isna().any().any():
        raise ValueError("Subject marks must contain valid numeric values.")
    if ((marks < 0) | (marks > 100)).any().any():
        raise ValueError("Subject marks must be between 0 and 100.")

    results["Total_Marks"] = np.sum(marks.to_numpy(), axis=1)
    results["Average_Marks"] = np.round(np.mean(marks.to_numpy(), axis=1), 2)

    def assign_grade(average):
        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    results["Grade"] = results["Average_Marks"].apply(assign_grade)
    # A student passes only if every subject mark is at least PASS_MARK.
    results["Result"] = np.where((marks >= PASS_MARK).all(axis=1), "Pass", "Fail")
    return results


def print_overall_summary(results):
    """Print class-level statistics."""
    averages = results["Average_Marks"].to_numpy()
    top_index = results["Average_Marks"].idxmax()
    low_index = results["Average_Marks"].idxmin()

    print("\n" + "=" * 62)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 62)
    print(f"Number of students       : {len(results)}")
    print(f"Overall class average    : {np.mean(averages):.2f}")
    print(f"Highest student average  : {results.loc[top_index, 'Name']} "
          f"({results.loc[top_index, 'Average_Marks']:.2f})")
    print(f"Lowest student average   : {results.loc[low_index, 'Name']} "
          f"({results.loc[low_index, 'Average_Marks']:.2f})")
    print(f"Students passed          : {(results['Result'] == 'Pass').sum()}")
    print(f"Students failed          : {(results['Result'] == 'Fail').sum()}")


def print_subject_analysis(results):
    """Show each subject's average, highest mark, and lowest mark."""
    subject_summary = results[SUBJECTS].agg(["mean", "max", "min"]).T
    subject_summary.columns = ["Average", "Highest", "Lowest"]
    subject_summary = subject_summary.round(2)

    print("\nSUBJECT-WISE ANALYSIS")
    print("-" * 62)
    print(subject_summary.to_string())


def print_department_analysis(results):
    """Compare average student performance across departments."""
    summary = results.groupby("Department")["Average_Marks"].mean().round(2)
    print("\nDEPARTMENT-WISE AVERAGE")
    print("-" * 62)
    print(summary.to_string())


def print_top_performers(results, count=5):
    """Display the top students ranked by average marks."""
    top_students = results.nlargest(count, "Average_Marks")
    print(f"\nTOP {count} PERFORMERS")
    print("-" * 62)
    print(top_students[["Student_ID", "Name", "Department",
                        "Average_Marks", "Grade"]].to_string(index=False))


def print_student_report(results):
    """Display a compact report for every student."""
    columns = ["Student_ID", "Name", "Department", "Total_Marks",
               "Average_Marks", "Grade", "Result", ATTENDANCE_COLUMN]
    print("\nSTUDENT REPORT")
    print("-" * 90)
    print(results[columns].to_string(index=False))


def main():
    try:
        data = load_data()
        results = calculate_student_results(data)
        print(f"\nLoaded {len(data)} student records from: {DATA_FILE.name}")
        print_overall_summary(results)
        print_subject_analysis(results)
        print_department_analysis(results)
        print_top_performers(results)
        print_student_report(results)

        output_file = Path(__file__).parent / "student_results.csv"
        results.to_csv(output_file, index=False)
        print(f"\nDetailed results saved to: {output_file.name}")
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
