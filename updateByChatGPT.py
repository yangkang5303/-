# -*- coding: utf-8 -*-
import random
import time

def distribute_students(total_students, num_classes):
    """分配学生到各个班级"""
    students_per_class = total_students // num_classes
    students_left = total_students % num_classes
    return [students_per_class + (1 if i < students_left else 0) for i in range(num_classes)]

def print_class_distribution(class_num, total_students, male_students, female_students, male_names, female_names):
    """打印班级分配情况"""
    print(f"{class_num}班 {total_students}人；其中，{male_students}位男生，{female_students}位女生")
    for i in range(male_students):
        print(f"男 {male_names[i]}号")
    for i in range(female_students):
        print(f"女 {female_names[i]}号")

def main():
    total_male = 160
    total_female = 100
    num_classes = 7

    print(f"一共 {total_male} 个男生，{total_female} 个女生，分 {num_classes} 个班：")

    male_names = list(range(1, total_male + 1))
    female_names = list(range(1, total_female + 1))
    random.shuffle(male_names)
    random.shuffle(female_names)

    male_distribution = distribute_students(total_male, num_classes)
    female_distribution = distribute_students(total_female, num_classes)
    total_distribution = [male_distribution[i] + female_distribution[i] for i in range(num_classes)]

    print("班级总人数", total_distribution)
    print("男生总人数", male_distribution)
    print("女生总人数", female_distribution)

    # 开始给每个班随机派送男生女生
    male_index = 0
    female_index = 0
    for i in range(num_classes):
        male_count = male_distribution[i]
        female_count = female_distribution[i]
        print_class_distribution(i + 1, total_distribution[i], male_count, female_count, male_names[male_index:male_index + male_count], female_names[female_index:female_index + female_count])
        male_index += male_count
        female_index += female_count

    print("分班完成！本对话框三分钟后自动退出，请将屏幕内容全部复制粘贴到word或wps文字处理")
    time.sleep(180)

if __name__ == "__main__":
    main()
