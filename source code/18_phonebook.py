
people = {
    "EMMA": "617-555-0100", #一对键值对
    "RODRIGO": "617-555-0101",
    "BRIAN": "617-555-0102",
    "DAVID": "617-555-0103",
}
if "EMMA" in people:  #不用循环遍历链表
    # 对字典直接进行EMMA的索引，不用对数字1，2，3进行索引
    print(f"found {people['EMMA']}")
