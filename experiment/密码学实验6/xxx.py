import pyDes
import random


class User:
    def __init__(self, userid):
        self.id = userid
        self.key_with_kdc = None


class KDC:
    def __init__(self, user_list: list):
        self.keys = {}
        for user in user_list:
            key = str(random.randint(0, 99999999)).zfill(8)
            user.key_with_kdc = key
            self.keys[user.id] = key

    def produce_key(self):
        return str(random.randint(0, 99999999)).zfill(8)


def distribute_key(user1: User, user2: User, kdc: KDC):
    des_obj_1kdc = pyDes.des(user1.key_with_kdc)  # 初始化user1和kdc之间用于加解密的des对象
    des_obj_2kdc = pyDes.des(user2.key_with_kdc)  # 初始化user2和kdc之间用于加解密的des对象
    content_toprint = []
    content = []
    # 第一步
    request = user1.id+user2.id
    n1 = abs(hash(request))  # 生成用于标识user1和user2会话的的唯一标识
    content.append(request+'||'+str(n1))
    content_toprint.append(user1.id+'->'+'KDC: ' + content[0])
    # 第二步
    ks = kdc.produce_key()
    des_obj_12 = pyDes.des(ks)
    in_content = des_obj_2kdc.encrypt(ks+'||'+user1.id, padmode=pyDes.PAD_PKCS5)
    outcontent = des_obj_1kdc.encrypt(ks+'||'+content[0]+'||'+str(in_content), padmode=pyDes.PAD_PKCS5)
    content.append(outcontent)
    content_toprint.append("KDC->"+user1.id+': '+str(outcontent))
    # 第三步
    content.append(in_content)
    content_toprint.append(user1.id+'->'+user2.id+': '+str(in_content))
    # 第四步 假设f(x)为hash()%10000
    n2 = random.randint(100, 10000000)
    tmp = des_obj_12.encrypt(str(n2), padmode=pyDes.PAD_PKCS5)
    content.append(tmp)
    content_toprint.append(user2.id+'->'+user1.id+': '+str(tmp))
    # 第五步
    tmp = hash(n2)  # 对发送来的数字fx运算
    content.append(tmp)
    content_toprint.append(user1.id+"->"+user2.id+": "+str(tmp))
    for i in content_toprint:
        print(i)

    print("明文:")
    print(user1.id+'->'+'KDC: ' + content[0])
    print("KDC->"+user1.id+': ', des_obj_1kdc.decrypt(content[1]))
    print(user1.id+'->'+user2.id+': ', des_obj_2kdc.decrypt(content[2]))
    print(user2.id+'->'+user1.id+': ', des_obj_12.decrypt(content[3]))
    print(user1.id+"->"+user2.id+": "+str(content_toprint[4]))

if __name__ == '__main__':
    users = []
    for i in range(10):
        users.append(User(chr(65+i)))
    Kdc = KDC(users)
    distribute_key(users[0], users[1], Kdc)  # 用户A和B进行通信
    print("\n")
    distribute_key(users[5], users[6], Kdc)  # 用户f和用户g进行通信


