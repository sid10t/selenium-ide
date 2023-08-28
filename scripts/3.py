import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('-ignore -ssl-errors')
chrome_options.add_argument('--ignore-certificate-errors')


class Test():
    def start(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.vars = {}

    def end(self):
        self.driver.quit()

    def roll(self):
        # 模拟滚动置底
        temp_height = 0
        while True:
            # 循环将滚动条下拉
            self.driver.execute_script("window.scrollBy(0, 4000)")
            # sleep一下让滚动条反应一下
            time.sleep(1)
            # 获取当前滚动条距离顶部的距离
            check_height = self.driver.execute_script(
                "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
            # 如果两者相等说明到底了
            if check_height == temp_height:
                break
            temp_height = check_height

    def test_(self):
        self.driver.get("https://cloud.tencent.com/developer/tag/17908")
        self.driver.set_window_size(1532, 856)
        # self.driver.execute_script("window.scrollTo(0,12000)")
        self.roll()
        self.vars["array"] = []
        self.vars["sections"] = self.driver.find_elements(
            By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/div/div[2]/com/div[1]/section")
        print(len(self.vars["sections"]))

        try:
            for section in self.vars["sections"]:
                # 作者
                author = section.find_element(
                    By.XPATH, "./div[2]/div/div[1]/div/div/a").text
                # 题目
                title = section.find_element(By.XPATH, "./div[1]/h3").text
                # 点赞数量
                nums = section.find_element(
                    By.XPATH, "./div[2]/div/div[2]/span[2]").text
                self.vars["array"].append((author, title, nums))
            # break
        except:
            pass
  
        lst = sorted(self.vars["array"], key=lambda x: int(x[-1]), reverse=True)[:6]
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
        for it in lst:
            print(it)
