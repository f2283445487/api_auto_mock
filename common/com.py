import yaml
import random

base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
char0 = '京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽赣粤青藏川宁琼'
char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
char2 = '1234567890'


def read_yaml(portal):
    """读取配置文件"""
    with open(r'./config.yaml', encoding='utf-8') as f:
        read = yaml.load(f.read(), Loader=yaml.FullLoader)
        values = read.get(portal)
        return values


# def get_random_str(min_length, max_length):
#   """
#   生成指定长度的随机字符串
#   """
#   random_str = ''
#   length = len(base_str) - 1
#   for i in range(max_length):
#     random_str += base_str[random.randint(min_length, length)]
#   return random_str


def get_random_num(str1, min_length, max_length):
    """
    生成指定长度的数字
    """
    int_list = []
    for i in [min_length - 1, min_length, max_length - 1, max_length, max_length + 1]:
        random_int = random.randint(10 ** (i - 1), (10 ** i) - 1)
        if str1 == 'STRING':
            int_list.append(str(random_int))
        elif str1 == 'INT':
            int_list.append(int(random_int))
    return int_list


def get_driver_num():
    """生成随机车牌号"""
    len0 = len(char0) - 1
    len1 = len(char1) - 1
    len2 = len(char2) - 1
    code = ''
    index0 = random.randint(1, len0)
    index1 = random.randint(1, len1)
    code += char0[index0]
    code += char1[index1]
    for i in range(1, 6):
        index2 = random.randint(1, len2)
        code += char2[index2]
    return code




def get_identity():
    num = get_random_num('INT', 18, 18)
    return num


def get_mobileNumber():
    num = get_random_num('INT', 11, 11)
    return num


def mock(char):
    if char == '车牌号':
        return get_driver_num()
    elif char == '身份证号':
        return get_identity()
    elif char == '手机号':
        return get_mobileNumber()


def get_random_list(size, random_length):
    list1 = []
    for i in range(size):
        list1.append(int((random_length + 1) * random.random()) - int(random_length * random.random()))
    return list1


def change_list(char):
    while '[' in char or ']' in char:
        str1 = char.replace('[', '').replace(']', '')
        str2 = str1.split(',')
        return str2


def get_driver_list():
    list1 = []
    for i in range(5):
        list1.append(get_driver_num())
    return list1