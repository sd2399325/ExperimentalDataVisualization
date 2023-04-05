import os
import json
import fnmatch
from collections import defaultdict


def load_directory_tree(root_dir, lvl=0):
    """根据输入的路径及遍历层级加载路径下所有子目录及文件，并加载成树形数据结构


    : param root_dir: 路径
    : param lvl: 遍历层级
    : return: 路径树结构
    """

    dir_tree = defaultdict(dict)
    dir_tree['name'] = os.path.basename(root_dir)
    dir_tree['dir'] = root_dir
    dir_tree['children'] = list()

    # 迭代遍历路径下第一层文件夹并构成树结构
    files = [f for f in os.listdir(root_dir)
             if os.path.isdir(os.path.join(root_dir, f)) and lvl>0]

    # 遍历第一层文件内包含的文件夹,具体层数根据传入的遍历层数确定
    for file in files:
        if(lvl == 0):
            break
        dir_tree_child = defaultdict(dict)
        dir_tree_child[file] = load_directory_tree(os.path.join(root_dir, file), lvl-1)

        dir_tree['children'].append(dir_tree_child)
    return dir_tree

def filter_directory_tree(dir_tree, key_word):
    """根据关键词对目录树进行筛选并重新构建目录树

    : param dir_tree: 目录树
    : param key_word: 关键词
    : return: 筛选后的目录树
    """
    # 递归遍历目录树
    for key, value in dir_tree.items():
        if key == 'name':
            if key_word in value:
                return dir_tree
        elif key == 'children':
            for child in value:
                for k, v in child.items():
                    res = filter_directory_tree(v, key_word)
                    if res:
                        return res
        else:
            continue
    return None


print(json.dumps(load_directory_tree("D:/projects", 2), indent=4))


