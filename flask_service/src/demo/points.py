'''
Author: FirbathYu firbath@163.com
Date: 2023-02-15 13:46:38
LastEditors: FirbathYu firbath@163.com
LastEditTime: 2023-02-15 20:48:31
Description: 
'''
# -*- coding:utf-8 -*-
from itertools import product, permutations, combinations


def calculate(cal, a_str, b_str):
    a = int(a_str)
    b = int(b_str)

    if "/" == cal:
        if b == 0 or a % b != 0:
            return None
        else:
            return a/b
    elif "-" == cal:
        if a < b:
            return None
        else:
            return a-b
    elif "+" == cal:
        return a+b
    elif "*" == cal:
        return a*b


def check_step_ignore(step_list, tar):
    for step in step_list:
        if tar == step:
            print("ignore", step, tar)
            return True
    return False


def group_work(item_list_src):

    calculate_list = ("+", "-", "*", "/")
    item_list_rst = list()
    err_list = list()
    igno_list = list()
    step_list = list()

    for item in item_list_src:
        group_list = list(permutations(item["nums"], 2))  # 排列
        for group in group_list:
            tmp = item["nums"].copy()
            for tar in group:
                tmp.remove(tar)

            for cal in calculate_list:
                rst = calculate(cal, *group)
                if rst != None:
                    nums = tmp.copy()
                    nums.append(str(int(rst)))

                    if cal in ("+", "*"):
                        num1 = max(int(group[0]), int(group[1]))
                        num2 = min(int(group[0]), int(group[1]))
                    else:
                        num1 = int(group[0])
                        num2 = int(group[1])

                    step = "{}{}{}{}{}".format(num1, cal, num2, "=", int(rst))
                    if(item.get("step")):
                        step = "{} -> {}".format(item["step"], step)
                    itemNew = {
                        "step": step,
                        "nums": nums,
                    }
                    if step in step_list:
                        igno_list.append(itemNew)
                    else:
                        item_list_rst.append(itemNew)
                        step_list.append(step)
                else:
                    err_list.append(
                        ("err-->{}{}{}".format(group[0], cal, group[1])))

    print("item_list_rst", len(item_list_rst),   "\n")
    print("err_list", len(err_list),   "\n")
    print("igno_list", len(igno_list),   "\n")
    return item_list_rst


def runDemo(nums):

    calculate_list = ("+", "-", "*", "/")
    num_list_0 = nums.split(" ")
    print("num_list_0", len(num_list_0), num_list_0)

    # pro_list = list(product(("+", "-", "*", "/"), repeat=1))  # 积
    # per_list = list(permutations(num_list_0, 4))  # 排列
    # print("per_list 0", per_list, len(per_list))

    item_list_src = list()
    item_list_src.append({
        "step": "",
        "nums": nums.split(" "),
    })

    # 第1轮计算
    print("第1轮计算")
    item_list_1 = group_work(item_list_src)
    # 第2轮计算
    print("第2轮计算")
    item_list_2 = group_work(item_list_1)
    # 第3轮计算
    print("第3轮计算")
    item_list_3 = group_work(item_list_2)

    count = 0
    for item in item_list_3:
        if int(item["nums"][0]) == 24:
            print(item)
            count += 1

    print(count)


if __name__ == "__main__":
    runDemo("1 2 3 4")
