"""
用于将b站下载的视频（以m4s格式保存，视频和音频分开存储）转换为mp4文件并保存在统一目录下
"""

r'''
ffmpeg -i .\video.m4s -i .\audio.m4s -vcodec copy -acodec copy output.mp4
'''

import os

sourcePath = r"L:\手机备份\bilibili下载"   #下载视频文件的地址
outputPath = r"L:\手机备份\VideoOutput"    #保存输出的mp4文件的地址
i = 0

for root,dirs,files in os.walk(sourcePath):     #遍历下载目录
    for file in files:
        #获取文件所属目录
        #print(root)
        #获取文件路径
        #print(file)
        if file == "video.m4s":
            filename = "output{}.mp4".format(i)
            cmd = r"ffmpeg -i .\video.m4s -i .\audio.m4s -vcodec copy -acodec copy {}".format(os.path.join(outputPath,filename))    #调用ffmpeg合成视频
            i += 1
            os.chdir(root)
            print(cmd)
            os.system(cmd)