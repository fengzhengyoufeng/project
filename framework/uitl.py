import xlrd
from framework.logger import Logger
logger=Logger("logger=Util").getlogger()
import os
class Util():
    @classmethod
    def read_excel(self,excelPath,sheetName="sheet1"):
        workbook=xlrd.open_workbook(excelPath)
        sheet=workbook.sheet_by_name(sheetName)
        #��ȡkey
        keys=sheet.row_values(0)
        #��ȡ��
        rowName=sheet.nrows
        #��ȡ��
        cloName=sheet.ncols
        #�Ƚ����жϱ���������Ƿ����Ҫ��
        if rowName<=1:
            logger.info("this excel only one type,please add other type")
        else:
            #����һ���ֵ����������ȡ����ֵ��
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