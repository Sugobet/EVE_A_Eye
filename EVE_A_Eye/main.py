'''
作者: Sugobet
QQ: 321355478
Github: 

脚本开源免费，使用前请先查阅readme.md文档
有任何问题请QQ联系，有必要时将会收取一定费用
'''


import os
import time
import threading
from PIL import Image, ImageFile, UnidentifiedImageError
ImageFile.LOAD_TRUNCATED_IMAGES = True
import cv2
from pykeyboard import *
import uiautomation as auto
from uiautomation.uiautomation import Bitmap
import win32clipboard
import win32con
from ctypes import *


wx_groupName = '1702366463'       # 微信群名， 留空则不发微信     请务必将要发送的群或人的这个聊天窗口设置成独立窗口中打开，并且不要最小化
wx_context = '星系警告!!!'        # 要发送的微信消息
conVal = 0.8        # 阈值：程序执行一遍的间隔时间，单位：秒
# 路径请勿出现中文
path = 'C:/Users/sugob/Desktop/EVE_A_Eye/EVE_A_Eye'        # 脚本目录绝对路径 请将复制过来的路径的反斜杠修改成斜杠！
devices = {                         # 模拟器地址，要开几个预警机就填对应预警机的模拟器的地址， 照抄
    '3QE': [        # 星系名        请勿出现中文或中文字符以及特殊字符
        '127.0.0.1:62001',      # cmd输入adb devices查看模拟器地址
        False       # 没卵用，但不能少也不能改
    ],
}
gameSendPosition = {        # 从聊天框中第二个频道开始数，即系统频道之后为第二频道
    '第二频道': '38 117',       # 本地 频道
    '第三频道': '38 170',
    '第四频道': '38 223',
    '第五频道': '38 278',
    '第六频道': '38 332',
    '第七频道': '38 382'
}
sendTo = gameSendPosition['第三频道']       # 默认发送军团频道

mutex = threading.Lock()


