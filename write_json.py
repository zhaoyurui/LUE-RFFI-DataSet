import tarfile
import numpy as np
import os
import json
# 初始化你的JSON结构
json_data = {}
def traverse_directory(path):
    # 遍历指定目录下的所有文件和文件夹
    for scene in os.listdir(path):
        scene_path = os.path.join(path, scene)
        print(f"环境目录: { scene_path}")  #应该是写的发射机的信号吧

        if os.path.isdir(scene_path):
            json_data[scene] = {}
            for recevier in os.listdir(scene_path):
                recevier_path = os.path.join(scene_path, recevier)
                print(f"接收机目录: {recevier_path}")  #
                if os.path.isdir(recevier_path):
                    json_data[scene][recevier] = {}
                    for device in os.listdir(recevier_path):
                        GU_path = os.path.join(recevier_path, device)
                        if os.path.isdir(GU_path):
                            json_data[scene][recevier][device] = {}
                            for files_channel in os.listdir(GU_path):
                                Channel_path = os.path.join(GU_path, files_channel)
                                print(f"通道目录: {Channel_path}")
                                if os.path.isdir(Channel_path):
                                    json_data[scene][recevier][device][files_channel] = {}
                                    for mod in os.listdir(Channel_path):
                                        mod_path = os.path.join(Channel_path, mod)
                                        print(f"调制目录: {mod_path}")
                                        if os.path.isdir(mod_path):
                                            json_data[scene][recevier][device][files_channel][mod] = {}
                                            for bit_rate in os.listdir(mod_path):
                                                bit_path = os.path.join(mod_path, bit_rate)
                                                print(f"码速率目录: {bit_path}")
                                                if os.path.isdir(bit_path):
                                                    json_data[scene][recevier][device][files_channel][mod][bit_rate]={}
                                                    i = 1;
                                                    for num in os.listdir(bit_path):
                                                        if num.endswith('.float32'):
                                                            json_data[scene][recevier][device][files_channel][mod][bit_rate][
                                                                "data{}".format(i)] = []
                                                            parameters = num.split('_')
                                                            num_path = os.path.join(bit_path, num)
                                                            file_info = {
                                                                "sampling rate": parameters[0],
                                                                "gain": parameters[1],
                                                                "number": parameters[3],
                                                                "file_path": num_path,
                                                                "center frequency": '770M',
                                                                "date": parameters[4].split('.')[0],
                                                            }
                                                            json_data[scene][recevier][device][files_channel][mod][bit_rate]["data{}".format(i)].append(file_info)
                                                            i+=1

top_directory = r'.\LUE_Data'
traverse_directory(top_directory)
with open('.\LUE_Data.\LUE_Data.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)


# 加载JSON文件
def load_and_interpret_json(json_file_path):
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

        # 解读并打印JSON数据
    for scene, scene_data in json_data.items():
        print(f"环境: {scene}")
        for receiver, receiver_data in scene_data.items():
            print(f"  接收机: {receiver}")
            for device, device_data in receiver_data.items():
                print(f"    设备: {device}")
                for files_channel, channel_data in device_data.items():
                    print(f"      通道: {files_channel}")
                    for mod, mod_data in channel_data.items():
                        print(f"        调制方式: {mod}")
                        for bit_rate, rate_data in mod_data.items():
                            print(f"          码速率: {bit_rate}")
                            for data_key, file_infos in rate_data.items():
                                print(f"            数据文件: {data_key}")
                                for file_info in file_infos:
                                    print(f"              文件信息:")
                                    for key, value in file_info.items():
                                        print(f"                {key}: {value}")
                                    print()

                                # 指定JSON文件路径


json_file_path = r'.\LUE_Data.\LUE_Data.json'
print("解读")
# 运行解读程序
load_and_interpret_json(json_file_path)