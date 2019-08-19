import datetime
import requests
import random
import time
import json
import os
import sys
import traceback

class myPrinter(object):
    '''
    用于自定义输出
    '''
    __logPath = ''

    def __init__(self, logPath):
        self.__logPath = logPath
        self.myPrint('myPrinter 初始化成功！')

    def myPrint(self, *myPrintStr):
        """
        自定义输出
        输出到屏幕的同时输出到文件中
        输入值： 需要输出的内容
        返回值： 无
        """
        temp = ''
        for oneStr in myPrintStr:
            temp += str(oneStr)
            print('{}, 时间：{}，{}'.format(self.__logPath[:self.__logPath.index('.log')], datetime.datetime.now(), temp))
            logFile = open(self.__logPath,'a',encoding='utf-8')
            '''
            不需要则注释下面这句
            '''
            print('{}, 时间：{}，{}'.format(self.__logPath[:self.__logPath.index('.log')], datetime.datetime.now(), temp), file = logFile)

class myJson():
    '''
    class: myJson
    用途： 用于管理脚本使用过程中所用到的数据
    '''
    __userNum = ''
    __passWord = ''
    __wannaRoom = ''
    __wannaSeat = ''
    __startTime = ''
    __wannaDuration = ''
    __partnerFlag = ''
    __partnerNum = ''
    __partnerName = ''
    __partnerWannaSeat = ''
    __serverToken = ''
    __userName = ''
    __cookies = ''
    __userID = ''
    __partnerID = ''
    __jsonPath = ''
    __readedJson = {}
    myPrint = None
    
    def __init__(self, jsonPath:str, myPrinterFunc):
        self.myPrint = myPrinterFunc
        self.__jsonPath = jsonPath
        self.readJsonFile()
        self.__variablesAssignment()
    
    def readJsonFile(self):
        """
        读取本地JSON文件
        """
        file = open(self.__jsonPath, 'r', encoding='utf-8-sig')
        self.__readedJson = json.load(file)
        file.close()
    
    def __variablesAssignment(self):
        """
        将读取到的值赋给相应的变量
        """
        self.__userNum = int(self.__readedJson['userNum'])
        self.__passWord = self.__readedJson['passWord']
        self.__wannaRoom = int(self.__readedJson['wannaRoom'])
        self.__wannaSeat = int(self.__readedJson['wannaSeat'])
        self.__startTime = int(self.__readedJson['startTime'])
        self.__wannaDuration = int(self.__readedJson['wannaDuration'])
        self.__partnerFlag = bool(self.__readedJson['partnerFlag'])
        if(self.partnerFlag):
            self.__partnerNum = int(self.__readedJson['partnerNum'])
            self.__partnerName = self.__readedJson['partnerName']
            self.__partnerWannaSeat = int(self.__readedJson['partnerWannaSeat'])
        self.__serverToken = self.__readedJson['serverToken']
        self.__userName = self.__readedJson['userName']
        self.__cookies = self.__readedJson['cookies']
        self.__userID = self.__readedJson['userID']
        self.__partnerID = self.__readedJson['partnerID']

    def __saveJsonToFile(self):
        """
        保存JSON文件到本地
        """
        file = open(self.__jsonPath, 'w', encoding='utf-8-sig')
        json.dump(self.__readedJson, file, ensure_ascii=False)
        file.close()

    @property
    def userNum(self):
        return self.__userNum

    @userNum.setter
    def userNum(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__userNum, value))
        self.__userNum = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def passWord(self):
        return self.__passWord

    @passWord.setter
    def passWord(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__passWord, value))
        self.__passWord = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()
    
    @property
    def wannaRoom(self):
        return self.__wannaRoom

    @wannaRoom.setter
    def wannaRoom(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__wannaRoom, value))
        self.__wannaRoom = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def wannaSeat(self):
        return self.__wannaSeat

    @wannaSeat.setter
    def wannaSeat(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__wannaSeat, value))
        self.__wannaSeat = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def startTime(self):
        return self.__startTime

    @startTime.setter
    def startTime(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__startTime, value))
        self.__startTime = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def wannaDuration(self):
        return self.__wannaDuration

    @wannaDuration.setter
    def wannaDuration(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__wannaDuration, value))
        self.__wannaDuration = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def partnerFlag(self):
        return self.__partnerFlag

    @partnerFlag.setter
    def partnerFlag(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__partnerFlag, value))
        self.__partnerFlag = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def partnerNum(self):
        return self.__partnerNum

    @partnerNum.setter
    def partnerNum(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__partnerNum, value))
        self.__partnerNum = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def partnerName(self):
        return self.__partnerName

    @partnerName.setter
    def partnerName(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__partnerName, value))
        self.__partnerName = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def partnerWannaSeat(self):
        return self.__partnerWannaSeat

    @partnerWannaSeat.setter
    def partnerWannaSeat(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__partnerWannaSeat, value))
        self.__partnerWannaSeat = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def serverToken(self):
        return self.__serverToken

    @serverToken.setter
    def serverToken(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__serverToken, value))
        self.__serverToken = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def userName(self):
        return self.__userName

    @userName.setter
    def userName(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__userName, value))
        self.__userName = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def cookies(self):
        return self.__cookies

    @cookies.setter
    def cookies(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__cookies, value))
        self.__cookies = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__userID, value))
        self.__userID = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    @property
    def partnerID(self):
        return self.__partnerID

    @partnerID.setter
    def partnerID(self, value):
        self.myPrint('修改{}的值，从 {} 变成 {}'.format(sys._getframe().f_code.co_name, self.__partnerID, value))
        self.__partnerID = value
        self.__readedJson[sys._getframe().f_code.co_name] = value
        self.__saveJsonToFile()

    def __str__(self):
        '''
        输出相关的信息~~~
        '''
        if(self.partnerFlag):
            '''
            如果有同伴则输出用户名，cookies，以及同伴的学号姓名
            一般用于Debug
            '''
            return '类名：{}, userNum:{}, cookies:{}, partnerFlag:{}, partnerUserNum:{}, partnerName:{}'.format(self.__class__.__name__, self.userNum, self.cookies, self.partnerFlag, self.partnerNum, self.partnerName)
        else:
            return '类名：{}, userNum:{}, cookies:{}'.format(self.__class__.__name__, self.userNum, self.cookies)

