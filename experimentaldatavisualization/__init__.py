import os
import json
from collections import defaultdict


def load_directory_tree(dir, lvl=0):
    """根据输入的路径及遍历层级加载路径下所有目录树结构

    : param dir: 路径
    : type  dir: str
    : param lvl: 遍历层级
    : type  lvl: int
    """
    _dir_tree = defaultdict(dict)
    _dir_tree['name'] = os.path.basename(dir)
    _dir_tree['children'] = list()

    # 迭代遍历所有路径并构成树结构
    _files = [f for f in os.listdir(dir)
             if os.path.isdir(os.path.join(dir, f)) and lvl>0]

    for file in _files:
        if(lvl == 0):
            break
        _dir_tree_child = defaultdict(dict)
        _dir_tree_child[file] = load_directory_tree(os.path.join(dir, file), lvl-1)

        _dir_tree['children'].append(_dir_tree_child)
    return _dir_tree

# 测试路径树的结果
#print(json.dumps(pathTreeJson("D:/projects", 3), indent=4))