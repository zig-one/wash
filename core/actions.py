from core.ability import Ability
from core.conf import settings
from core import actionList
# from PyQt5.QtGui import QPixmap, QIcon, QPainter
import time

class Action(object):
    """动作类, 读取action.py下的列表, 去img文件下下寻找对应的图片"""

    def __init__(self):
        # self.imgDir = settings.SETUP_DIR / "img"
        pass
    def getQMovie(self, name):
        module = actionList
        pictures=[]
        ACTTime=[]
        try:
            #拿到属性
            pictureNameList = getattr(module, name)
            # for j in pictureNameList:
            #     print("j here",j)
            #     pictures.append(QPixmap(str(self.imgDir / j)))
            ACTTime = getattr(module, name+"time")
            return pictureNameList,ACTTime
        except BaseException as e:
            print(e)  
            print("There's no "+name)
            return [],[]
        
 


class ActionItem():
    #动作名字
    actionName = "1"

    #本动作能否中断别的动作
    IsInterrupt = False
    #本动作能否被中断
    Interupt_able = True
    #是否可以被拖动
    Move_able = True

    #动作优先级
    priority = 0


    #接受相应信号，屏蔽外部信号
    #接手单击
    acceptClick = False
    #接手释放
    acceptRelease = False
    #接手移动
    acceptMove = False
    #接手双击
    acceptDoubleClick = False

    #动作已经完成
    finished = False

    #帧管理
    ACTList = []
    ACTTime = []
    totTime = 0
    curTime = 0
    T_INTERVAL=500#刷新率

    def __lt__(self, other):
        return self.priority < other.priority

    def __init__(self,T_INTERVAL=500,actionName="",):
        self.TIME_INTERVAL=T_INTERVAL
        print("ttINt",self.TIME_INTERVAL)
        self.actionName = actionName
        self.imgDir = settings.SETUP_DIR / "img"        
        print("ACTList")
        print(actionName)
        self.ACTList,self.ACTTime=Action().getQMovie(actionName)
        for i in self.ACTTime:
            self.totTime+=i


    def init(self, Father):
        self.father=Father
        print("self.TIME_INTERVAL",self.TIME_INTERVAL)
        self.father.TIME_INTERVAL=self.TIME_INTERVAL
        print("fahter.TIME_INTERVAL",self.father.TIME_INTERVAL)
        self.finished=False
        
    def Clicked(self,bt=None):
        pass
    def doubleClicked(self):
        pass
    def Released(self):
        pass
    def moved(self):
        pass
    def interrupted(self):
        pass   
    def finishedAct(self):
        print("STOP!!!")
        self.finished=True
    def actionInterrupted(self):
        pass
    def nextAct(self):
        #动作已经结束
        if(self.curTime==self.totTime):
            self.finishedAct()
            return
#TODO:check safety
        #寻找当前帧
        i=self.curTime
        k=0
        print("self.curtime",self.curTime,"ACTTime.size",self.ACTTime.__len__(),"--------------------------")
        while(i>0):
           i-=self.ACTTime[k]
           k+=1
        k-=1
        #设置图像
        self.father.setPix(self.ACTList[k])
        self.curTime+=1




class drag(ActionItem):
    def __init__(self,T_INTERVAL=500):
        super(drag, self).__init__(T_INTERVAL=T_INTERVAL,actionName="drag")
        self.IsInterrupt = True
        self.acceptMove=True
        self.Move_able=True
        self.Interupt_able=False

    def nextAct(self):
        if (self.father.draging==False):
            finished=True
        else:
            if -1 <= self.father.moveDistance < 0:
                self.father.setPix(str(self.imgDir / settings.MOUSE_TO_RIGHT_1))
            elif -2 <= self.father.mmoveDistance < -1:
                self.father.setPix(str(self.imgDir / settings.MOUSE_TO_RIGHT_2))
            elif self.father.mmoveDistance < -2:
                self.father.setPix(str(self.imgDir / settings.MOUSE_TO_RIGHT_3))
            elif 0 < self.father.mmoveDistance <= 1:
                self.father.setPix(str(self.imgDir / settings.MOUSE_TO_LEFT_1))
            elif 1 < self.father.mmoveDistance <= 2:
                self.father.self.father.msetPix(str(self.imgDir / settings.MOUSE_TO_LEFT_2))
            elif 2 < self.father.mmoveDistance:
                self.father.setPix(str(self.imgDir / settings.MOUSE_TO_LEFT_3))
        


