import tarfile
import numpy as np
import os


def extract_float32_files_from_tar(tar_filepath, extract_dir,rel_dir,para):
    # 确保提取目录存在
    out_path = os.path.join(extract_dir, para[10])
    extract_dir = os.path.join(out_path, rel_dir)
    extract_dir = os.path.join(extract_dir, para[4], para[5])
    if not os.path.exists(extract_dir):
        os.makedirs(extract_dir)

        # 打开tar文件
    with tarfile.open(tar_filepath, 'r') as tar:
            # 遍历tar文件中的所有成员
            for member in tar.getmembers():
                # 检查文件名是否以.float32结尾（不区分大小写）
                if member.name.lower().endswith('.float32'):
                    # 提取文件到指定目录，注意要移除文件名中的路径部分，只保留文件名
                    tar.extract(member, path=extract_dir)
                    original_file_path = os.path.join(extract_dir, member.name)
                    new_filename=para[6]+'_'+para[7]+'_'+para[11].split('.')[0]+'_'+member.name
                    new_file_path = os.path.join(extract_dir, new_filename)
                    # 重命名文件
                    os.rename(original_file_path, new_file_path)
                    # 如果需要，可以重命名提取的文件以去掉路径部分
                    # 但是tarfile.extract()已经处理了路径，所以通常不需要这一步
                    # 如果tar内的路径是多余的，你可能需要手动处理
                    # extracted_file_path = os.path.join(extract_dir, os.path.basename(member.name))
                    # shutil.move(os.path.join(extract_dir, member.name), extracted_file_path)

                # 使用示例


def traverse_directory(path,out_path):
    # 遍历指定目录下的所有文件和文件夹
    for root, dirs, files in os.walk(path):
        # 打印当前遍历的目录路径
        print(f"当前目录: {root}")

        # 打印当前目录下的所有子文件夹
        for dir in dirs:
            dir_path = os.path.join(root, dir)

            print(f"子文件夹: {dir_path}")

            # 打印当前目录下的所有文件
        for file in files:
            parameters = file.split('_')
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(root, path)
            extract_float32_files_from_tar(file_path, out_path,rel_path,parameters)
            print(f"文件: {file_path}")

        # 使用示例


top_directory = r'E:\New data out-temp 26.5-71.7' # 替换为你的顶级目录路径
out_directory = r'E:\LUE_Data\Outdoor'
traverse_directory(top_directory,out_directory)



