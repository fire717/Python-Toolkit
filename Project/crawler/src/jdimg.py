
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
    def __init__(self, keywords):
        self.keywords = keywords
        self.i = 0
        self.page = 0
        self.url = 'https://www.jd.com/'
        self.browser = webdriver.Chrome()
        self.browser_item = webdriver.Chrome()


    # 获取页面信息 - 到具体商品的页面
    def get_html(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys(self.keywords)  # 搜索框输入“爬虫书”
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()  # 点击搜索
        time.sleep(3)  # 给商品页面加载时间


    def closeWrongPage(self):
        # self.browser_item.get("view-source:https://item.jd.com/66659620021.html")
        # current_url = self.browser_item.current_url
        # print(current_url,len(current_url))

        # current_title = self.browser_item.title
        # print(current_title,len(current_title))


        # self.browser_item.get("https://item.jd.com/66659620021.html")
        # current_url = self.browser_item.current_url
        # print(current_url,len(current_url))

        current_title = self.browser_item.title
        print("in closeWrongPage",current_title,len(current_title))


        if len(current_title) ==0:
            #ctrl+w
            win32api.keybd_event(17, 0, 0, 0)
            win32api.keybd_event(87, 0, 0, 0)
            win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(87, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(1)


    #解析商品详情页面
    def parse_html_item_all(self, item_url):
        #不写规则了 遍历所有 但是好像很多img解析出来都是防爬的git
        #队列
        self.browser_item.get(item_url)
        print(item_url)

        find_array = []

        item_p_list = self.browser_item.find_elements_by_xpath('//*[@id="J-detail-content"]/p')
        find_array.extend(item_p_list)
        item_div_list = self.browser_item.find_elements_by_xpath('//*[@id="J-detail-content"]/div')
        find_array.extend(item_div_list)

        idx = 0
        while 1:
            if idx== len(find_array):
                break

            #print("idx: ",idx)

            this_item = find_array[idx]
            items_div = this_item.find_elements_by_xpath('div')
            if len(items_div)>0:
                #print("1111")
                find_array.extend(items_div)

            items_p = this_item.find_elements_by_xpath('p')
            if len(items_p)>0:
                #print("222")
                find_array.extend(items_p)

            items_img = this_item.find_elements_by_xpath('img')
            for item_img in items_img:
                #print("333")
                img_url = item_img.get_attribute('src')
                #print("344",img_url)
                if not img_url:
                    img_url = item_img.get_attribute('href')
                    #print("355",img_url)
                    #b
                if img_url:
                    if img_url[-3:]!="jpg":
                        continue
                    print(img_url)
                    action = ActionChains(self.browser_item).move_to_element(item_img)#移动到该元素
                    action.context_click(item_img)#右键点击该元素

                    action.perform()#执行保存
                    time.sleep(1)

                    win32api.keybd_event(86, 0, 0, 0)
                    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(2)
                    keyEnter()
                    time.sleep(1)

                    #self.closeWrongPage()

            idx+=1



    def parse_html_item(self, item_url):
        #手写规则
        print(item_url)
        self.browser_item.get(item_url)

        p_list = self.browser_item.find_elements_by_xpath('//*[@id="J-detail-content"]/p')
        if len(p_list)==0:
            p_list = self.browser_item.find_elements_by_xpath('//*[@id="J-detail-content"]/div/p')


        print(" -----len(p_list)", len(p_list))
        if len(p_list)==0:
            return


        elif len(p_list)==1:
            div_list = self.browser_item.find_elements_by_xpath('//*[@id="J-detail-content"]/div/div')
            print("---len div_list: ",len(div_list))
            for div in div_list:
                div_list2 = div.find_elements_by_xpath('div')
                print("--len div_list2",len(div_list2))
                for div2 in div_list2:
                    img_node = div2.find_elements_by_xpath('div/img')
                    print("--len img_node",len(img_node))
                    if len(img_node)>0:
                        img_url = img_node[0].get_attribute('src')
                        #print(img_url)

                        if img_url[-3:]!="jpg":
                            continue

                        if img_url:

                            action = ActionChains(self.browser_item).move_to_element(img_node[0])#移动到该元素
                            action.context_click(img_node[0])#右键点击该元素

                            action.perform()#执行保存
                            time.sleep(1)

                            win32api.keybd_event(86, 0, 0, 0)
                            win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)
                            time.sleep(2)
                            keyEnter()
                            time.sleep(1)

                            #self.closeWrongPage()
                            #img_url_true = gettext()


        elif len(p_list)==2 or len(p_list)==3 :
            for p_one in p_list:
                img_list = p_one.find_elements_by_xpath('img')
                if(len(img_list)>1):
                    break

            print("---len img_list: ",len(img_list))
            for img in img_list:

                img_url = img.get_attribute('src')
                print(img_url)

                if img_url[-3:]=="png":
                    continue

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
                    time.sleep(2)
                    keyEnter()
                    time.sleep(1)

                    #self.closeWrongPage()

                    #img_url_true = gettext()



        elif len(p_list)>3:

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
                    time.sleep(2)
                    keyEnter()
                    time.sleep(1)

                    #self.closeWrongPage()

                    #img_url_true = gettext()

                    
        else:
            print("--sp len(p_list): ",len(p_list))


        self.browser_item.quit()
        self.browser_item = webdriver.Chrome()

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

            #item_url = "https://item.jd.com/100004746314.html"
            self.parse_html_item(item_url)
            #b
            

    # 主函数
    def main(self):
        self.get_html()
        #self.page = 0

        # self.closeWrongPage()
        # b

        while True:
            print()
            print("-----------------------page--------------------: ",self.page)
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

    keywords = "商务衬衫"
    spider = JdSpider(keywords)
    spider.main()
