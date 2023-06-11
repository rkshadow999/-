import pyautogui
from PIL import Image
import cv2
import time
import numpy as np

class daotianlu():
    def __init__(self) -> None:
        self.x = 734 #小程序左上角坐标x轴  1187   734
        self.y = 98  #小程序左上角y轴       97    98
        self.w = 449 #小程序宽度(通过 左上角x轴-右上角x轴 得出结果)
        self.h = 841 #小程序高度(通过 左上角y轴-左下角y轴 得出结果)
        self.fanhuizuobiao = 1138,897 #返回按钮的坐标(当需要手动时)1586  1138
        self.dibuzuobiao = 962,912 #空白处底部坐标(当需要手动时)1404  962
        self.tupozuobiao= 960,599 #突破坐标(当需要手动时)1409  960
        
        self.dizi = cv2.imread('images/dizi.png') #主页弟子图片
        self.peiyang = cv2.imread('images/peiyang.png') #进入弟子培养图片
        self.xiuxing = cv2.imread('images/xiuxing.png') #进入培养找到修行按钮
        self.xiuxingtupo = cv2.imread('images/xiuxingtupo.png') #修行突破标识
        self.next = cv2.imread('images/next.png') #下一个人物
        self.pojing = cv2.imread('images/pojing.png') #破镜按钮
        self.tupo = cv2.imread('images/tupo.png') #突破按钮
        self.querentupo = cv2.imread('images/querentupo.png') #确认突破
        self.queren = cv2.imread('images/queren.png') #成功率不足时出现确认
        self.tiaoguo = cv2.imread('images/tiaoguo.png') #跳过突破
        self.renwu = cv2.imread('images/renwu.png') #主页任务图片
        self.fanhui = cv2.imread('images/fanhui.png') #主页任务图片
        self.liandanrenwu = cv2.imread('images/liandanrenwu.png') #任务中的炼丹任务
        self.zhibiao = cv2.imread('images/zhibiao.png') #任务指标
        self.liandankefenpei = cv2.imread('images/liandankefenpei.png') #炼丹人物分配点击
        self.liandanxuanze = cv2.imread('images/liandanxuanze.png') #炼丹人物选择
        self.danyao = cv2.imread('images/danyao.png') #炼丹丹药
        self.danyaolianzhi = cv2.imread('images/danyaolianzhi.png') #丹药炼制
        self.danyaodi = cv2.imread('images/danyaodi.png') #丹药炼制调整最低
        self.liandanqueren = cv2.imread('images/liandanqueren.png') #丹药确认
        self.tuichu = cv2.imread('images/tuichu.png') #丹药退出
        self.changjinggerenwu = cv2.imread('images/changjinggerenwu.png') #藏经阁任务
        self.yanxi = cv2.imread('images/yanxi.png') #藏经阁研习
        self.yanxiquanbu = cv2.imread('images/yanxiquanbu.png') #藏经阁研习全部
        self.youli = cv2.imread('images/youli.png') #游历任务
        self.youlitiaozhan = cv2.imread('images/youlitiaozhan.png') #游历挑战
        self.youlijiangli = cv2.imread('images/youlijiangli.png') #游历奖励
        self.lingqu = cv2.imread('images/lingqu.png') #游历奖励领取
        self.youlishouyi = cv2.imread('images/youlishouyi.png') #游历快速收益
        self.youlilingqu = cv2.imread('images/youlilingqu.png') #游历快速领取
        self.youlihuicheng = cv2.imread('images/youlihuicheng.png') #游历回城
        self.suoyaota = cv2.imread('images/suoyaota.png') #锁妖塔任务
        self.suoyaota1 = cv2.imread('images/suoyaota1.png') #选择锁妖塔
        self.suoyaotajiangli = cv2.imread('images/suoyaotajiangli.png') #锁妖塔奖励
        
        self.douji = cv2.imread('images/douji.png') #主页斗技图片
        self.tiaozhan = cv2.imread('images/tiaozhan.png') #挑战3/3按钮
        self.tiaozhan1 = cv2.imread('images/tiaozhan1.png') #挑战按钮
        self.zhuye = cv2.imread('images/zhuye.png') #挑战按钮
        self.wanshangtiaozhan = cv2.imread('images/wanshangtiaozhan.png') #晚上过十点的挑战图片
        
        self.fangke = cv2.imread('images/fangke.png') #访客按钮
        self.fangkewenhao = cv2.imread('images/fangkewenhao.png') #访客人按钮
        self.fangkewenhao1 = cv2.imread('images/fangkewenhao1.png') #访客人按钮(夜间)
        self.fangkejixu = cv2.imread('images/fangkejixu.png') #访客继续按钮
        self.fangkewenti = cv2.imread('images/fangkewenti.png') #访客确认问题按钮
        self.fangkewenti1 = cv2.imread('images/fangkewenti1.png') #访客确认问题按钮
        self.fangkezhandou = cv2.imread('images/fangkezhandou.png') #访客战斗按钮
        
    
    def jietu(self):
        # 截取整个屏幕
        screenshot = pyautogui.screenshot()
        # 截取指定区域，这里的参数是一个元组，分别指定左上角和右下角的坐标
        # 例如，这里截取了屏幕上方 100 像素的区域
        region = (self.x,self.y,self.w,self.h)
        screenshot = pyautogui.screenshot(region=region)
        # 保存截图到文件
        screenshot.save('images/screenshot.png')
        large_image = cv2.imread('images/screenshot.png')
        return large_image
    
    #查找
    def chazhao(self):
        #查找弟子按钮在哪
        self.zuobiao(self.dizi)
        #查找培养按钮
        self.zuobiao(self.peiyang)
        #查找修行按钮
        self.zuobiao(self.xiuxing)
        #弟子轮询
        for i in range(60):
            location = self.zuobiao(self.xiuxingtupo)
            if location is None:
                self.zuobiao(self.next)
            else:
                self.tupos()
        self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])#手动点击空白处
        #返回到主页
        locahost = self.zuobiao(self.fanhui)
        if locahost is None:
            self.click(self.fanhuizuobiao[0],self.fanhuizuobiao[1]) #手动返回
        #访客操作
        self.fangkes()
        #任务操作
        location = self.zuobiao(self.renwu)
        if location is None:
            self.click(self.fanhuizuobiao[0],self.fanhuizuobiao[1])#手动点击返回
            self.zuobiao(self.renwu)
        self.renwus()
        time.sleep(1)
        #斗技场操作
        self.zuobiao(self.douji)
        self.doujis()
        
    
    #任务
    def renwus(self):
        localhost = self.zuobiao(self.liandanrenwu)
        if localhost is not None:
            self.liandan(localhost=localhost)
        localhost = self.zuobiao(self.changjinggerenwu)
        if localhost is not None:
            self.changjingge(localhost)
        localhost = self.zuobiao(self.youli)
        if localhost is not None:
            self.youlirenwu(localhost)
        pyautogui.moveTo(217+self.x, 461+self.y)#移动到任务栏中心
        pyautogui.scroll(-100) #滚动到最下栏
        pyautogui.scroll(-100)
        pyautogui.scroll(-100)
        localhost = self.zuobiao(self.suoyaota)
        if localhost is not None:
            self.suoyaotarenwu(localhost)
        self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])#手动到主页
    
    #锁妖塔操作
    def suoyaotarenwu(self,localhost):
        self.click(localhost[0]+250+self.x,localhost[1]+self.y+20)
        time.sleep(5)
        localhost = self.zuobiao(self.zhibiao)
        if localhost is not None:
             self.click(localhost[0]+self.x,localhost[1]+self.y+170)#进入锁妖塔
             time.sleep(2)
        self.zuobiao(self.suoyaota1)
        localhost = self.zuobiao(self.suoyaotajiangli)
        self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])#手动返回锁妖塔主页
        #如果有主页弹窗就会取消掉
        locahost = self.zuobiao(self.zhuye)
        if locahost is not None:
            self.click(self.fanhuizuobiao[0],self.fanhuizuobiao[1]) #手动退出弹窗
    
    #游历操作
    def youlirenwu(self,localhost):
        self.click(localhost[0]+250+self.x,localhost[1]+self.y+20)
        time.sleep(1)
        self.zuobiao(self.youlitiaozhan)
        time.sleep(4)
        localhost = self.zuobiao(self.youlijiangli)
        if localhost is not None:
            self.zuobiao(self.lingqu)
            time.sleep(3)
            self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])#手动点击空白处
        localhost = self.zuobiao(self.youlijiangli)
        if localhost is not None:
            self.zuobiao(self.youlishouyi)
            self.zuobiao(self.youlilingqu)
            time.sleep(3)
            self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])#手动点击空白处
            self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])#手动点击空白处
        self.zuobiao(self.youlihuicheng)#退出游历
        time.sleep(5)
        #如果有主页弹窗就会取消掉
        locahost = self.zuobiao(self.zhuye)
        if locahost is not None:
            self.click(self.fanhuizuobiao[0],self.fanhuizuobiao[1]) #手动退出弹窗
        self.zuobiao(self.renwu)#返回任务
    
    #藏经阁操作
    def changjingge(self,localhost):
        self.click(localhost[0]+250+self.x,localhost[1]+self.y+20)
        time.sleep(5)
        localhost = self.zuobiao(self.zhibiao)
        if localhost is not None:
             self.click(localhost[0]+self.x+20,localhost[1]+self.y+170)#进入藏经阁
             time.sleep(2)
        localhost = self.zuobiao(self.yanxi)
        if localhost is not None:
            self.zuobiao(self.yanxiquanbu)
            time.sleep(5)
            self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])#研习完毕
            self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])#退出研习
        self.zuobiao(self.tuichu)#退出藏经阁
        time.sleep(0.5)
        #如果有主页弹窗就会取消掉
        locahost = self.zuobiao(self.zhuye)
        if locahost is not None:
            self.click(self.fanhuizuobiao[0],self.fanhuizuobiao[1]) #手动退出弹窗
        self.zuobiao(self.renwu)#返回任务
        
            
    #炼丹炉操作
    def liandan(self,localhost):
        self.click(localhost[0]+250+self.x,localhost[1]+self.y+20)
        time.sleep(5)
        localhost = self.zuobiao(self.zhibiao)
        if localhost is not None:
            self.click(localhost[0]+self.x-10,localhost[1]+self.y+128)#进入丹炉
            time.sleep(1)
            self.click(localhost[0]+self.x-10,localhost[1]+self.y+168)#进入丹炉配置
            time.sleep(1)
        localhost = self.zuobiao(self.liandankefenpei)
        #选择炼丹分配人物
        if localhost is not None:
            self.zuobiao(self.liandanxuanze)
            self.zuobiao(self.queren)
            time.sleep(1)
        #炼丹丹药选择
        localhost = self.zuobiao(self.danyao)
        if localhost is not None:
            self.zuobiao(self.danyaolianzhi)
            localhost = self.zuobiao(self.danyaodi)
            if localhost is not None:
                self.click(localhost[0]+self.x+34,localhost[1]+self.y+16)#丹炉炼制调制最低
                localhost = self.zuobiao(self.liandanqueren)
                pyautogui.moveTo(localhost[0]+self.x, localhost[1]-50+self.y)
                pyautogui.mouseDown(button='left')
                end_x, end_y = (localhost[0]+61+self.x, localhost[1]-50+self.y)  # 指定结束点位置
                pyautogui.moveTo(end_x, end_y, duration=1)  # 移动鼠标到结束点位置
                pyautogui.PAUSE = 1  # 等待一段时间
                pyautogui.mouseUp(button='left')  # 松开鼠标左键
                self.click(end_x+60,end_y)#点击边缘
        self.zuobiao(self.tuichu)
        time.sleep(0.5)
        self.zuobiao(self.renwu)#返回任务

    #访客
    def fangkes(self):
        localhost = self.zuobiao(self.fangke)
        if localhost is None:
            self.zuobiao(self.fangke)
        time.sleep(3)
        while True:
            print("进入访客")
            localhost = self.zuobiao(self.fangkewenhao)
            if localhost is not None:
                break
            else:
                localhost = self.zuobiao(self.fangkewenhao1)
                if localhost is not None:
                    break
        time.sleep(1)
        while True:
            #连续对话(普通)
            print("访客连续对话")
            localhost = self.zuobiao(self.fangkejixu)
            if localhost is None:
                print("访客结束")
                break
            #当出现问题时(随机点击一个问题)
            localhost = self.zuobiao(self.fangkewenti)
            if localhost is not None:
                self.zuobiao(self.queren)
            localhost = self.zuobiao(self.fangkewenti1)
            if localhost is not None:
                self.zuobiao(self.queren)
            localhost = self.zuobiao(self.fangkezhandou)
            if localhost is not None:
                print("进入访客战斗")
                time.sleep(8)
                localhost = self.zuobiao(self.tiaoguo)
                if localhost is None:
                    self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])#手动点击空白处(返回到主页)
                time.sleep(3)
        locahost = self.zuobiao(self.zhuye)
        if locahost is not None:
            self.click(self.fanhuizuobiao[0],self.fanhuizuobiao[1]) #手动退出弹窗
        
        
    #斗技
    def doujis(self):
        time.sleep(2)
        for i in range(3):
            #判断是否过了十点的挑战
            locahost = self.zuobiao(self.wanshangtiaozhan)
            if locahost is not None:
                    self.click(self.fanhuizuobiao[0],self.fanhuizuobiao[1]) #手动返回
                    return
            #点击挑战
            locahost = self.zuobiao(self.tiaozhan)
            if locahost is None:
                self.click(self.fanhuizuobiao[0],self.fanhuizuobiao[1])
                return
            #选择挑战人物
            self.zuobiao(self.tiaozhan1)
            time.sleep(10)
            #循环查找是否通过挑战
            while True:
                print("进入斗技")
                locahost = self.zuobiao(self.tiaoguo)
                if locahost is not None:
                    break
            time.sleep(3)
        #返回到主页
        locahost = self.zuobiao(self.fanhui)
        if locahost is None:
            self.click(self.fanhuizuobiao[0],self.fanhuizuobiao[1]) #手动返回
        time.sleep(3)
        #如果有主页弹窗就会取消掉
        locahost = self.zuobiao(self.zhuye)
        if locahost is not None:
            self.click(self.fanhuizuobiao[0],self.fanhuizuobiao[1]) #手动退出弹窗
    
    #突破
    def tupos(self):
        #查找破镜按钮
        localhost = self.zuobiao(self.pojing)
        print("有突破:",localhost)
        if localhost is None:
            self.click(self.tupozuobiao[0],self.tupozuobiao[1])
        self.zuobiao(self.querentupo)
        #如果遇到成功率不足
        self.zuobiao(self.queren)
        #跳过突破
        localhost = self.zuobiao(self.tiaoguo)
        if localhost is not None:
            self.click(localhost[0]+self.x,localhost[1]+self.y)
            time.sleep(2)
            self.click(localhost[0]+self.x,localhost[1]+self.y)
        else:
            #手动跳过
            self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])
            self.click(self.dibuzuobiao[0],self.dibuzuobiao[1])
    
    #查找图片是否存在
    def find_image_location(self,large_image, small_image, threshold=0.9):
        w, h = small_image.shape[::2]
        res = cv2.matchTemplate(large_image, small_image, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        # 获取匹配结果中的最大值和位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        # 计算小图在大图中的中心点坐标
        center_x = int((top_left[0] + bottom_right[0]) / 2)
        center_y = int((top_left[1] + bottom_right[1]) / 2)
        
        if len(loc[0]) == 0:
            return None

        #显示每个阶段图片
        # cv2.rectangle(large_image, top_left, bottom_right, (0, 0, 255), 2)
        # cv2.imshow('Large Image', large_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return center_x,center_y
    
    #坐标
    def zuobiao(self,small_image):        
        #截图当前
        large_image = self.jietu()
        location = self.find_image_location(large_image,small_image)
        if location is None:
            print("没有找到")
        else:
            print("找到图片:", location)
            self.click(location[0]+self.x,location[1]+self.y)
        return location
        
    #点击
    def click(self,x,y):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.5)
        
        

if __name__ == "__main__":
    dao = daotianlu()
    dao.chazhao()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
