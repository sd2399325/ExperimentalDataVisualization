import os
import json
import re
from collections import defaultdict

def load_dir_tree(path, depth=2, keyword=None):
    """
    遍历指定目录下的子目录，并返回目录结构
    :param path: str 目录路径
    :param depth: int 遍历深度，默认为2
    :param keyword: str 模糊匹配关键词，默认为空
    :return: dict 目录结构
    """
    if not os.path.isdir(path):
        raise ValueError("无效的路径参数: {}并不是一个合法的目录".format(path))
    if depth < 0:
        raise ValueError("无效的遍历深度参数: 深度参数不能为负数")
    if not isinstance(keyword, str):
        raise ValueError("无效的关键词参数: 关键词必须为字符串或者None")

    result = {
        "name": os.path.basename(path),
        "path": os.path.abspath(path),
        "children": []
    }

    if depth == 0:
        return result

    # 遍历子目录 如果不是目录则跳过
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isdir(file_path):
            if keyword is None or re.search(keyword, file_name):
                child = load_dir_tree(file_path, depth=depth-1, keyword=keyword)
                result["children"].append(child)
        else:
            continue

    return result

def rename_dir(path, new_name):
    """
    修改指定目录的名称
    :param path: str 目录路径
    :param new_name: str 新的目录名称
    """
    if not os.path.isdir(path):
        raise ValueError("无效的路径参数: {}并不是一个合法的目录".format(path))
    if not isinstance(new_name, str):
        raise ValueError("无效的名称: 文件夹名称必须为字符串")

    parent_path = os.path.dirname(path)
    new_path = os.path.join(parent_path, new_name)

    if os.path.exists(new_path):
        raise ValueError("无效的名称: {}已经存在该文件夹，请重新命名".format(new_name))

    os.rename(path, new_path)


