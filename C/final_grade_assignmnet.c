/*-----------------------------------------------------------------------------------
 * Name:        final_grade_assignment.c
 * Purpose:     Calculate final grade for C programming class
 * Notes:       Best attempt at a final grade calculator for a C programming class. 
                Program includes exception handling for invalid inputs and divide by zero errors.

-----------------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

void print_help();
void enter_data();
void calculate_average();
void calculate_grade();
char get_letter_grade(int);

// Note: had to change labs to laboratories because labs is a function in stdlib.h and was causing a conflict.
int tests[3], num_tests = 0;
int programs[7], num_programs = 0;
int laboratories[9], num_laboratories = 0;
int exercises[9], num_exercises = 0;
int attendance[1], num_attendance = 0;

int main() {
    char command[20];
    while (true) {
        printf("Enter command (type help to see all commands): ");
        fgets(command, sizeof(command), stdin);
        for (int i = 0; i < strlen(command); ++i) {
            command[i] = tolower(command[i]);
        }
        if (strstr(command, "help")) {
            print_help();
        } else if (strstr(command, "enter")) {
            enter_data();
        } else if (strstr(command, "average")) {
            calculate_average();
        } else if (strstr(command, "grade")) {
            calculate_grade();
        } else if (strstr(command, "exit")) {
            printf("Exiting program ...\n");
            break;
        } else {
            printf("Invalid command: %s\n", command);
        }
    }
    return 0;
}

void print_help() {
    char help_text[] = "Commands:\n"
                       "help:    print this command list\n"
                       "enter:   enter values for one type of assignment\n"
                       "average: calculate/print average for one type of assignment\n"
                       "grade:   calculate/print letter grade based on assignment scores\n"
                       "exit:    exit program";
    printf("%s\n", help_text);
}

void enter_data() {
    char category[20];
    int limit;
    printf("Category to enter (tests, programs, labs, exercises, attendance): ");
    fgets(category, sizeof(category), stdin);
    for (int i = 0; i < strlen(category); ++i) {
        category[i] = tolower(category[i]);
    }

    if (strstr(category, "tests")) {
        limit = 3;
    } else if (strstr(category, "programs")) {
        limit = 7;
    } else if (strstr(category, "labs")) {
        limit = 9;
    } else if (strstr(category, "exercises")) {
        limit = 9;
    } else if (strstr(category, "attendance")) {
        limit = 1;
    } else {
        printf("Invalid category: %s\n", category);
        return;
    }

    for (int i = 0; i < limit; ++i) {
        int score;
        if (strstr(category, "attendance")) {
            printf("Enter attendance score (0-5): ");
        } else {
            printf("Enter score %d (0-100): ", i + 1);
        }
        scanf("%d", &score);
        getchar(); // To consume the newline from scanf

        if (strstr(category, "tests")) {
            tests[num_tests++] = score;
        } else if (strstr(category, "programs")) {
            programs[num_programs++] = score;
        } else if (strstr(category, "labs")) {
            laboratories[num_laboratories++] = score;
                } else if (strstr(category, "exercises")) {
            exercises[num_exercises++] = score;
        } else if (strstr(category, "attendance")) {
            attendance[num_attendance++] = score;
        }
    }
}

void calculate_average() {
    char category[20];
    int total = 0;
    int count = 0;
    printf("Enter category to average (programs, labs, exercises): ");
    fgets(category, sizeof(category), stdin);
    for (int i = 0; i < strlen(category); ++i) {
        category[i] = tolower(category[i]);
    }

    if (strstr(category, "programs")) {
        for (int i = 0; i < num_programs; ++i) {
            total += programs[i];
        }
        count = num_programs;
    } else if (strstr(category, "labs")) {
        for (int i = 0; i < num_laboratories; ++i) {
            total += laboratories[i];
        }
        count = num_laboratories;
    } else if (strstr(category, "exercises")) {
        for (int i = 0; i < num_exercises; ++i) {
            total += exercises[i];
        }
        count = num_exercises;
    } else {
        printf("Invalid category: %s\n", category);
        return;
    }

    if (count == 0) {
        printf("No scores entered for %s\n", category);
    } else {
        float average = (float)total / count;
        printf("Average for %s: %.2f\n", category, average);
    }
}

void calculate_grade() {
    if (num_tests != 3 || num_programs == 0 || num_laboratories == 0 || num_exercises == 0 || num_attendance == 0) {
        printf("Enter scores for all assignments before calculating grade.\n");
        return;
    }

    int lab_avg = 0, program_avg = 0, exercise_avg = 0, attend = 0;
    for (int i = 0; i < num_laboratories; ++i) {
        lab_avg += laboratories[i];
    }
    lab_avg = lab_avg * 0.2 / num_laboratories;

    for (int i = 0; i < num_programs; ++i) {
        program_avg += programs[i];
    }
    program_avg = program_avg * 0.2 / num_programs;

    for (int i = 0; i < num_exercises; ++i) {
        exercise_avg += exercises[i];
    }
    exercise_avg = exercise_avg * 0.1 / num_exercises;

    attend = attendance[0] * 1;

    int highest_test = tests[0];
    int other_tests = tests[1] + tests[2];

    if (tests[1] > highest_test) {
        highest_test = tests[1];
        other_tests = tests[0] + tests[2];
    }

    if (tests[2] > highest_test) {
        highest_test = tests[2];
        other_tests = tests[0] + tests[1];
    }

    highest_test *= 0.15;
    other_tests *= 0.1;

    int weighted_avg = lab_avg + program_avg + exercise_avg + attend + highest_test + other_tests;
    char letter_grade = get_letter_grade(weighted_avg);

        printf("Weighted average: %.2f\n", (float)weighted_avg);
        printf("Letter grade: %c\n", letter_grade);
}

char get_letter_grade(int average) {
    int rounded_average = (average < 0) ? (average - 5) / 10 : (average + 5) / 10;
    rounded_average *= 10;

    if (rounded_average >= 90) {
        return 'A';
    } else if (rounded_average >= 80) {
        return 'B';
    } else if (rounded_average >= 70) {
        return 'C';
    } else if (rounded_average >= 60) {
        return 'D';
    } else {
        return 'F';
    }
}

