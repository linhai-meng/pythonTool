import  os
import re


'''
author:menglinhai
time: 2018/8/27
function : operate folder
'''
def find_file(path,flag_chang=False):
    '''
    根据输入查找只定目录的文件
    :return:
    '''


    file = input("请输入需要查找的文件：")
    files = os.listdir(path)
    f_result = []
    for f in files:
        if re.search(file,f):
            f_result.append(f)
    print("找到的文件为%s"%(str(f_result)))
    if flag_chang == False:
        flag = input("继续操作本文件夹吗？y/n")
        if flag == "n":
            is_changefolder = input("需要换文件夹吗？y/n")
            if is_changefolder == "y" or is_changefolder == "Y":
                start()
            else:
                return
        elif flag == "y":
            operation(path)
    return (path,f_result)



def save_file(path):
    """
    根据输入目录得到目录下的文件名 文件类型 并保存到files.txt中
    :return:
    """

    files = os.listdir(path)
    result = []
    for f in files:
        type_file = path.split(".")[-1]
        print(f)
        f = f.ljust(50," ")
        type_file = type_file.ljust(10," ")
        result.append((f,type_file))
    with open("files.txt","w") as f:
        for fi in result:

            f.writelines(fi[0]+fi[1])
            f.write("\n")
    flag = input("继续操作本文件夹吗？y/n")
    if flag == "n":
        is_changefolder = input("需要换文件夹吗？y/n")
        if is_changefolder == "y" or is_changefolder == "Y":
            start()
        else:
            return
    elif flag == "y":
        operation(path)

def chang_file_name(path):
    """
    根据查找到的用户名进行替换用户名操作
    :return:
    """
    path ,file = find_file(path,True)
    new_file_name = input("请输入新的文件名：")
    src_file = os.path.join(path,file[0])
    dst_file = os.path.join(path,new_file_name)
    os.rename(src_file,dst_file)
    print("文件更改完成")
    flag = input("继续操作本文件夹吗？y/n")
    if flag == "n":
        is_changefolder = input("需要换文件夹吗？y/n")
        if is_changefolder == "y" or is_changefolder == "Y":
            start()
        else:
            return
    elif flag == "y":
        operation(path)
def input_folder():
    while True:
        path = input("请输入目录：")
        path = re.sub(r'\\', r'/', path)
        if os.path.isdir(path):
            break
        else:
            print("请重新输入：")
    return path
def operation(path):
    flag = input("请输入要进行的操作\n F 表示查找\n S:将只定目录保存到files.txt\n C:表示将查找出的文件进行替换，只能替换第一个文件: \nq:退出")
    if flag.strip() =="F":
        find_file(path)
    elif flag.strip() == "S":
        save_file(path)
    elif flag.strip() == "C":
        chang_file_name(path)

def start():
    path= input_folder()
    operation(path)

if __name__ == '__main__':
    start()