'''
Author: FirbathYu firbath@163.com
Date: 2023-02-15 13:46:38
LastEditors: FirbathYu firbath@163.com
LastEditTime: 2023-02-16 12:34:21
Description: 
'''
# -*- coding:utf-8 -*-
from itertools import product, permutations, combinations
from datetime import datetime
import json


def calculate(cal, a, b):
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
        group_list = list(combinations(item["nums"], 2))  # 组合
        for group in group_list:

            remainder = item["nums"].copy()
            for tar in group:
                remainder.remove(tar)

            # 使用组合模式，保持大数在前可以减少大量运算
            num0 = max(int(group[0]), int(group[1]))
            num1 = min(int(group[0]), int(group[1]))
            for cal in calculate_list:
                rst = calculate(cal, num0, num1)
                if rst != None:
                    nums = remainder.copy()
                    nums.append(str(int(rst)))

                    # x*1和x/1按重复步骤特殊处理(可选)
                    if num1 == 1 and cal == "/":
                        cal = "*"
                    step = "{}{}{}{}{}".format(num0, cal, num1, "=", int(rst))
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

    # print("item_list_rst", len(item_list_rst), "\n")
    # print("err_list", len(err_list), "\n")
    # print("igno_list", len(igno_list), "\n")
    return item_list_rst


def playGame(item_list_src):
    # print("item_list_src", len(item_list_src), item_list_src)

    item_list_0 = list()
    item_list_0.append({
        "step": "",
        "nums": item_list_src,
    })

    # print("第1轮计算") # 第1轮计算
    item_list_1 = group_work(item_list_0)

    # print("第2轮计算") # 第2轮计算
    item_list_2 = group_work(item_list_1)

    # print("第3轮计算") # 第3轮计算
    item_list_3 = group_work(item_list_2)

    rst_list = list()
    for item in item_list_3:
        if int(item["nums"][0]) == 24:
            print(item)
            rst_list.append(item)

    # print(count)
    return rst_list


def test_itertools(num_list_src, count=2):

    print("num_list_src", len(num_list_src), num_list_src)
    pro_list = list(product(num_list_src, repeat=count))  # 积
    per_list = list(permutations(num_list_src, count))  # 排列
    com_list = list(combinations(num_list_src, count))  # 组合
    print("pro_list ", len(pro_list), pro_list)
    print("per_list ", len(per_list), per_list)
    print("com_list ", len(com_list), com_list)


def runDemo():
    num_list_src = "9 11 12 13".split(" ")
    # test_itertools("1 2 3 4", 2)
    playGame(num_list_src)

    # start = datetime.now()

    # card_list = list(range(1, 14))*4
    # com_list = list(combinations(card_list, 4))  # 组合

    # zero_list = list()

    # for index, sample in enumerate(com_list):
    #     rst = playGame(list(sample))
    #     print("{}/{}".format(index, len(com_list)), sample, rst)
    #     if rst == 0:
    #         zero_list.append(sample)
    # print("card_list ", len(card_list), card_list)
    # print("com_list ", len(com_list))
    # print("zero_list ", len(zero_list))

    # end1 = datetime.now()
    # print("time spend ", (end1 - start).total_seconds())
    # f = open("zero_list.json", 'w', encoding='utf-8')
    # f.write(json.dumps(zero_list))
    # f.close()
    # print("time spend ", (datetime.now() - end1).total_seconds())


if __name__ == "__main__":
    runDemo()
