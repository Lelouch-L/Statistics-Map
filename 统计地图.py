import pandas as pd
import numpy as np
from pyecharts.charts import Pie ,Grid,Bar,Line
from pyecharts.faker import Faker #数据包
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import csv
for countnum in range(1,2):
    csvFile = open("市级得分.csv", "r")
    reader = csv.reader(csvFile)
    # 建立空字典
    result = {}
    for item in reader:
        # 忽略第一行
        if reader.line_num == 1:
            continue
        result[item[0]] = item[1]

    csvFile.close()
    values = []
    city = []
    for k in result.keys():
        city.append(k)
    for value in result.values():
        # value=float(value)
        values.append(value)
    list1 = [[city[i], values[i]] for i in range(len(city))]  # 首先创建数据
    print(list1)
    map_1 = Map(init_opts=opts.InitOpts(width="600px", height="690px"))  # 创建地图，其中括号内可以调整大小，也可以修改主题颜色。
    map_1.add("湖北省增长动力综合得分", list1, maptype="湖北")  # 添加地图
    map_1.set_global_opts(  # 设置全局配置项
        title_opts=opts.TitleOpts(title="湖北省增长动力综合得分"),
        visualmap_opts=opts.VisualMapOpts(max_=1200, is_piecewise=True),  # 最大数据范围 并且使用分段
        legend_opts=opts.LegendOpts(is_show=False), )  # 是否显示图例)
    map_1.render('%d.html'%countnum)