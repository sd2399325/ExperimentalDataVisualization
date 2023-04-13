import os
import json

import experimentaldatavisualization.__init__ as edv

def test_load_directory():
    # 创建测试目录和文件
    test_dir_path = os.path.join(".", "test_dir")
    os.mkdir(test_dir_path)

    sub_dir_path = os.path.join(test_dir_path, "sub_dir")
    os.mkdir(sub_dir_path)

    file_path = os.path.join(sub_dir_path, "test_file.txt")
    with open(file_path, "w") as f:
        f.write("test")

    # 测试遍历目录
    expected_result = {
        "name": "test_dir",
        "path": test_dir_path,
        "subdirectories": [
            {
                "name": "sub_dir",
                "path": sub_dir_path,
                "subdirectories": [
                    {
                        "name": "test_file.txt",
                        "path": file_path,
                        "subdirectories": []
                    }
                ]
            }
        ]
    }
    result = edv.load_dir_tree(test_dir_path)
    assert json.dumps(result, sort_keys=True) == json.dumps(expected_result, sort_keys=True)

    # 清理测试目录和文件
    os.remove(file_path)
    os.rmdir(sub_dir_path)
    os.rmdir(test_dir_path)


def test_rename_directory():
    # 创建测试目录
    test_dir_path = os.path.join(".", "test_dir")
    os.mkdir(test_dir_path)

    # 测试修改目录名称
    edv.rename_dir(test_dir_path, "new_test_dir")
    assert os.path.exists(os.path.join(".", "new_test_dir"))

    # 清理测试目录
    os.rmdir(os.path.join(".", "new_test_dir"))