def setClipboardFile(paths):
    try:
        im = Image.open(paths)
        im.save('1.bmp')
        aString = windll.user32.LoadImageW(0, r"1.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
    except UnidentifiedImageError:
        setClipboardFile(paths)
        return

    if aString != 0:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
        win32clipboard.CloseClipboard()
        return
    print('图片载入失败')


def send_msg(content, msg_type=1):
    wechatWindow = auto.WindowControl(
        searchDepth=1, Name=f"{wx_groupName}")
    wechatWindow.SetActive()
    edit = wechatWindow.EditControl()
    if msg_type == 1:
        auto.SetClipboardText(content)
    elif msg_type == 2:
        auto.SetClipboardBitmap(Bitmap.FromFile(content))
    elif msg_type == 3:
        setClipboardFile(content)
    edit.SendKeys('{Enter}')
    edit.SendKeys('{Ctrl}v')
    edit.SendKeys("{Enter}")


def Start():
    # 启动时重置  ‘’图片
    with open(f'{path}/tem/list.png', 'rb') as sc1:
        con = sc1.read()
        for k in devices:
            f = open(f'{path}/new_{k}_list.png', 'wb')
            f.write(con)
            f.close()
    
    with open(f'{path}/tem/playerList.png', 'rb') as sc:
        con = sc.read()
        for k in devices:
            f = open(f'{path}/old_{k}_playerList.png', 'wb')
            f.write(con)
            f.close()
            f = open(f'{path}/new_{k}_playerList.png', 'wb')
            f.write(con)
            f.close()

    # 监听线程
    for k in devices:
        t = threading.Thread(target=Listening, args=(k, ))
        t.start()
    
    print('Started')
    context = f"预警系统已上线，监测星系列表：\n {devices.keys()}"
    mutex.acquire()
    send_msg(context, msg_type=1)
    mutex.release()


def screenc(filename, num):
    os.system(f'adb -s {devices[filename][0]} exec-out screencap -p > {filename}_{num}.png')


def crop(x1, y1, x2, y2, scFileName, svFileName):
    try:
        img = Image.open(scFileName)
        re = img.crop((x1, y1, x2, y2))
        re.save(svFileName)
        img.close()
        re.close()
    except Exception:
        return


def LoadImage(img1, img2):
    i1 = cv2.imread(img1, 0)
    i2 = cv2.imread(img2, 0)
    return i1, i2


def IF_Img_I(src, mp):
    # w, h = mp.shape[::2]
    res = None
    try:
        res = cv2.matchTemplate(src,mp,cv2.TM_CCOEFF_NORMED)
    except Exception:
        return False, 0.999
    _, mac_v, _, _ = cv2.minMaxLoc(res)
    if mac_v < 0.99:
        return True, mac_v
    return False, mac_v


def SendGameMassage(tag):
    str1 = f'adb -s {devices[tag][0]} '
    os.system(str1 + 'shell input tap 211 478')
    time.sleep(0.2)
    os.system(str1 + f'shell input tap {sendTo}')
    time.sleep(0.2)
    os.system(str1 + 'shell input tap 266 520')
    time.sleep(0.2)
    os.system(str1 + 'shell input tap 685 511')
    time.sleep(0.2)
    os.system(str1 + 'shell input tap 68 292')
    time.sleep(0.2)
    os.system(str1 + 'shell input tap 250 350')
    time.sleep(0.2)
    os.system(str1 + 'shell input tap 250 433')
    time.sleep(0.2)
    os.system(str1 + 'shell input tap 344 190')
    time.sleep(0.2)
    os.system(str1 + 'shell input tap 342 512')
    time.sleep(1)


def SendWeChat(tag, num):
    if wx_groupName == '':
        return
    mutex.acquire()
    send_msg(f'{path}/{tag}_{num}.png', msg_type=3)
    context = f"{tag} {wx_context}"
    send_msg(context, msg_type=1)
    mutex.release()


def Listening(tag):
    # *截图->裁剪->识别->动作（游戏频道发送， 微信发送）

    def task2(tag):
        num = 0
        while True:
            screenc(tag, 1)
            # 检测舰船列表, 发送 微信
            time.sleep(0.5)
            crop(918, 44, 956, 153, f'{path}/{tag}_1.png', f'new_{tag}_list.png')
            i3, i4 = LoadImage(f"{path}/new_{tag}_list.png", f"{path}/tem/list.png")
            list_status, list_mac_v = IF_Img_I(i3, i4)

            if list_mac_v !=0.0 and list_mac_v < 0.10:
                if wx_groupName == '':
                    continue
                
                if num < 1:
                    num += 1
                    print('二次检测')
                    time.sleep(2)
                    continue
                # 防误报  二次检测

                num = 0
                print(tag + '检测到舰船列表有人', list_mac_v)
                SendWeChat(tag, 1)
                i1, i2 = LoadImage(f"{path}/new_{tag}_playerList.png", f"{path}/old_{tag}_playerList.png")
                cv2.imwrite(f'{path}/old_{tag}_playerList.png', i1, [cv2.IMWRITE_PNG_COMPRESSION, 0])
                time.sleep(40)
                continue

    t = threading.Thread(target=task2, args=(tag, ))
    t.start()

    while True:
        continue
        screenc(tag, 2)
        time.sleep(conVal)
        # 第一次识别后, 判断是否检测舰船列表, 动作结束后将new playerList覆盖掉old
        time.sleep(0.35)
        crop(774, 502, 956, 537, f'{path}/{tag}_2.png', f'new_{tag}_playerList.png')
        i1, i2 = LoadImage(f"{path}/new_{tag}_playerList.png", f"{path}/old_{tag}_playerList.png")
        list_status, list_mac_v = IF_Img_I(i1, i2)

        # 疑似故障等待
        if list_mac_v <= 0.01:
            print(tag, '疑似故障')
            time.sleep(3)
            continue
            
        # 检测到本地有红白, 发送游戏频道
        if list_status:
            print(tag + '警告')
            SendGameMassage(tag)
            cv2.imwrite(f'{path}/old_{tag}_playerList.png', i1, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            time.sleep(5)


Start()
