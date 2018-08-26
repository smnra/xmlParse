#  解析xml 时间驱动型



import os
import xml.etree.cElementTree as ET
    
    
def readXml(fileName):
    markTables = []
    markTable = []

    point = {}
    points = []

    for event,elem in ET.iterparse(fileName,events=('start', 'end')):
        #if elem.tag :
        #    print(elem)
        if elem.tag == '{http://earth.google.com/kml/2.2}Placemark':
            # print(elem)
            pass

        # 读取table
        elif elem.tag == '{http://earth.google.com/kml/2.2}table':
            if event=='end':
                markTable.append(r'\n')                         #当table 标签结束时
                markTables.append(markTable)                     #把 markTable 列表 添加到 markTables 列表中
                print(markTable)
                markTable = []                                   # 把 markTable 清空
        elif elem.tag == '{http://earth.google.com/kml/2.2}td':
            if event=='start':
                markTable.append(elem.text)


        # 读取点的信息
        elif elem.tag == '{http://earth.google.com/kml/2.2}name':
            if event == 'start':
                point["name"] = elem.text                                               # 读取point的name
        elif elem.tag == '{http://earth.google.com/kml/2.2}coordinates':
            if event == 'start':
                point["coordinates"] = elem.text                                       # 读取 point 的 coordinates
        elif elem.tag == '{http://earth.google.com/kml/2.2}Point':
            if event == 'end':                                                           # 把point 添加到 points 列表
                points.append(point)
                print(point)
                point = {}                                                                # 清空 point



        elem.clear()

    return points
    
    
readXml(r'./kml.kml')

