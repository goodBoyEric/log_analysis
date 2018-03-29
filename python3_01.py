# -*- coding :utf-8 -*-
# !/usr/bin/python3
# _author=liusong time=2018/3/29

import time

file = """C:\\Users\\zhaohaifeng\\Documents\\WeChat Files\\wxid_q51iv4rp4rwo12\\Files\\001007604624.log"""


def main_function(file_address=''):
    if file_address == '':
        raise ArithmeticError('file为空')
    open_file = open(file_address, mode='rb')
    data = open_file.read()

    # 十进制小于10，需补0
    data_16 = []
    for i in data:
        data_16_i = hex(i)
        if len(data_16_i) == 3:
            data_16_i = '0x0' + data_16_i[2]
        data_16.append(data_16_i)
    len_data = len(data_16)
    print('log总长度：%s' % len_data)
    time.sleep(1)

    # 读取50字节
    for i in range(1, int(len_data/50) + 1):
        new_i = i * 50
        start_number = new_i - 50
        one_log = data_16[start_number:new_i]
        print('\n', len(one_log), one_log)
        #  解析时间
        time_chang(one_log[:4])

        # 解析GSM状态
        gsm_status(one_log[4])

        # 解析网络状态
        internet_status(one_log[5])

        # 解析信号强度
        signal_strength(one_log[6])

        # 解析LAC
        lac_function(one_log[7:11])

        # 解析CI
        ci_function(one_log[11:15])

        # 解析GPS状态
        gps_status(one_log[15])


def time_chang(x_time):
    # print(x_time)
    string_num = ''
    for i in range(0, len(x_time)):
        string_num = string_num + x_time[i][2:]
    # print(string_num)
    aa = str(int(string_num.upper(), 16))
    time_local = time.localtime(int(aa))
    data_time = time.strftime('%Y-%m-%d %H:%M:%S', time_local)
    print('时间为：%s' % data_time)
    return data_time


def gsm_status(gsm_status_16):
    """
    0：模块断电
    1：模块上电
    2：检查模块供电PIN状态
    3：AT指令正常
    4：检测SIM卡
    5：SimCard在位
    6：注册到网络运营商
    7：开始TCP连接
    8：TCP连接OK
    :param gsm_status_16:pass
    :return:pass
    """
    gsm_status_10 = str(int(gsm_status_16.upper(), 16))
    if gsm_status_10 == '0':
        gsm_status_data = 'gsm_status:0,模块断电'
    elif gsm_status_10 == '1':
        gsm_status_data = 'gsm_status:1,模块上电'
    elif gsm_status_10 == '2':
        gsm_status_data = 'gsm_status:2,检查模块供电PIN状态'
    elif gsm_status_10 == '3':
        gsm_status_data = 'gsm_status:3,AT指令正常'
    elif gsm_status_10 == '4':
        gsm_status_data = 'gsm_status:4,检测SIM卡'
    elif gsm_status_10 == '5':
        gsm_status_data = 'gsm_status:5,SimCard在位'
    elif gsm_status_10 == '6':
        gsm_status_data = 'gsm_status:6,注册到网络运营商'
    elif gsm_status_10 == '7':
        gsm_status_data = 'gsm_status:7,开始TCP连接'
    elif gsm_status_10 == '8':
        gsm_status_data = 'gsm_status:8,TCP连接OK'
    else:
        gsm_status_data = 'gsm_status状态错误'
        assert ('gsm_status 状态错误')
    print(gsm_status_data)
    return gsm_status_data


def internet_status(internet_status_16):
    """
    0： 没有注册网络
    1：注册到了本地网络
    2： 找到运营商但没
    有注册网络
    3： 注册被拒绝
    4： 未知的数据
    5：注册在漫游
    状态.
    :return:
    """
    internet_status_10 = str(int(internet_status_16.upper(), 16))
    if internet_status_10 == '0':
        internet_status_data = 'internet_status:0,没有注册网络'
    elif internet_status_10 == '1':
        internet_status_data = 'internet_status:1,注册到了本地网络'
    elif internet_status_10 == '2':
        internet_status_data = 'internet_status:2,找到运营商但没有注册网络'
    elif internet_status_10 == '3':
        internet_status_data = 'internet_status:3,注册被拒绝'
    elif internet_status_10 == '4':
        internet_status_data = 'internet_status:4,未知的数据'
    elif internet_status_10 == '5':
        internet_status_data = 'internet_status:5,注册在漫游'
    else:
        internet_status_data = 'internet_status状态错误'
        assert ArithmeticError('internet_status状态错误')
    print(internet_status_data)
    return internet_status_data


def signal_strength(signal_strength_16):
    """
    0~31， 99为无信号
    :param signal_strength_16:
    :return:
    """
    signal_strength_data = str(int(signal_strength_16.upper(), 16))
    if signal_strength_data == '99':
        print('无信号')
    else:
        print('信号强度为：%s' % signal_strength_data)
    return signal_strength_data


def lac_function(lac_16):
    lac_data = ''
    for i in range(0, len(lac_16)):
        lac_data = lac_data + lac_16[i][2:]
    print(lac_data)
    return lac_data


def ci_function(ci_16):
    ci_data = ''
    for i in range(0, len(ci_16)):
        ci_data = ci_data + ci_16[i][2:]
    print(ci_data)
    return ci_data


def gps_status(gps_status_16):
    """
    0：休眠状态
    1：运行状态
    2：模块开启
    3：模块关闭
    4：模块重启
    :return:
    """
    gps_status_10 = str(int(gps_status_16.upper(), 16))
    if gps_status_10 == '0':
        gps_status_data = 'gps_status:0,休眠状态'
    elif gps_status_10 == '1':
        gps_status_data = 'gps_status:1,运行状态'
    elif gps_status_10 == '2':
        gps_status_data = 'gps_status:2,模块开启'
    elif gps_status_10 == '3':
        gps_status_data = 'gps_status:3,模块关闭'
    elif gps_status_10 == '4':
        gps_status_data = 'gps_status:4,模块重启'
    else:
        gps_status_data = 'gps_status_data 状态错误'
        assert ArithmeticError('gps_status_data 状态错误')
    print('GPS：%s' % gps_status_data)
    return gps_status_10

if __name__ == '__main__':
    main_function(file_address=file)
