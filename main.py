"""
COMP90049 Introduction to Machine Learning
2026 Semester 1
Assignment 1

DO NOT CHANGE THIS FILE!
"""

import os
import sys
import gc

def verify_task1():
    try:
        from task1 import task1
    except ImportError:
        print("Task 1's function not found.")
        return

    print("=" * 80)
    print("Executing Task 1...\n")
    
    task1()

    print("Checking Task 1's output...\n")
    if os.path.isfile("task1_statistics.json"):
        print("\tTask 1's JSON output found.\n")
    else:
        print("\tTask 1's JSON output NOT found. Please check your code.\n")

    print("Finished Task 1.")
    print("=" * 80)

def verify_task2():
    try:
        from task2 import task2
    except ImportError:
        print("Task 2's function not found.")
        return

    print("=" * 80)
    print("Executing Task 2...\n")
    
    task2()

    print("Checking Task 2's output...\n")
    if os.path.isfile("task2_discriminative_power.png"):
        print("\tTask 2's PNG output found.\n")
    else:
        print("\tTask 2's PNG output NOT found. Please check your code.\n")

    print("Finished Task 2.")
    print("=" * 80)

def verify_task3():
    try:
        from task3 import task3
    except ImportError:
        print("Task 3's function not found.")
        return

    print("=" * 80)
    print("Executing Task 3...\n")
    
    task3()

    print("Checking Task 3's output...\n")
    if os.path.isfile("task3_unscaled_knn_accuracy.json"):
        print("\tTask 3's JSON output found.\n")
    else:
        print("\tTask 3's JSON output NOT found. Please check your code.\n")
    
    if os.path.isfile("task3_scaled_knn_accuracy.json"):
        print("\tTask 3's JSON output found.\n")
    else:
        print("\tTask 3's JSON output NOT found. Please check your code.\n")

    print("Finished executing Task 3.")
    print("=" * 80)

def verify_task4():
    try:
        from task4 import task4
    except ImportError:
        print("Task 4's function not found.")
        return

    print("=" * 80)
    print("Executing Task 4...\n")
    
    task4()

    print("Checking Task 4's output...\n")
    if os.path.isfile("task4_gnb_accuracy.json"):
        print("\tTask 4's JSON output found.\n")
    else:
        print("\tTask 4's JSON output NOT found. Please check your code.\n")

    if os.path.isfile("task4_gnb_heatmap.png"):
        print("\tTask 4's PNG output found.\n")
    else:
        print("\tTask 4's PNG output NOT found. Please check your code.\n")

    if os.path.isfile("task4_gnb_performance.json"):
        print("\tTask 4's JSON output found.\n")
    else:
        print("\tTask 4's JSON output NOT found. Please check your code.\n")

    print("Finished executing Task 4.")
    print("=" * 80)

def verify_task5():
    try:
        from task5 import task5
    except ImportError:
        print("Task 5's function not found.")
        return

    print("=" * 80)
    print("Executing Task 5...\n")
    
    task5()

    print("Checking Task 5's output...\n")
    if os.path.isfile("task5_dt_statistics.json"):
        print("\tTask 5's JSON output found.\n")
    else:
        print("\tTask 5's JSON output NOT found. Please check your code.\n")
    
    if os.path.isfile("task5_dt_visualisation.png"):
        print("\tTask 5's PNG output found.\n")
    else:
        print("\tTask 5's PNG output NOT found. Please check your code.\n")

    print("Finished executing Task 5.")
    print("=" * 80)

def verify_task6():
    try:
        from task6 import task6
    except ImportError:
        print("Task 6's function not found.")
        return

    print("=" * 80)
    print("Executing Task 6...\n")

    task6()

    print("Checking Task 6's output...\n")

    if os.path.isfile("task6_svm_accuracy.png"):
        print("\tTask 6's PNG output found.\n")
    else:
        print("\tTask 6's PNG output NOT found. Please check your code.\n")

    print("Finished executing Task 6.")
    print("=" * 80)

def verify_task7():
    try:
        from task7 import task7
    except ImportError:
        print("Task 7's function not found.")
        return

    print("=" * 80)
    print("Executing Task 7...\n")

    gc.collect()  # flush memory accumulated from tasks 1–6
    task7()

    print("Checking Task 7's output...\n")
    if os.path.isfile("task7_logistic_regression.json"):
        print("\tTask 7's JSON output found.\n")
    else:
        print("\tTask 7's JSON output NOT found. Please check your code.\n")

    print("Finished executing Task 7.")
    print("=" * 80)

def verify_discussion():
    print("=" * 80)
    print("Checking for discussion...\n")
    
    if os.path.isfile("template_discussion_section.pdf"):
        print("\ttemplate_discussion_section.pdf file found.\n")
    else:
        print("\ttemplate_discussion_section.pdf file NOT found. Please check your code.\n")

    print("Finished checking for discussion")
    print("=" * 80)

def main():
    args = sys.argv
    assert len(args) >= 2, "Please provide a task."
    task = args[1]
    assert task in ["all"] + ["discussion"]+ ["task" + str(i) for i in range(1, 9)], \
        "Invalid task."
    if task == "task1":
        verify_task1()
    elif task == "task2":
        verify_task2()
    elif task == "task3":
        verify_task3()
    elif task == "task4":
        verify_task4()
    elif task == "task5":
        verify_task5()
    elif task == "task6":
        verify_task6()
    elif task == "task7":
        verify_task7()
    elif task == "discussion":
        verify_discussion()
    elif task == "all":
        verify_task1()
        verify_task2()
        verify_task3()
        verify_task4()
        verify_task5()
        verify_task6()
        verify_task7()
        verify_discussion()

if __name__ == "__main__":
    main()
