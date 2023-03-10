import os
import json
from collections import defaultdict


def load_directory_tree(dir, lvl=0):
    """根据输入的路径及遍历层级加载路径下所有目录树结构

    : param dir: 路径
    : param lvl: 遍历层级
    : return: 路径树结构
    """
    dir_tree = defaultdict(dict)
    dir_tree['name'] = os.path.basename(dir)
    dir_tree['children'] = list()

    # 迭代遍历路径下第一层文件夹并构成树结构
    files = [f for f in os.listdir(dir)
             if os.path.isdir(os.path.join(dir, f)) and lvl>0]

    # 遍历第一层文件内包含的文件夹,具体层数根据传入的遍历层数确定
    for file in files:
        if(lvl == 0):
            break
        dir_tree_child = defaultdict(dict)
        dir_tree_child[file] = load_directory_tree(os.path.join(dir, file), lvl-1)

        dir_tree['children'].append(dir_tree_child)
    return dir_tree

