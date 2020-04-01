
#配置参考https://www.cnblogs.com/LXP-Never/p/11386933.html#京东爬虫案例
#主要就是下一个和chrome版本一样的核

from selenium import webdriver
import time


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import win32clipboard as w
import win32con

import win32api


VK_CODE ={'enter':0x0D, 'down_arrow':0x28}
#键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
#键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)


def keyEnter():
    keyDown('enter')
    keyUp('enter')


def gettext():
    w.OpenClipboard()
    t = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return t

class JdSpider(object):
    def __init__(self):
        self.i = 0
        self.page = 0
        self.url = 'https://www.jd.com/'
        self.browser = webdriver.Chrome()
        self.browser_item = webdriver.Chrome()

    # 获取页面信息 - 到具体商品的页面
    def get_html(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('polo衫')  # 搜索框输入“爬虫书”
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()  # 点击搜索
        time.sleep(3)  # 给商品页面加载时间



    #解析商品详情页面
    def parse_html_item(self, item_url):
        print(item_url)
        self.browser_item.get(item_url)

        p_list = self.browser_item.find_elements_by_xpath('//*[@id="J-detail-content"]/p')
        if len(p_list)==0:
            p_list = self.browser_item.find_elements_by_xpath('//*[@id="J-detail-content"]/div/p')


        print(" -----len(p_list)", len(p_list))
        if len(p_list)==0:
            return

        elif len(p_list)==2:
            img_list = p_list[0].find_elements_by_xpath('img')
            print("---len img_list: ",len(img_list))
            for img in img_list:

                img_url = img.get_attribute('src')
                print(img_url)

                if img_url:

                    action = ActionChains(self.browser_item).move_to_element(img)#移动到该元素
                    action.context_click(img)#右键点击该元素
                    # action.send_keys(Keys.ARROW_DOWN)#点击键盘向下箭头
                    # action.send_keys(Keys.ARROW_DOWN)
                    # action.send_keys(Keys.ARROW_DOWN)
                    # action.send_keys(Keys.ARROW_DOWN)
                    # action.send_keys(Keys.ENTER)
                    action.perform()#执行保存
                    time.sleep(1)

                    win32api.keybd_event(86, 0, 0, 0)
                    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(1)
                    keyEnter()
                    time.sleep(1)

                    img_url_true = gettext()

                    
                #img_url = img.get_attribute('src')
                #print(img_url)

            print("Done one ------------------------------")
            time.sleep(1)

        elif len(p_list)>2:

            for p_img in p_list:
                img_list = p_img.find_elements_by_xpath('img')
                if(len(img_list))==0:
                    continue
                img_url = img_list[0].get_attribute('src')
                if img_url:
                    print(img_url)

                    action = ActionChains(self.browser_item).move_to_element(img_list[0])#移动到该元素
                    action.context_click(img_list[0])#右键点击该元素
                    action.perform()#执行保存
                    time.sleep(1)

                    win32api.keybd_event(86, 0, 0, 0)
                    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(1)
                    keyEnter()
                    time.sleep(1)

                    img_url_true = gettext()

                    
        else:
            print("--sp len(p_list): ",len(p_list))

    # 解析目录页面
    def parse_html(self):
        # 把下拉菜单拉到底部,执行JS脚本
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        # 提取所有商品节点对象列表 li列表
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        print("---len li_list: ", len(li_list))

        for li in li_list:

            div_list = li.find_elements_by_xpath('div/div')
            link = div_list[0].find_elements_by_xpath('a')

            item_url = link[0].get_attribute('href')

            self.parse_html_item(item_url)

            

    # 主函数
    def main(self):
        self.get_html()
        #self.page = 0
        while True:
            print("-----------------------page----------: ",self.page)
            self.parse_html()
            # 判断是否该点击下一页,没有找到说明不是最后一页
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(3)

            else:
                break
            self.page+=1
        #print(self.i)


if __name__ == '__main__':
    spider = JdSpider()
    spider.main()
