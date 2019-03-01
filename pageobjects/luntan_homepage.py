from selenium.webdriver.common.by import By
from framework.base import BasePage
import time
class LuntanHomePage(BasePage):
    #登录元素
    luntan_home_page_input_name_search_loc=(By.NAME,"username")#账号
    luntan_home_page_input_pwd_search_loc = (By.NAME, "password")#密码
    luntan_home_page_button1_search_loc = (By.CSS_SELECTOR, "button em")#登录按钮
    #默认板块发帖元素
    luntan_home_page_a_mrbk_search_loc=(By.CSS_SELECTOR,".fl_icn a img")#默认板块
    luntan_home_page_input_tzsr_t_search_loc = (By.CSS_SELECTOR, ".pbt input")#帖子输入
    luntan_home_page_a_pssage_search_loc = (By.CSS_SELECTOR, ".area textarea")#正文
    luntan_home_page_button2_search_loc=(By.CSS_SELECTOR,".ptm button")#发表按钮
    #默认板块回帖元素
    luntan_home_page_input_text_mrbk_search_loc=(By.CSS_SELECTOR,".area textarea")#回帖文本框
    luntan_home_page_button3_search_loc=(By.CSS_SELECTOR,".ptm button")#发表回复
    #退出登录
    luntan_home_page_button4_search_loc=(By.LINK_TEXT,"退出")#退出登录
    #进入默认板块，删除帖子
    luntan_home_page_button5_search_loc=(By.CSS_SELECTOR,"tbody:nth-last-child(2) tr td:nth-child(2) input")
    luntan_home_page_button6_search_loc=(By.CSS_SELECTOR,"body div form p strong:nth-child(1) a")
    luntan_home_page_button7_search_loc=(By.ID,"modsubmit")
    #进入版块管理(管理中心--论坛)
    luntan_home_page_a_glzx_search_loc=(By.PARTIAL_LINK_TEXT,"管理中心")
    luntan_home_page_a_luntanmrbk_search_loc=(By.CSS_SELECTOR,".nav li:nth-last-child(8)")
    #添加新板块
    luntan_home_page_iframe_search_loc=(By.CSS_SELECTOR,"td iframe")
    luntan_home_page_a_addnew_search_loc=(By.CSS_SELECTOR,".lastboard .addtr")
    luntan_home_page_input_addNew_search_loc = (By.NAME, "newforum[1][]")
    luntan_home_page_input_tijiao_search_loc=(By.CSS_SELECTOR,".fixsel input")
    luntan_home_page_button14_search_loc = (By.CSS_SELECTOR, ".uinfo p:first-of-type a")  # 退出登录按钮

    #新用户发帖：
    luntan_home_page_a_xjbk_search_loc = (By.CSS_SELECTOR, ".fl_row a img")  # 新建板块
    #进行帖子搜索    # 搜索haotest帖子
    luntan_home_page_input_sousuo_search_loc=(By.CSS_SELECTOR,".scbar_txt_td input")#搜索框
    luntan_home_page_button11_search_loc=(By.NAME,"searchsubmit")#进入搜索页面
    luntan_home_page_button12_search_loc=(By.CLASS_NAME,"schbtn")#点击搜索按钮
    luntan_home_page_a_into_search_loc=(By.CSS_SELECTOR,".xs3 a")# 点击进入搜索的帖子
    luntan_home_page_span_tit_search_loc = (By.ID, "thread_subject")
    # 验证帖子标题和期望的一致
    # 用户退出

    #发起投票新帖
    luntan_home_page_button8_search_loc=(By.CSS_SELECTOR,".bw0 a img")
    luntan_home_page_button9_search_loc = (By.CSS_SELECTOR, ".mbw li:nth-last-child(1) a")
    luntan_home_page_a_toupiao1_search_loc=(By.XPATH,'//*[@id="pollm_c_1"]/p[1]/input')
    luntan_home_page_a_toupiao2_search_loc = (By.XPATH, "//*[@id='pollm_c_1']/p[2]/input")
    luntan_home_page_button10_search_loc = (By.NAME, "topicsubmit")  # 发起投票按钮
    luntan_home_page_button13_search_loc=(By.CSS_SELECTOR, ".pr")
    luntan_home_page_input_toupiao_search_loc=(By.NAME, "pollsubmit")

    #取出投票各个选项的名称以及投票比例 //label[@for="option_1"]
    luntan_home_page_label1_search_loc=(By.XPATH,'//label[@for="option_1"]')#选项1
    luntan_home_page_label2_search_loc=(By.XPATH,'//label[@for="option_2"]')#选项2
    luntan_home_page_bili1_search_loc=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[2]/td[2]')#比例1
    luntan_home_page_bili2_search_loc=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[4]/td[2]')

    #取出投票的主题名称
    luntan_home_page_span_timu_search_loc=(By.CSS_SELECTOR,"h1 span")


    def login_search(self,name,pwd):  # 登录
        self.sendkeys(name, *self.luntan_home_page_input_name_search_loc)
        self.sendkeys(pwd, *self.luntan_home_page_input_pwd_search_loc)
        self.click(*self.luntan_home_page_button1_search_loc)

    def fatie_search(self,tittle,text_fatie): # 默认板块发帖
        self.click(*self.luntan_home_page_a_mrbk_search_loc)
        self.sendkeys(tittle, *self.luntan_home_page_input_tzsr_t_search_loc)
        self.sendkeys(text_fatie, *self.luntan_home_page_a_pssage_search_loc)
        self.click(*self.luntan_home_page_button2_search_loc)

    def huitie_search(self, text_huitie):    # 默认板块回帖
        self.sendkeys(text_huitie, *self.luntan_home_page_input_text_mrbk_search_loc)
        self.click(*self.luntan_home_page_button3_search_loc)

    def logout_search(self):    # 退出登录
        self.click(*self.luntan_home_page_button4_search_loc)

    def delete_tiezi(self):    #进入默认板块，删除帖子
        self.click(*self.luntan_home_page_a_mrbk_search_loc)
        time.sleep(3)
        self.click(*self.luntan_home_page_button5_search_loc)
        time.sleep(3)
        self.click(*self.luntan_home_page_button6_search_loc)
        time.sleep(3)
        self.click(*self.luntan_home_page_button7_search_loc)

    def into_guanlizhongxin(self):#进入管理中心
        self.click(*self.luntan_home_page_a_glzx_search_loc)
        self.switch_windows(1)
        self.click(*self.luntan_home_page_a_luntanmrbk_search_loc)
        time.sleep(5)

    def add_bankuai_search(self,test):#新建板块
        self.iframe(*self.luntan_home_page_iframe_search_loc)
        self.click(*self.luntan_home_page_a_addnew_search_loc)
        self.sendkeys(test,*self.luntan_home_page_input_addNew_search_loc)
        self.click(*self.luntan_home_page_input_tijiao_search_loc)
        self.switch_windows(1)
        self.click(*self.luntan_home_page_button14_search_loc)

    def people_fatie(self,tittle,text_fatie):
        self.click(*self.luntan_home_page_a_xjbk_search_loc)
        self.sendkeys(tittle, *self.luntan_home_page_input_tzsr_t_search_loc)
        self.sendkeys(text_fatie, *self.luntan_home_page_a_pssage_search_loc)
        self.click(*self.luntan_home_page_button2_search_loc)
        time.sleep(5)

    def toupiao_search(self,tit,xuan1,xuan2):#发表投票帖子
        self.click(*self.luntan_home_page_a_mrbk_search_loc)
        self.click(*self.luntan_home_page_button8_search_loc)
        self.click(*self.luntan_home_page_button9_search_loc)#发起投票按钮
        time.sleep(2)
        self.sendkeys(tit, *self.luntan_home_page_input_tzsr_t_search_loc)
        self.sendkeys(xuan1,*self.luntan_home_page_a_toupiao1_search_loc)
        self.sendkeys(xuan2,*self.luntan_home_page_a_toupiao2_search_loc)
        self.click(*self.luntan_home_page_button10_search_loc)
        self.click(*self.luntan_home_page_button13_search_loc)
        self.click(*self.luntan_home_page_input_toupiao_search_loc)

    def toupiao_bili_search(self):
        label1=self.getText(*self.luntan_home_page_label1_search_loc)
        label2 = self.getText(*self.luntan_home_page_label2_search_loc)
        bili1=self.getText(*self.luntan_home_page_bili1_search_loc)
        bili2 = self.getText(*self.luntan_home_page_bili2_search_loc)
        print("选项",label1,"所占比例：",bili1)
        print("选项", label2, "所占比例：", bili2)

    def get_piao_tittle_search(self):    #取出投票的主题名称
        piao_tittle=self.getText(*self.luntan_home_page_span_timu_search_loc)
        print("投票的题目是：",piao_tittle)

    def select_tiezi_search(self,text):
        self.sendkeys(text,*self.luntan_home_page_input_sousuo_search_loc)
        self.click(*self.luntan_home_page_button11_search_loc)
        self.switch_windows(1)
        self.click(*self.luntan_home_page_button12_search_loc)
        self.click(*self.luntan_home_page_a_into_search_loc)
        self.switch_windows(2)
        title=self.getText(*self.luntan_home_page_span_tit_search_loc)
        if title=="haotest":
            print("帖子标题与期望的一致")


