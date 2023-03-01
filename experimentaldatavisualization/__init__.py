import os
import json
from collections import defaultdict


def load_directory_tree(dir_path, lvl=0):
    """根据输入的路径及遍历层级加载路径下所有目录树结构

    : param dir_path: 路径
    : type  dir_path: str
    : param lvl: 遍历层级
    : type  lvl: int
    """
    dirTree = defaultdict(dict)
    dirTree['name'] = os.path.basename(dir_path)
    dirTree['children'] = list()

    # 迭代遍历所有路径并构成树结构
    files = [f for f in os.listdir(dir_path)
             if os.path.isdir(os.path.join(dir_path, f)) and lvl>0]

    for file in files:
        if(lvl == 0):
            break
        dirTree2 = defaultdict(dict)
        dirTree2[file] = load_directory_tree(os.path.join(dir_path, file), lvl-1)

        dirTree['children'].append(dirTree2)
    return dirTree

# 测试路径树的结果
#print(json.dumps(pathTreeJson("D:/projects", 3), indent=4))