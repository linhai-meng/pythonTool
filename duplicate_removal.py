
# 删除相同的文件，包括各个文件夹里面各个相同的文件


import os

def get_all_files(path,arr):
    '''
    得到一个目录下面所有的文件，并返回列表
    :param path: 路径，读取文件的路径
    :param arr: 列表，加载绝对目录的文件
    :return: 返回目录的集合
    '''
    files = os.listdir(path)
    for file in files:
        # print(file)
        path_file= os.path.join(path,file)
        if os.path.isdir(path_file):
            arr = get_all_files(path_file,arr)
        else:
            arr.append(path_file)
    return  arr

def remove_duplicate(path_files):
    '''
    利用输入的绝对路径的文件，利用哈希的方式进行去重。
    :param path_files: 绝对值路径文件
    :return: True
    '''
    remove_duplicate_map = {}
    remove_list = []
    for file in path_files:
        with open(file,'rb') as f:
            f_hash =hash(f.read())
            print(f_hash)
            if f_hash in remove_duplicate_map:
                # os.remove(file)
                remove_list.append(file)
            else:
                remove_duplicate_map[f_hash] = file
    for remove_file in remove_list:
        os.remove(remove_file)
    return True

if __name__ == '__main__':
    path  = "请输入需要去除重复图片的目录"
    if path == "":
        path = "./problem_files"
    files_list=[]
    files = get_all_files(path,files_list)
    flag = remove_duplicate(files)
    if flag:
        print("去重完毕，谢谢")


