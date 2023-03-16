import os
from collections import defaultdict


def load_directory_tree(root_dir, lvl=0):
    """根据输入的路径及遍历层级加载路径下所有子目录及文件，并加载成树形数据结构


    : param dir: 路径
    : param lvl: 遍历层级
    : return: 路径树结构
    """
    dir_tree = defaultdict(dict)
    dir_tree['name'] = os.path.basename(root_dir)
    dir_tree['children'] = list()

    # 迭代遍历路径下第一层文件夹并构成树结构
    files = [f for f in os.listdir(root_dir)
             if os.path.isdir(os.path.join(root_dir, f)) and lvl>0]

    # 遍历第一层文件内包含的文件夹,具体层数根据传入的遍历层数确定
    for file in files:
        dir_tree_child = defaultdict(dict)
        dir_tree_child['name'] = file
        dir_tree_child['children'] = load_directory_tree(os.path.join(root_dir, file), lvl-1)
        dir_tree['children'].append(dir_tree_child)

    return dir_tree

