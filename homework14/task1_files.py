"""Homework 14. Task 1 Files"""

# Files
# Напишите программу, которая создает текстовый файл(если его нету)
# 'students.txt'. Запишите в файл список студентов, номер группы, их оценки.
# Каждый студент на новой строке.
# Откройте файл и прочитайте всю информацию из
# него. Напечатайте общее количество студентов, количество студентов для
# каждой группы и среднюю оценку для каждой группы. Допишите эту информацию в
# конец файла. Передусмотрите возможные ошибки и обработайте их.


def calculate_statistics(file_path):
    """This function counts amount of students and average mark
        for each group"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if not lines:
            print('File is empty')
            return

        total_students = len(lines)
        group_counts = {}
        group_scores = {}

        for line in lines:
            parts = line.strip().split(', ')
            if len(parts) == 3:

                group, mark = parts[1], int(parts[2])

                if group not in group_counts:
                    group_counts[group] = 0
                    group_scores[group] = 0

                group_counts[group] += 1
                group_scores[group] += mark

        group_averages = {
            group: group_scores[group] / group_counts[group]
            for group, value in group_counts.items()}

        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'\nTotal amount of students: {total_students}\n')
            for group, value in group_counts.items():
                file.write(f'Group {group}: {group_counts[group]} students, '
                           f'Average mark: {group_averages[group]:.2f}\n')

    except FileNotFoundError:
        print(f'File {file_path} not found.')


def write_file():
    '''This function creates file with students, their group names and marks'''
    with open('students.txt', 'w', encoding='utf-8') as students_file:
        students = ['Vasya Ivanov, group 1, 7\n',
                    'Liza Vetrova, group 1, 8\n',
                    'Petya Petrov, group 2, 8\n',
                    'Katya Sidorova, group 2, 9']
        students_file.writelines(students)


print(write_file())
print(calculate_statistics('students.txt'))
