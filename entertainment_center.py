# -*- coding: UTF-8 -*-
# Import Python Libraries or Module
import os
# Import fresh_tomatoes Module
import fresh_tomatoes
# Import the Movie Class writen by myself
import movie

# 通过listdir函数获取"."当前路径下的所有文件，并将结果保存在all_files列表
all_files = os.listdir(".")

# 通过path.splitext()函数获取每个文件的后缀名，并将符合条件的文件保存到
# movie_infomation_files列表中。“*.mvi”后缀名的含义为movie_infomation。
movie_infomation_files = []
for file in all_files:
    if os.path.splitext(file)[1] == ".mvi":
        movie_infomation_files.append(file)

# 创建movie列表用语储存Movie实例
movie_list = []
# 创建movie信息模板列表，用语储存从“*.mvi”文件中读取的Movie信息（此处也可直接用空列表）
# 创建一个模板更便于核对“*.mvi”文件应该包含的信息行数
movie_info = ["movie_title", "movie_storyline", "movie_director",
              "movie_on_show_date", "movie_length", "movie_rank",
              "poster_image", "trailer_youtube"]
for movie_infomation_file in movie_infomation_files:
    # 通过open内置命令逐个读取“*.mvi”文件（"r"表示以只读方式打开文件），使用temp临时储存
    temp = open(movie_infomation_file, "r")
    # 通过字符串的splitlines()函数将读取的全部文本内容按行划分成列表
    movie_info = temp.read().splitlines()
    """在解决readline()后多一个换行符时查找到的方法，直接替换旧的分行（readline）读取方式：
       for i in range(8):
           movie_info[i] = temp.readline()"""
    temp.close
    # 检测两个重要数据：movie_info[6]对应电影海报，movie_info[7]对应电影预告片，
    # 如果不为空，则使用这组电影信息创建新的Movie实例，并存入movie_list
    if movie_info[6] != "" and movie_info[7] != "":
        movie_list.append(movie.Movie(movie_info[0], movie_info[1],
                                      movie_info[2], movie_info[3],
                                      movie_info[4], movie_info[5],
                                      movie_info[6], movie_info[7]))

# 使用fresh_tomatoes提供的函数生成静态页面
fresh_tomatoes.open_movies_page(movie_list)