class fallingBody(ActionItem):
    def __init__(self, posX=-1, posY=-1,T_INTERVAL=10):
        super(fallingBody, self).__init__(T_INTERVAL=T_INTERVAL,actionName="fallingBody")
        self.IsInterrupt = True
        self.acceptMove=True
        self.Move_able=False
        self.Interupt_able=False
        self.posX=posX
        self.posY=posY

    def nextAct(self): 
        if(self.posX==-1):
            self.posX=self.father.geometry().x()
            self.posY=self.father.geometry().y()
        rect = self.father.desktop.availableGeometry()
        # print("here", self.pos().x(), "y", self.pos().y())
        if (self.father.pos().y() > 0) and (self.father.pos().y() < rect.height() - 200):
            #下落    
            rect = self.father.desktop.availableGeometry()
            self.father.move(self.posX, self.posY)
            #动作
            self.father.setPix("shime4.png")
            # 下落速度
            self.posY += 10
            self.father.setPix(settings.INIT_PICTURE)
        else:
            self.finishedAct()




class walk(ActionItem):
    curFrame=0
    def __init__(self,T_INTERVAL=500):
        super(walk, self).__init__(T_INTERVAL=400,actionName="walk")
        self.IsInterrupt = False
        self.acceptMove=True
        self.Move_able=True
        self.acceptClick=True
        self.Interupt_able=True
        self.finished=False

    def Clicked(self,bt=None):
        # print("stop!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        self.finishedAct()

    def nextAct(self):
        """走路"""
        # if self.father.walking is True:
        print("--walking--")
        self.father.move(self.father.pos().x() - 4, self.father.pos().y())
        if self.father.pos().x() < -128:
            self.father.move(
                self.father.desktop.availableGeometry().bottomRight().x() - 50,
                self.father.pos().y(),
            )
        # print("curFrame",self.curFrame)
        self.father.setPix(self.ACTList[self.curFrame])
        print("haha ",self.ACTList[self.curFrame])
        if self.curFrame == 1:
            self.curFrame = 0
        else:
            self.curFrame = 1
        # self.finished=False




class stand(ActionItem):
    curFrame=0
    def __init__(self,T_INTERVAL=500):
        super(stand, self).__init__(T_INTERVAL=400,actionName="stand")
        self.IsInterrupt = False
        self.acceptMove=True
        self.Move_able=True
        self.acceptClick=True
        self.Interupt_able=True

    def Clicked(self,bt=None):
        self.finishedAct()


class sing(ActionItem):
    curFrame=0
    def __init__(self,T_INTERVAL=500):
        super(sing, self).__init__(T_INTERVAL=400,actionName="sing")
        self.IsInterrupt = False
        self.acceptMove=True
        self.Move_able=True
        self.acceptClick=True
        self.Interupt_able=True

    def Clicked(self,bt=None):
        self.finishedAct()


class pull(ActionItem):
    curFrame=0
    def __init__(self,T_INTERVAL=500):
        super(pull, self).__init__(T_INTERVAL=400,actionName="pull")
        self.IsInterrupt = False
        self.acceptMove=True
        self.Move_able=True
        self.acceptClick=True
        self.Interupt_able=True

    def Clicked(self,bt=None):
        self.finishedAct()


class lie(ActionItem):
    curFrame=0
    def __init__(self,T_INTERVAL=500):
        super(lie, self).__init__(T_INTERVAL=400,actionName="lie")
        self.IsInterrupt = False
        self.acceptMove=True
        self.Move_able=True
        self.acceptClick=True
        self.Interupt_able=True

    def Clicked(self,bt=None):
        self.finishedAct()

class run(ActionItem):
    curFrame=0
    def __init__(self,T_INTERVAL=500):
        super(run, self).__init__(T_INTERVAL=400,actionName="run")
        self.IsInterrupt = False
        self.acceptMove=True
        self.Move_able=True
        self.acceptClick=True
        self.Interupt_able=True

    def Clicked(self,bt=None):
        self.finishedAct()

class boring(ActionItem):
    curFrame=0
    def __init__(self,T_INTERVAL=500):
        super(boring, self).__init__(T_INTERVAL=400,actionName="boring")
        self.IsInterrupt = False
        self.acceptMove=True
        self.Move_able=True
        self.acceptClick=True
        self.Interupt_able=True

    def Clicked(self,bt=None):
        self.finishedAct()