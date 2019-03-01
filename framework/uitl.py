import xlrd
from framework.logger import Logger
logger=Logger("logger=Util").getlogger()
import os
class Util():
    @classmethod
    def read_excel(self,excelPath,sheetName="sheet1"):
        workbook=xlrd.open_workbook(excelPath)
        sheet=workbook.sheet_by_name(sheetName)
        #获取key
        keys=sheet.row_values(0)
        #获取行
        rowName=sheet.nrows
        #获取列
        cloName=sheet.ncols
        #先进行判断表格中数据是否符合要求
        if rowName<=1:
            logger.info("this excel only one type,please add other type")
        else:
            #定义一个字典用来存放所取到的值：
            r=[]
            for i in range(1,rowName):
                sheet_data={ }
                value=sheet.row_values(i)
                for j in range(cloName):
                    sheet_data[keys[j]]=value[j]
                r.append(sheet_data)
            return r

if __name__=='__main__':
    print(Util.read_excel("lujing"))