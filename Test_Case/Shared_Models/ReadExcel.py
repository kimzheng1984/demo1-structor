#coding=utf-8
import xlrd 

def readexcel(fname,sheet):
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name(sheet)#打开sheet
    except:
        print("no sheet in %s named Sheet1")% fname
    nrows = sh.nrows#获取行数    
    ncols = sh.ncols#获取列数
    #读取excel中除首行外所有内容
    datalist=[]
    for j in range(0,ncols):
        for i in range(1,nrows):
            cell_single=sh.cell_value(i,j)
            datalist.append(cell_single)
    return datalist

#参数说明：文件名、sheet名、获取整行中row_data[]的下标
def readcolumn(fname, sheet, columnindex):
    #打开excel
    bk = xlrd.open_workbook(fname)
    try:
        #通过名称打开sheet
        sh = bk.sheet_by_name(sheet)  # 打开sheet
    except IOError:
        print("no sheet in %s named Sheet1") % fname
    #获取整行的数据
    row_data = sh.row_values(1)
    #返回整行数据，调用时通过下标获取具体列
    return row_data[columnindex]






