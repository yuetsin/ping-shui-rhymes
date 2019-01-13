# -*- coding: utf-8 -*-

from rhyme_init import get_sheet

ping_shui_rhymes = get_sheet()

print("----------------")

rawString = input("输入字，或输入 end 结束：\n        ")

while rawString != "end":
    if len(rawString) == 1:
        print("平仄是：")
        for i in ping_shui_rhymes:
            if i.chineseChar == rawString:
                print(i.getDescript())
                if not i.isPolyphone:
                    break
        print("\n----------------")
    else:
        print("平仄是：", end='')
        polyList = []
        for j in rawString:
            fixedObj = False
            for i in ping_shui_rhymes:
                if i.chineseChar == j:
                    if i.isPolyphone:
                        print("多", end='')
                        if not i in polyList:
                            polyList.append(i)
                        fixedObj = False
                        break
                    elif i.isPing():
                        print("平", end='')
                        fixedObj = False
                        break
                    else:
                        print("仄", end='')
                        fixedObj = False
                        break
                fixedObj = not fixedObj
            if fixedObj:
                print("〇", end='')
                fixedObj = not fixedObj
        if polyList != []:
            print("\n下面是多音字：\n----------------")
            for j in polyList:
                for i in ping_shui_rhymes:
                    if i.chineseChar == j.chineseChar:
                        print(i.getDescript())
                print("----------------")
        else:
            print("\n----------------")
    rawString = input("输入字，或输入 end 结束：\n        ")
