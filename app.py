# -*- coding: utf-8 -*-
import random,time
total_male = 160
total_female = 100
ban = 7

print("一共",total_male,"个男生，",total_female,"个女生，分",ban,"个班：")


male_name  = list(range(1,total_male +1))
female_name  = list(range(1,total_female +1))
random.shuffle(male_name)
random.shuffle(female_name)
# print(male_name)
# print(female_name)

male_of_1ban = total_male//ban
female_of_1ban = total_female//ban

male_left = total_male%ban
female_left = total_female%ban

total_num = [male_of_1ban + female_of_1ban] * ban

male_num = [male_of_1ban] *ban
female_num = [female_of_1ban] *ban

# print(male_of_1ban)
# print(male_left)
#
# print(female_of_1ban)
# print(female_left)


#在人数不能被整除的情况下最大可能地平衡各个班级人数
for i in range(male_left):
    # print(i)
    total_num[i] = total_num[i] + 1
    male_num[i] = male_num[i] +1
    # print(total_num[i])
# print(total_num)

for j in range(female_left):
    # print(j)
    total_num[ban - j - 1] = total_num[ban - j -1 ] + 1
    female_num[ban - j - 1] = female_num[ban - j - 1] +1
    # print(total_num[ban - j -1 ])
print("班级总人数",total_num)
print("男生总人数",male_num)
print("女生总人数",female_num)

#开始给每个班随机派送男生女生
for x in range(ban):
    print(x+1,"班",total_num[x],"人；其中，",male_num[x],"位男生，",female_num[x],"位女生")
    for male in range(male_num[x]):
        print("男",male_name[male],"号")
    del male_name[0:male_num[x]]
    for female in range(female_num[x]):
        print("女",female_name[female],"号")
    del female_name[0:female_num[x]]

print("分班完成！本对话框三分钟后自动退出，请将屏幕内容全部复制粘贴到word或wps文字处理")
time.sleep(180)