class seatBooker(object):
    '''
    class: seatBooker
    用于座位预约
    bookTomoroow：测试时候使用的
    work：预约工作的入口函数
    renewInfo: 用于更新信息，第一次使用的时候或者更换了用户名密码或者小伙伴的信息。。。
    '''
    jsonPath = 'config.json'
    logPath = 'logging.log'
    bookerName = '预约者'
    czJson = None
    myPrint = None
    
    def __init__(self, bookerName, jsonPath):
        '''
        用于booker的初始化
        输入值： booker的姓名，json文件的地址
        返回值： 无
        '''
        self.bookerName = bookerName
        self.logPath = '{}.log'.format(self.bookerName)
        self.myPrint = myPrinter(self.logPath).myPrint
        self.jsonPath = jsonPath
        self.czJson = myJson(jsonPath, self.myPrint)
        if(not self.czJson.cookies):
            self.myPrint('未登录，现在开始登录！')
            self.renewInfo()
        self.myPrint('初始化成功！{}'.format(self.czJson))

    def __getTrueRoomNum(self,room):
        """
        获取真正的自习室ID
        1：二楼南，2：南楼北，3：三楼北，4：三楼南
        输入值： 想要自习室的标号
        返回值： 想要自习室的真正ID
        """
        return {
            1: 36,
            2: 35,
            3: 31,
            4: 37,
        }[room]

    def __calBeginTime(self, startTime=9, flag=0): 
        """
        计算开始时间
        这个flag用于标志是预约今天的位置还是明天的。0：今天；其他：明天。
        输入值： 开始时间和今天或者明天的标志位
        返回值： 计算好的开始时间的时间戳
        """
        mustSeconds = 3600
        d1 = datetime.datetime(1970, 1, 1)
        d2 = datetime.datetime.now()
        date = d2-d1
        date = int(date.days)
        beginTime = date*3600*24 + mustSeconds*(startTime - 8)
        if flag == 0:
            beginTime += mustSeconds*24
        return beginTime

    def __getHeaders(self, referURL = 'https://jxnu.huitu.zhishulib.com/'):
        """
        获得响应头
        输入值： 访问的前一个页面的地址，默认首页
        返回值： 构造好的文件头
        """
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                'Host': 'jxnu.huitu.zhishulib.com',
                'Referer': referURL,
                'Cookie': self.czJson.cookies
                }
        return headers

    def __sendBookSeatRequests(self, bookSeatContent, headers):
        """
        发送位置预约的请求
        输入值： 预约位置所需要的字典以及文件头
        返回值： 预约状态和获取到的requests对象
        """
        bookSeatURL = 'https://jxnu.huitu.zhishulib.com/Seat/Index/bookSeats?LAB_JSON=1'
        try:
            self.myPrint('__sendBookSeatRequests: sending request ')
            reqS = requests.Session()
            bookSeatRequst = reqS.post(bookSeatURL, data=bookSeatContent, headers=headers, timeout=3.2)
            return True, bookSeatRequst
        except:
            self.myPrint('__sendBookSeatRequests: timeout ')
            return False, None

    def __getNowYearMonthDay(self):
        """
        获取现在的年月日
        输入值： 无
        返回值： 当前是年、月、日，返回的形式是YEAR、MONTH、DAY
        """
        d = datetime.datetime.now()
        year = int(str(d)[:4])
        month = int(str(d)[5:7])
        day = int(str(d)[8:10])
        return year, month, day

    def __getNowHourMinSec(self):
        """
        获取现在的时分秒
        输入值： 无
        返回值： 当前是时、分、秒，返回的形式是HOUR、MINIUTE、SECONDS
        """
        d = datetime.datetime.now()
        hour = int(str(d)[11:13])
        miniute = int(str(d)[14:16])
        seconds = int(str(d)[17:19])
        return hour, miniute,seconds

    def __saveTrueCookies(self, loginRequest):
        """
        解析真实的cookies
        输入值： 登录时候获取的requests对象
        返回值： 无
        """
        cookies = loginRequest.cookies
        trueCookie = ''
        for cookie in cookies:
            tempLen = len(' for jxnu.huitu.zhishulib.com/>')
            trueCookie += str(cookie)[7:-tempLen] + ';'
        trueCookie = trueCookie[1:-1]
        self.czJson.cookies = trueCookie
        # return True
        
    def __login(self):
        """
        登录，获取cookies
        输入值： 无
        返回值： 登陆时候获取到的requests对象
        """
        loginSignatureURL = 'https://jxnu.huitu.zhishulib.com/User/Index/login?forward=/Seat/Index/searchSeats?space_category%5Bcategory_id%5D=591&space_category%5Bcontent_id%5D=36&LAB_JSON=1'
        LoginURL = 'https://jxnu.huitu.zhishulib.com/api/1/login'
        headers = {
            'accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Length': '299',
            'content-type': 'application/json',
            'Cookie': 'web_language=zh-CN',
            'Host': 'jxnu.huitu.zhishulib.com',
            'Origin': 'https://jxnu.huitu.zhishulib.com',
            'Referer': 'https://jxnu.huitu.zhishulib.com/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Mobile Safari/537.36'
        }
        userNum = self.czJson.userNum
        userPassword = self.czJson.passWord
        loginSignatureRequests = requests.get(loginSignatureURL)
        loginSignatureJson = loginSignatureRequests.json()
        loginCode = loginSignatureJson['content']['data']['code']
        loginStr = loginSignatureJson['content']['data']['str']
        loginContent = {
            "login_name": str(userNum),
            "password": str(userPassword),
            "code": str(loginCode),
            "str": str(loginStr)
        }
        loginRequest = requests.post(LoginURL, headers = headers, data = json.dumps(loginContent), timeout = 3.2)
        self.__saveTrueCookies(loginRequest)
        return loginRequest

    def __savePartnerID(self, getPartnerIDHeaders):
        """
        解析同伴ID，并将同伴ID存储到JSON文件中
        输入值： 获取同伴ID所需要的文件头Headers
        返回值： 无
        """
        getPartnerIDURL = 'https://jxnu.huitu.zhishulib.com/User/Index/judgeNameStudentNumber?LAB_JSON=1'
        searchUserIDContent = {'name': self.czJson.partnerName, 'student_number': self.czJson.partnerNum}
        searchUserIDRequest = requests.post(getPartnerIDURL, data=searchUserIDContent, headers=getPartnerIDHeaders)
        searchUserIDJson = searchUserIDRequest.json()
        self.myPrint("getPartnerID:  searchUserIDJson{}".format(searchUserIDJson))
        partnerID = searchUserIDJson['DATA']['user_id']
        self.czJson.partnerID = partnerID

    def __saveUserInfo(self, loginReq):
        """
        从登录返回的数据中解析用户的ID以及姓名，并且保存到JSON文件中
        输入值： 登录时候得到的requests对象
        返回值： 无
        """
        loginRequest = loginReq
        userInfoJson = loginRequest.json()
        self.czJson.userID = userInfoJson['id']
        self.czJson.userName = userInfoJson['name']

    def renewInfo(self):
        """
        更新JSON文件中的COOKIES，用户ID，如果partnerFlag置为True，则还需要更新同伴ID
        输入值： 无
        返回值： 无
        """
        loginRequest = self.__login()
        self.__saveUserInfo(loginRequest)
        if(self.czJson.partnerFlag):
            self.__savePartnerID(self.__getHeaders())

    def __getWannaSeatID(self, startTime, wannaDuration):
        """
        获取想要位置的真实ID，有小伙伴的时候就同时获得小伙伴想要位置的ID
        输入值： 开始时间和相应持续的时间，startTime是时间戳形式，wannaduration换算成秒
        返回值：用户想要位置的ID和同伴想要位置的ID，当没有小伙伴的时候，小伙伴位置的ID为0
        """
        getWannaSeatIDURL = 'https://jxnu.huitu.zhishulib.com/Seat/Index/searchSeats?LAB_JSON=1'
        wannaSeatID = 0
        partnerWannaSeatID = 0
        partnerWannaSeat = self.czJson.partnerWannaSeat
        partnerFlag = bool(self.czJson.partnerFlag)
        wannaSeat = self.czJson.wannaSeat
        getWannaSeatIDHeaders = self.__getHeaders()
        getWannaSeatIDContent = {
            'beginTime': startTime,
            'duration': wannaDuration, 
            'num': '1',
            'space_category[category_id]': '591', 
            'space_category[content_id]': str(self.__getTrueRoomNum(int(self.czJson.wannaRoom)))
        }
        getWannaSeatIDRequest = requests.post(getWannaSeatIDURL, data=getWannaSeatIDContent, headers=getWannaSeatIDHeaders)
        getWannaSeatIDJson = getWannaSeatIDRequest.json()
        if 'data' not in getWannaSeatIDJson:
            self.myPrint(getWannaSeatIDJson)
        if(wannaSeat == 0):
            wannaSeatID = getWannaSeatIDJson['data']['bestPairSeats']['seats'][0]['id']
            if(partnerFlag):
                partnerWannaSeatID += 1
        else:
            wannaSeatID = getWannaSeatIDJson['data']['POIs'][-wannaSeat]['id']
            if(partnerFlag):
                partnerWannaSeatID = getWannaSeatIDJson['data']['POIs'][-partnerWannaSeat]['id']
        return wannaSeatID, partnerWannaSeatID

    def __bookSeat(self, bookSeatContent, bookSeatHeaders):
        '''
        位置预约
        输入值： 用于位置预约所使用的数据字典
        返回值： 预约系统返回的信息以及预约状态
        '''
        isBookedFlag = False # 已有预约的标记
        requestTimes = 0 # 请求发送次数的计数器
        bookSeatState = 'fail'
        bookSeatMsg = '搞事情'
        Hour,Mins,Secs = self.__getNowHourMinSec()
        while Hour != 21 or Mins != 59 or Secs != 59: # 只要还没有到21：59：59那就一直休息
            Hour,Mins,Secs = self.__getNowHourMinSec()
            time.sleep(0.5)
        requestState, bookSeatRequest = self.__sendBookSeatRequests(bookSeatContent, bookSeatHeaders) # 发送请求
        sumOfTriedSeatsNum = 0 # 用于记录位置尝试的数量
        while(bookSeatState == 'fail' and sumOfTriedSeatsNum <= 12): # 如果没有预约成功b并且尝试次数小于13次则继续尝试
            sumOfTriedSeatsNum += 1
            requestTimes = 1 
            while requestState == False or bookSeatRequest.status_code != 200: # 如果请求没有发送成功或者对方服务器崩溃就一直请求
                requestTimes = requestTimes + 1
                requestState, bookSeatRequest = self.__sendBookSeatRequests(bookSeatContent, bookSeatHeaders)
                if(requestTimes == 60):
                    print('尝试了60次，状态码：{}'.format(bookSeatRequest.status_code))
                    break
            try:
                bookSeatRequestJson = bookSeatRequest.json()
                bookSeatState = bookSeatRequestJson['DATA']['result']
                bookSeatMsg = bookSeatRequestJson['DATA']['msg']
                if('已有的预约' in bookSeatMsg): # 已有预约表明已经有了位置，则强制中断。
                    isBookedFlag = True
                    bookSeatMsg, bookSeatState = '安排上了', "true"
                    self.myPrint('__bookSeat: 为你尝试了{}次'.format(requestTimes))
                    break
                if('已被加入黑名单' in bookSeatMsg): # 忘记签到被拉黑了直接结束本次任务！
                    bookSeatState = 'fail'
                    break
                if('选择的位置无法预约' in bookSeatMsg): # 位置被占了就尝试下一个位置
                    bookSeatState = 'fail'
                    bookSeatContent['seats[0]'] -= 1
                    self.myPrint('__bookSeat: 反馈信息如下：{} 现在开始尝试这个位置：{}'.format(bookSeatMsg, bookSeatContent['seats[0]']))
                    if(self.czJson.partnerFlag):
                        bookSeatContent['seats[1]'] += 1
                        self.myPrint('__bookSeat: 反馈信息如下：{} 现在开始尝试这两个位置：{}，{}'.format(bookSeatMsg, bookSeatContent['seats[0]'], bookSeatContent['seats[1]']))
            except:
                bookSeatState = 'fail'
                pass
            self.myPrint('__bookSeat: 为你尝试了{}次'.format(requestTimes))
        if(bookSeatState == 'fail' and isBookedFlag != True): # 尝试了60次，依旧没能成功预约上
            bookSeatState = 'fail'
            try:
                bookSeatMsg = bookSeatRequestJson['DATA']['msg'] + ', 都尝试过了'
            except:
                bookSeatMsg = '很抱歉的通知你，我真的努力了，奈何大家的学习热情真的太高了，我。。。没能帮你抢到位置，所以自己再去捡漏吧。'
        self.myPrint('__bookSeat :为你尝试了{}个位置'.format(sumOfTriedSeatsNum))
        return bookSeatMsg, bookSeatState

    def bookTomorrow(self):
        '''
        预约第二天的位置的入口函数
        输入： 无
        返回值： 无
        '''
        seatInfo = ''
        partnerFlag = bool(self.czJson.partnerFlag)
        startTime = int(self.__calBeginTime(int(self.czJson.startTime)))
        wannaDuration = 3600*int(self.czJson.wannaDuration)
        wannaSeatID, partnerWannaSeatID = self.__getWannaSeatID(startTime,wannaDuration)
        bookSeatHeaders = self.__getHeaders()
        '''
        拼装数据字典
        '''
        bookSeatContent = {
            'beginTime': startTime, 
            'duration': wannaDuration, 
            'seats[0]': wannaSeatID, 
            'seatBookers[0]': int(self.czJson.userID)
            } 
        if(partnerFlag):
            bookSeatContent['seats[1]'] = partnerWannaSeatID
            bookSeatContent['seatBookers[1]'] = self.czJson.partnerID
        self.myPrint('bookSeatContent:{}'.format(bookSeatContent))
        bookSeatMsg, bookSeatStatus = self.__bookSeat(bookSeatContent,bookSeatHeaders)
        self.myPrint('预约状态：{}，预约消息：{}'.format(bookSeatStatus,bookSeatMsg))
        if(bookSeatStatus):
            '''
            如果预约成功了则获取详细的信息
            headers暂时使用位置预约的headers
            '''
            seatInfo = self.__getBookedSeatInfo(bookSeatHeaders)
        message = '{}\n{}'.format(bookSeatMsg,seatInfo)
        if(self.czJson.serverToken):
            self.__sendMessage(message,bookSeatStatus)
        else:
            self.myPrint('预约信息：{} \n 预约情况：{}'.format(message,bookSeatStatus))
        

    def __getBookedSeatInfo(self,getBookedSeatInfoHeaders):
        '''
        获取预约成功的位置的详细信息
        输入： 用于获取预约位置状态的headers
        返回值： 包含座位详细信息的字符串
        '''
        requstStatus = False
        while(requstStatus == False):
            try:
                headers = getBookedSeatInfoHeaders
                seatInfoReq = requests.get('https://jxnu.huitu.zhishulib.com/Seat/Index/myBookingList?LAB_JSON=1',headers = headers, timeout=6.3)
                seatInfoJson = seatInfoReq.json()
                requstStatus = True
            except:
                time.sleep(12)
        seatNum = seatInfoJson['content']['defaultItems'][0]['seatNum']#位置
        roomName = seatInfoJson['content']['defaultItems'][0]['roomName']#自习室名
        startTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(seatInfoJson['content']['defaultItems'][0]['time'])))#开始时间
        endTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(seatInfoJson['content']['defaultItems'][0]['time'])+int(seatInfoJson['content']['defaultItems'][0]['duration'])))#结束时间
        seatInfo = '''
        <p>您预约的位置信息如下：</p>
        <p>自习室名称：{}</p>
        <p>座号：{}</p>
        <p>开始时间：{}</p>
        <p>结束时间：{}</p>
        <p>记得定好闹钟哦！</p>
        '''.format(str(roomName), str(seatNum), str(startTime),str(endTime))
        return seatInfo

    def work(self):
        '''
        整个类的工作函数
        输入： 无
        返回值： 无
        '''
        self.myPrint('开始工作咯！')
        while(True):
            Hour,Mins,Secs = self.__getNowHourMinSec()
            if Hour == 21 and Mins == 59:
                self.myPrint('开始预约')
                self.czJson.readJsonFile()
                try: 
                    self.bookTomorrow()
                except Exception:
                    self.myPrint('预约失败\n使用的信息：{}\n错误信息：{}'.format(self.czJson, traceback.format_exc()))
                    pass
            Mins += Secs #假装Secs有用
            time.sleep(5)

    def __sendMessage(self, msg='快来见抢座位程序最后一面啦~', state='false'):
        req = requests.post('https://sc.ftqq.com/{}.send?text=位置预约系统的来信&desp={}'.format(self.czJson.serverToken, msg))
        reqJson = req.json()
        self.myPrint('__sendMessage: {}{}{}'.format(msg, reqJson['errmsg'], state))                
        
