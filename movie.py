# -*- coding: UTF-8 -*-
import webbrowser

# 定义Movie类


class Movie():

    # 实例初始化函数
    def __init__(self, movie_title, movie_storyline, movie_director,
                 movie_on_show_date, movie_length, movie_rank,
                 poster_image, trailer_youtube):
        # 电影标题
        self.title = movie_title
        # 故事梗概
        self.storyline = movie_storyline
        # 电影导演
        self.director = movie_director
        # 上映时间
        self.on_show_date = movie_on_show_date
        # 电影时长
        self.length_of_time = movie_length
        # 电影评分
        self.rank = movie_rank
        # 电影海报URL
        self.poster_image_url = poster_image
        # 电影预告片URL
        self.trailer_youtube_url = trailer_youtube

    # 电影类的方法，用于打开网页显示预告片
    def show_trailer(self):
        # 调用了webbrowser模块的open函数
        webbrowser.open(self.trailer_youtube_url)
