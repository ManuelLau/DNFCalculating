from PublicReference.base import *
from math import *


class 真龙星君技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    数据 = [0, 1000, 1058, 1115, 1173, 1230, 1288, 1345, 1403, 1461, 1518, 1576, 1633, 1691, 1748, 1806, 1895, 1984, 2073, 2162, 2251, 2339, 2428, 2517, 2606, 2695, 2784, 2873, 2962, 3051, 3140, 3228, 3317, 3406, 3495, 3584, 3673, 3762, 3851, 3940, 4029, 4118, 4206, 4295, 4384, 4473, 4562, 4651, 4740, 4829, 4918, 5007, 5095, 5184, 5273, 5362, 5451, 5540, 5629, 5718, 5807, 5896, 5985, 6073, 6162, 6251, 6340, 6429, 6518, 6607, 6696, 6785, 6874, 6963, 7051, 7140, 7229, 7318, 7407, 7496, 7585, 7674, 7763, 7852, 7940, 8029, 8118, 8207, 8296, 8385, 8474, 8563, 8652, 8741, 8830, 8918, 9007, 9096, 9185, 9274, 9363, 9452, 9541, 9630, 9719, 9808, 9897, 9986, 10075, 10164, 10253, 10342, 10431, 10520, 10609, 10698, 10787, 10876, 10965, 11054, 11143, 11232, 11321, 11410, 11499, 11588, 11677, 11766, 11855, 11944, 12033, 12122, 12211, 12300, 12389, 12478, 12567, 12656, 12745, 12834, 12923, 13012, 13101, 13190, 13279, 13368, 13457, 13546, 13635, 13724, 13813, 13902, 13991, 14080, 14169, 14258, 14347, 14436, 14525, 14614, 14703, 14792, 14881, 14970, 15059, 15148, 15237, 15326, 15415, 15504, 15593, 15682, 15771, 15860, 15949, 16038, 16127, 16216, 16305, 16394, 16483, 16572, 16661, 16750, 16839, 16928, 17017, 17106, 17195, 17284, 17373, 17462, 17551, 17640, 17729, 17818, 17907, 17996, 18085, 18174, 18263]
    关联技能 = ['普通攻击', '空斩打']

    def 加成倍率(self, 武器类型):
        return self.数据[self.等级] / 1000

class 真龙星君技能1(主动技能):
    名称 = '普通攻击'
    备注 = '(一轮，TP为基础精通)'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    基础 = 224.69
    成长 = 0
    基础2 = 142.11
    成长2 = 0
    CD = 2.0
    TP成长 = 0.10
    TP上限 = 3

class 真龙星君技能2(主动技能):
    名称 = '空斩打'
    所在等级 = 1
    等级上限 = 20
    基础等级 = 10
    数据1 = [0, 95, 105, 115, 126, 136, 147, 158, 168, 179, 189, 200, 210, 220, 231, 241, 252, 263, 273, 284, 294, 305, 315,
     325, 336, 346, 357, 368, 378, 389, 399, 410, 420, 430, 441, 451, 462, 473, 483, 494, 504, 515, 525, 535, 546, 556,
     567, 578, 588, 599, 609, 620, 630, 640, 651, 661, 672, 683, 693, 704, 714, 725, 735, 745, 756, 766, 777, 788, 798,
     809, 819]
    CD = 2
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能3(主动技能):
    名称 = '落凤锤'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [0, 329, 362, 397, 429, 463, 496, 530, 564, 597, 630, 663, 697, 731, 763, 797, 830, 864, 899, 931, 964, 997, 1031,
     1065, 1098, 1132, 1164, 1199, 1232, 1266, 1299, 1332, 1366, 1400, 1432, 1467, 1502, 1534, 1567, 1600, 1634, 1668,
     1700, 1735, 1767, 1802, 1836, 1868, 1902, 1935, 1968, 2003, 2035, 2070, 2102, 2136, 2170, 2203, 2236, 2270, 2303,
     2337, 2370, 2403, 2436, 2470, 2503, 2537, 2570, 2605, 2637]
    数据2 = [0, 1318, 1452, 1586, 1720, 1854, 1988, 2121, 2256, 2389, 2523, 2657, 2790, 2924, 3058, 3192, 3326, 3460, 3594,
     3727, 3862, 3995, 4130, 4263, 4397, 4530, 4663, 4798, 4931, 5066, 5199, 5333, 5467, 5601, 5735, 5869, 6003, 6137,
     6270, 6404, 6537, 6672, 6805, 6940, 7073, 7207, 7341, 7475, 7609, 7743, 7877, 8010, 8143, 8278, 8411, 8546, 8679,
     8812, 8947, 9080, 9215, 9349, 9483, 9617, 9750, 9884, 10017, 10152, 10285, 10420, 10553]
    倍率 = 1.2
    CD = 6
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能4(主动技能):
    名称 = '疾风打'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [0, 230, 255, 277, 301, 324, 347, 372, 396, 418, 442, 466, 489, 512, 536, 558, 583, 606, 630, 652, 677, 701, 723,
     747, 770, 793, 817, 841, 863, 887, 912, 934, 958, 982, 1004, 1029, 1052, 1076, 1098, 1122, 1146, 1169, 1192, 1217,
     1240, 1263, 1287, 1310, 1333, 1357, 1380, 1403, 1427, 1452, 1474, 1498, 1522, 1544, 1569, 1592, 1615, 1638, 1662,
     1684, 1709, 1732, 1755, 1779, 1803, 1827, 1850]
    数据2 = [0, 1310, 1443, 1577, 1709, 1842, 1976, 2109, 2241, 2373, 2506, 2640, 2773, 2906, 3037, 3171, 3304, 3437, 3570,
     3703, 3837, 3970, 4102, 4235, 4369, 4501, 4634, 4767, 4900, 5034, 5167, 5298, 5431, 5565, 5698, 5831, 5963, 6096,
     6230, 6363, 6496, 6628, 6762, 6895, 7028, 7161, 7292, 7426, 7559, 7692, 7825, 7959, 8091, 8223, 8357, 8490, 8623,
     8757, 8889, 9022, 9156, 9289, 9421, 9553, 9686, 9820, 9953, 10086, 10217, 10352, 10484]
    CD = 4.5
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能5(主动技能):
    名称 = '破魔符'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [0, 158, 174, 190, 206, 222, 237, 254, 270, 285, 303, 318, 334, 350, 366, 382, 398, 414, 430, 445, 463, 478, 494,
     510, 526, 542, 558, 574, 590, 607, 623, 638, 655, 670, 686, 703, 719, 735, 751, 767, 783, 799, 815, 830, 848, 863,
     879, 895, 911, 927, 943, 959, 975, 990, 1008, 1023, 1039, 1056, 1071, 1087, 1103, 1120, 1136, 1152, 1168, 1183,
     1200, 1216, 1231, 1249, 1264]
    攻击次数1 = 6
    CD = 2
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能6(被动技能):
    名称 = '潜龙'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['空斩打']
    关联技能2 = ['断空捶击','无双击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.38 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.27 + 0.03 * self.等级, 5)

class 真龙星君技能7(被动技能):
    名称 = '巨兵精通'
    所在等级 = 20
    等级上限 = 40
    基础等级 = 20
    冷却关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.01 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.01 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.01 * self.等级, 5)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.9

class 真龙星君技能8(主动技能):
    名称 = '断空捶击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据1 = [0, 69, 77, 83, 91, 97, 105, 112, 120, 126, 134, 141, 147, 155, 161, 169, 177, 184, 190, 198, 204, 212, 218, 226,
     232, 241, 248, 255, 262, 268, 276, 282, 290, 296, 304, 311, 319, 325, 333, 339, 347, 353, 360, 368, 376, 383, 390,
     397, 403, 411, 417, 425, 431, 440, 446, 454, 461, 468, 475, 481, 489, 495, 504, 511, 518, 524, 532, 538, 546, 552,
     560]
    数据2 = [0, 630, 694, 759, 823, 886, 950, 1015, 1079, 1143, 1206, 1270, 1335, 1399, 1463, 1526, 1591, 1655, 1719, 1783,
     1847, 1911, 1975, 2039, 2103, 2167, 2230, 2294, 2358, 2421, 2485, 2550, 2614, 2678, 2741, 2806, 2870, 2934, 2998,
     3062, 3126, 3190, 3254, 3318, 3382, 3446, 3510, 3574, 3639, 3702, 3766, 3830, 3894, 3959, 4022, 4086, 4150, 4215,
     4279, 4342, 4406, 4470, 4535, 4599, 4662, 4726, 4791, 4855, 4919, 4982, 5046]
    数据3 = [0, 700, 771, 842, 913, 986, 1056, 1127, 1199, 1269, 1340, 1412, 1482, 1553, 1625, 1696, 1767, 1839, 1909, 1980,
     2052, 2122, 2193, 2265, 2335, 2407, 2479, 2550, 2620, 2692, 2763, 2833, 2905, 2976, 3046, 3118, 3190, 3261, 3332,
     3403, 3474, 3545, 3616, 3687, 3758, 3829, 3901, 3973, 4043, 4114, 4186, 4256, 4327, 4399, 4469, 4540, 4613, 4683,
     4754, 4826, 4896, 4967, 5039, 5109, 5180, 5251, 5322, 5394, 5466, 5537, 5607]
    CD = 4.5
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级] + self.数据3[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能9(主动技能):
    名称 = '升天阵'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据1 = [0, 1507, 1659, 1811, 1965, 2117, 2270, 2423, 2577, 2730, 2882, 3034, 3188, 3341, 3494, 3645, 3800, 3952, 4104,
     4257, 4411, 4563, 4716, 4870, 5022, 5175, 5328, 5482, 5634, 5786, 5938, 6092, 6245, 6398, 6550, 6704, 6857, 7009,
     7162, 7316, 7468, 7621, 7775, 7926, 8079, 8232, 8386, 8538, 8691, 8843, 8997, 9150, 9303, 9455, 9609, 9762, 9913,
     10066, 10220, 10372, 10525, 10678, 10832, 10983, 11137, 11290, 11443, 11596, 11749, 11903, 12054]
    倍率 = 1.2
    CD = 5
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能10(主动技能):
    名称 = '黑暗切割'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据1 = [0, 670, 740, 809, 877, 947, 1017, 1087, 1157, 1223, 1294, 1363, 1433, 1503, 1571, 1640, 1711, 1782, 1850, 1919,
     1990, 2059, 2129, 2197, 2266, 2336, 2405, 2475, 2543, 2612, 2682, 2751, 2821, 2890, 2958, 3028, 3097, 3167, 3236,
     3305, 3374, 3444, 3514, 3582, 3652, 3723, 3793, 3861, 3930, 4000, 4070, 4138, 4208, 4277, 4347, 4417, 4486, 4555,
     4624, 4694, 4763, 4832, 4902, 4971, 5041, 5109, 5178, 5248, 5317, 5387, 5457]
    数据2 = [0, 1586, 1749, 1910, 2071, 2231, 2392, 2554, 2716, 2876, 3037, 3199, 3360, 3520, 3681, 3843, 4004, 4166, 4326,
     4487, 4648, 4810, 4970, 5131, 5293, 5455, 5615, 5776, 5937, 6098, 6258, 6421, 6582, 6743, 6903, 7065, 7226, 7388,
     7548, 7709, 7870, 8032, 8192, 8353, 8515, 8677, 8837, 8998, 9159, 9320, 9481, 9643, 9803, 9964, 10126, 10287,
     10448, 10610, 10770, 10931, 11093, 11254, 11414, 11575, 11737, 11898, 12058, 12220, 12381, 12543, 12703]
    CD = 6
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能11(主动技能):
    名称 = '朱雀符'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据1 = [0, 263, 290, 316, 343, 370, 397, 423, 450, 477, 504, 531, 557, 584, 611, 638, 664, 691, 718, 745, 771, 798, 825, 852, 878, 905, 932, 959, 985, 1012, 1039, 1066, 1092, 1119, 1146, 1174, 1200, 1225, 1252, 1278, 1305, 1332, 1359, 1387, 1413, 1440, 1467, 1494, 1520, 1547, 1574, 1601, 1627, 1654, 1681, 1708, 1734, 1761, 1788, 1815, 1841]
    攻击次数1 = 10
    CD = 6.5
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能12(主动技能):
    名称 = '星落打'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据1 = [0, 4655, 5128, 5600, 6072, 6543, 7017, 7489, 7961, 8434, 8906, 9378, 9851, 10323, 10795, 11267, 11740, 12212,
     12684, 13157, 13630, 14101, 14573, 15046, 15518, 15990, 16463, 16936, 17408, 17879, 18352, 18824, 19297, 19770,
     20242, 20714, 21185, 21658, 22130, 22603, 23076, 23548, 24020, 24493, 24964, 25437, 25909, 26382, 26854, 27326,
     27799, 28271, 28743, 29215, 29688, 30160, 30632, 31105, 31577, 32050, 32521, 32994, 33466, 33938, 34411, 34883,
     35356, 35829, 36300, 36772, 37244]
    CD = 12
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能13(主动技能):
    名称 = '巨旋风'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    近身数据 = [0, 265, 292, 319, 346, 373, 400, 427, 454, 482, 509, 536, 563, 590, 617, 642, 670, 697, 724, 751, 778, 805, 832,
     859, 886, 913, 940, 967, 994, 1021, 1048, 1075, 1102, 1129, 1156, 1183, 1210, 1237, 1263, 1290, 1317, 1344, 1371,
     1398, 1425, 1452, 1479, 1506, 1533, 1560, 1587, 1615, 1642, 1669, 1696, 1723, 1750, 1777, 1804, 1831, 1858, 1884,
     1911, 1938, 1965, 1992, 2019, 2046, 2073, 2100, 2127]
    近身倍率 = 1
    远程数据 =[0, 166, 183, 200, 216, 233, 250, 267, 283, 300, 317, 333, 351, 368, 385, 402, 418, 435, 452, 469, 485, 502, 519,
     537, 554, 570, 587, 604, 621, 637, 654, 671, 688, 704, 722, 739, 756, 773, 789, 806, 823, 839, 856, 873, 891, 908,
     924, 941, 958, 975, 991, 1008, 1025, 1042, 1058, 1076, 1093, 1110, 1127, 1143, 1160, 1177, 1194, 1210, 1227, 1244,
     1262, 1278, 1295, 1312, 1329]
    远程倍率 = 1
    攻击间隔 = 0.3
    持续时间 = 4
    攻击次数 = floor(持续时间/攻击间隔)
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.近身数据[self.等级] * self.近身倍率 + self.远程数据[self.等级] * self.攻击次数 * self.远程倍率) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能14(被动技能):
    名称 = '驱魔之书'
    所在等级 = 30
    等级上限 = 40
    基础等级 = 10
    关联技能 = ['真龙焚天','式神封灵阵','逆龙七杀','逆鳞震','灭魂符','苍龙逐日','无双击','式神：殇','疾空旋风破','落雷符','狂乱锤击','疾风打','朱雀符','黑暗切割','升天阵','落凤锤','破魔符']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.015 * self.等级, 5)


class 真龙星君技能15(主动技能):
    名称 = '狂乱锤击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 1038, 1143, 1249, 1354, 1459, 1564, 1670, 1775, 1880, 1985, 2090, 2196, 2301, 2406, 2511, 2617, 2723, 2828,
     2933, 3038, 3143, 3249, 3354, 3459, 3564, 3670, 3775, 3880, 3986, 4091, 4197, 4303, 4408, 4513, 4618, 4723, 4829,
     4934, 5039, 5144, 5250, 5355, 5460, 5565, 5670, 5776, 5881, 5986, 6093, 6198, 6303, 6409, 6514, 6619, 6724, 6830,
     6935, 7040, 7145, 7250, 7356, 7461, 7566, 7671, 7777, 7883, 7988, 8093, 8198, 8303]
    攻击次数1 = 4
    数据2 = [0, 1223, 1347, 1471, 1596, 1718, 1843, 1967, 2091, 2216, 2340, 2463, 2587, 2711, 2836, 2960, 3084, 3208, 3332,
     3457, 3580, 3704, 3829, 3952, 4077, 4201, 4325, 4450, 4573, 4697, 4821, 4945, 5070, 5194, 5318, 5443, 5565, 5690,
     5814, 5938, 6063, 6187, 6310, 6434, 6558, 6683, 6807, 6931, 7055, 7178, 7303, 7427, 7551, 7676, 7799, 7923, 8048,
     8171, 8296, 8420, 8543, 8668, 8792, 8917, 9041, 9164, 9288, 9412, 9537, 9661, 9785]
    攻击次数2 = 1
    数据3 = [0, 897, 988, 1078, 1170, 1261, 1351, 1442, 1534, 1624, 1715, 1807, 1897, 1989, 2079, 2170, 2262, 2352, 2444, 2535,
     2625, 2716, 2808, 2898, 2990, 3081, 3171, 3263, 3353, 3445, 3536, 3626, 3718, 3809, 3899, 3990, 4082, 4173, 4263,
     4355, 4446, 4537, 4627, 4719, 4810, 4900, 4992, 5083, 5174, 5264, 5356, 5447, 5537, 5630, 5720, 5810, 5901, 5993,
     6083, 6175, 6266, 6357, 6448, 6538, 6630, 6721, 6811, 6903, 6994, 7084, 7176]
    攻击次数3 = 1
    CD = 14
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能16(主动技能):
    名称 = '落雷符'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 1237, 1363, 1489, 1614, 1740, 1864, 1990, 2116, 2242, 2368, 2493, 2618, 2744, 2869, 2995, 3120, 3245, 3372,
     3497, 3623, 3749, 3873, 3999, 4124, 4251, 4377, 4502, 4628, 4753, 4879, 5003, 5131, 5256, 5381, 5507, 5632, 5758,
     5883, 6008, 6136, 6260, 6386, 6511, 6637, 6763, 6888, 7015, 7140, 7264, 7390, 7516, 7642, 7767, 7891, 8019, 8144,
     8270, 8395, 8520, 8646, 8771, 8897, 9023, 9148, 9275, 9399, 9525, 9650, 9776, 9902]
    攻击次数1 = 8
    CD = 1  # 倍率
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效CD(self, 武器类型):
        return round((20.07264407 - 0.0726440677966102 * self.等级) * self.CD / self.恢复 , 1)

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.1
        self.CD *= 0.85

class 真龙星君技能17(主动技能):
    名称 = '疾空旋风破'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据1 = [0, 746, 822, 897, 973, 1049, 1124, 1200, 1276, 1351, 1427, 1504, 1578, 1654, 1730, 1807, 1883, 1957, 2033, 2109,
     2185, 2261, 2336, 2411, 2488, 2563, 2639, 2714, 2790, 2866, 2943, 3018, 3092, 3170, 3245, 3321, 3397, 3471, 3548,
     3623, 3699, 3775, 3850, 3926, 4002, 4077, 4153, 4230, 4304, 4380, 4457, 4533, 4609, 4683, 4759, 4836, 4911, 4987,
     5062, 5137, 5214, 5290, 5365, 5440, 5517, 5592, 5669, 5744, 5818, 5896, 5971]
    攻击次数1 = 7
    数据2 = [0, 1560, 1718, 1877, 2035, 2193, 2351, 2510, 2668, 2826, 2985, 3143, 3301, 3461, 3619, 3776, 3936, 4094, 4252,
     4411, 4569, 4727, 4886, 5044, 5202, 5360, 5519, 5677, 5835, 5994, 6152, 6310, 6469, 6627, 6785, 6944, 7102, 7260,
     7419, 7577, 7735, 7894, 8052, 8210, 8368, 8527, 8685, 8843, 9002, 9160, 9318, 9477, 9635, 9793, 9952, 10110, 10268,
     10427, 10585, 10743, 10903, 11060, 11218, 11377, 11536, 11693, 11851, 12011, 12168, 12326, 12486]
    攻击次数2 = 1
    CD = 20
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.08
        self.攻击次数1 += 1
        self.CD *= 0.85

class 真龙星君技能18(主动技能):
    名称 = '式神：殇'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [0, 933, 1028, 1123, 1217, 1311, 1407, 1500, 1596, 1690, 1785, 1881, 1974, 2070, 2164, 2258, 2354, 2448, 2543, 2637,
     2732, 2828, 2921, 3017, 3110, 3206, 3302, 3395, 3490, 3584, 3679, 3775, 3869, 3964, 4057, 4153, 4249, 4342, 4437,
     4531, 4627, 4723, 4816, 4911, 5005, 5100, 5195, 5290, 5385, 5478, 5574, 5668, 5763, 5857, 5952, 6048, 6141, 6237,
     6331, 6426, 6520, 6615, 6710, 6805, 6899, 6994, 7089, 7184, 7278, 7373, 7468]
    攻击次数1 = 14
    倍率1 = 1
    数据2 = [0, 4130, 4549, 4969, 5387, 5807, 6225, 6645, 7063, 7483, 7901, 8322, 8740, 9159, 9577, 9997, 10416, 10836, 11254,
     11674, 12092, 12511, 12930, 13350, 13769, 14188, 14606, 15026, 15444, 15864, 16283, 16703, 17121, 17540, 17958,
     18379, 18797, 19217, 19635, 20055, 20473, 20893, 21311, 21731, 22150, 22569, 22987, 23408, 23826, 24245, 24663,
     25083, 25502, 25922, 26340, 26760, 27178, 27597, 28016, 28437, 28855, 29274, 29692, 30112, 30530, 30950, 31369,
     31789, 32207, 32626, 33044]
    攻击次数2 = 1
    倍率2 = 1
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 * self.倍率1 + self.数据2[self.等级] * self.攻击次数2 * self.倍率2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.攻击次数1 = 0
        self.倍率2 *= 4.79
        self.CD *= 0.95

class 真龙星君技能19(主动技能):
    名称 = '无双击'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [0, 791, 870, 950, 1031, 1110, 1190, 1272, 1352, 1432, 1512, 1592, 1673, 1753, 1833, 1913, 1994, 2074, 2154, 2234,
     2314, 2396, 2475, 2555, 2636, 2715, 2795, 2877, 2956, 3036, 3117, 3196, 3277, 3358, 3437, 3517, 3599, 3679, 3758,
     3839, 3919, 3998, 4080, 4160, 4239, 4320, 4400, 4479, 4561, 4641, 4720, 4801, 4882, 4962, 5042, 5122, 5202, 5283,
     5363, 5443, 5523, 5603, 5683, 5764, 5844, 5924, 6004, 6084, 6165, 6246, 6325]
    数据2 = [0, 10505, 11571, 12636, 13703, 14768, 15835, 16900, 17965, 19031, 20096, 21163, 22228, 23295, 24360, 25427, 26492,
     27558, 28623, 29689, 30755, 31820, 32887, 33952, 35018, 36083, 37151, 38216, 39282, 40347, 41413, 42478, 43545,
     44611, 45677, 46742, 47807, 48874, 49939, 51005, 52070, 53137, 54202, 55269, 56334, 57400, 58465, 59533, 60598,
     61663, 62729, 63794, 64860, 65925, 66993, 68058, 69124, 70189, 71256, 72321, 73388, 74453, 75519, 76584, 77649,
     78716, 79781, 80847, 81913, 82979, 84045]
    CD = 40
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能20(被动技能):
    名称 = '斗志散发'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.01 * self.等级, 5)


class 真龙星君技能21(主动技能):
    名称 = '苍龙逐日'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [0, 36333, 44758, 53183, 61609, 70036, 78460, 86885, 95310, 103736, 112162, 120587, 129011, 137437, 145862, 154288,
     162713, 171138, 179563, 187988, 196413, 204839, 213264, 221689, 230114, 238539, 246966, 255391, 263817, 272241,
     280666, 289091, 297517, 305943, 314368, 322792, 331217, 339643, 348069, 356494, 364918, 373343, 381769, 390195,
     398621, 407046, 415470, 423896, 432322, 440747, 449172, 457597, 466022, 474448, 482873, 491298, 499723, 508148,
     516573, 524999, 533424, 541850, 550275, 558699, 567126, 575551, 583977, 592402, 600828, 609251, 617677]
    倍率 = 1.1
    CD = 145

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * self.倍率


class 真龙星君技能22(主动技能):
    名称 = '灭魂符'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据1 = [0, 1410, 1554, 1697, 1839, 1983, 2126, 2270, 2412, 2556, 2699, 2843, 2985, 3129, 3271, 3416, 3558, 3701, 3843,
     3989, 4131, 4273, 4417, 4559, 4703, 4846, 4989, 5132, 5275, 5419, 5562, 5705, 5848, 5991, 6135, 6278, 6421, 6564,
     6708, 6851, 6994]
    攻击次数1 = 10
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.26
        self.CD *= 0.90


class 真龙星君技能23(主动技能):
    名称 = '逆鳞震'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [0, 24112, 26557, 29007, 31448, 33897, 36343, 38792, 41241, 43683, 46134, 48579, 51025, 53468, 55918, 58363, 60812,
     63254, 65703, 68152, 70595, 73043, 75488, 77937, 80380, 82829, 85275, 87723, 90172, 92613, 95064, 97510, 99957,
     102401, 104849, 107294, 109739, 112187, 114637, 117084, 119526, 121975, 124421, 126868, 129312, 131762, 134205,
     136655, 139097, 141547, 143994, 146440, 148886, 151331, 153780, 156223, 158672, 161118, 163566, 166010, 168458,
     170909, 173351, 175799, 178243, 180693, 183137, 185587, 188030, 190477, 192923]
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 装备护石(self):
        self.倍率 *= 1.20


class 真龙星君技能24(被动技能):
    名称 = '脉轮：式神'
    所在等级 = 75
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.34 + 0.02 * self.等级, 5)

class 真龙星君技能25(被动技能):
    名称 = '式神之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)

    def 物理攻击力倍率进图(self, 武器类型):
        return self.加成倍率(武器类型)

    def 魔法攻击力倍率进图(self, 武器类型):
        return self.加成倍率(武器类型)

class 真龙星君技能26(主动技能):
    名称 = '逆龙七杀'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [0, 1207, 1330, 1452, 1576, 1698, 1821, 1943, 2066, 2188, 2310, 2433, 2556, 2679, 2801, 2923, 3046, 3169, 3290,
     3414, 3537, 3660, 3782, 3904, 4027, 4149, 4271, 4394, 4517, 4639, 4763, 4884, 5007, 5130, 5252, 5374, 5498, 5620,
     5743, 5865, 5987, 6110, 6232, 6355, 6478, 6601, 6723, 6846, 6968, 7091, 7213, 7336, 7459, 7582, 7703, 7827, 7949,
     8070, 8194, 8316, 8440, 8562, 8684, 8807, 8930, 9051, 9175, 9297, 9421, 9543, 9664]
    数据2 = [0, 2417, 2660, 2905, 3151, 3397, 3641, 3886, 4132, 4377, 4622, 4867, 5113, 5357, 5603, 5848, 6094, 6338, 6583,
     6828, 7074, 7318, 7563, 7808, 8054, 8299, 8544, 8789, 9035, 9280, 9525, 9770, 10016, 10261, 10504, 10750, 10996,
     11241, 11485, 11730, 11977, 12222, 12466, 12711, 12957, 13203, 13447, 13692, 13938, 14182, 14427, 14672, 14918,
     15163, 15408, 15653, 15899, 16143, 16389, 16633, 16879, 17124, 17370, 17613, 17859, 18104, 18350, 18594, 18840,
     19085, 19330]
    数据3 = [0, 3623, 3991, 4359, 4727, 5094, 5462, 5830, 6198, 6565, 6934, 7301, 7669, 8037, 8403, 8772, 9139, 9506, 9876,
     10243, 10611, 10978, 11345, 11714, 12081, 12448, 12817, 13183, 13552, 13919, 14286, 14656, 15023, 15390, 15758,
     16126, 16494, 16861, 17229, 17597, 17964, 18333, 18700, 19068, 19436, 19803, 20170, 20538, 20906, 21274, 21642,
     22009, 22377, 22744, 23111, 23481, 23848, 24216, 24583, 24950, 25319, 25686, 26053, 26422, 26789, 27158, 27525,
     27892, 28261, 28628, 28996]
    数据4 = [0, 4831, 5323, 5812, 6303, 6793, 7284, 7773, 8264, 8754, 9245, 9735, 10226, 10716, 11206, 11696, 12186, 12677,
     13167, 13657, 14148, 14637, 15128, 15617, 16109, 16598, 17090, 17579, 18070, 18560, 19050, 19540, 20030, 20521,
     21011, 21502, 21992, 22481, 22972, 23462, 23953, 24443, 24934, 25423, 25915, 26403, 26895, 27384, 27875, 28365,
     28856, 29346, 29837, 30326, 30817, 31306, 31797, 32287, 32778, 33268, 33758, 34248, 34739, 35229, 35720, 36210,
     36700, 37190, 37680, 38170, 38661]
    数据5 = [0, 6041, 6653, 7266, 7879, 8491, 9104, 9718, 10330, 10943, 11556, 12169, 12782, 13395, 14007, 14620, 15233, 15846,
     16457, 17071, 17684, 18297, 18910, 19523, 20135, 20749, 21361, 21974, 22588, 23199, 23812, 24426, 25038, 25651,
     26263, 26877, 27490, 28103, 28716, 29329, 29941, 30554, 31166, 31780, 32393, 33004, 33618, 34231, 34843, 35457,
     36069, 36682, 37296, 37908, 38521, 39135, 39746, 40359, 40972, 41585, 42198, 42810, 43423, 44037, 44650, 45262,
     45874, 46488, 47101, 47713, 48326]
    数据6 = [0, 7248, 7983, 8719, 9455, 10190, 10925, 11661, 12397, 13131, 13867, 14603, 15338, 16072, 16808, 17544, 18280,
     19015, 19750, 20485, 21222, 21957, 22692, 23428, 24163, 24897, 25633, 26370, 27105, 27839, 28575, 29310, 30047,
     30782, 31517, 32252, 32988, 33723, 34457, 35194, 35930, 36665, 37400, 38136, 38871, 39607, 40342, 41077, 41813,
     42548, 43283, 44019, 44755, 45490, 46224, 46960, 47697, 48432, 49167, 49902, 50637, 51373, 52108, 52844, 53579,
     54315, 55050, 55785, 56522, 57257, 57991]
    数据7 = [0, 25381, 27956, 30531, 33105, 35681, 38256, 40831, 43406, 45982, 48555, 51130, 53705, 56281, 58856, 61431, 64005,
     66581, 69155, 71730, 74305, 76881, 79455, 82030, 84605, 87181, 89756, 92329, 94904, 97479, 100055, 102630, 105205,
     107779, 110355, 112930, 115504, 118079, 120655, 123229, 125804, 128379, 130955, 133530, 136105, 138678, 141254,
     143829, 146404, 148979, 151555, 154129, 156704, 159278, 161854, 164429, 167004, 169578, 172154, 174729, 177304,
     179879, 182452, 185028, 187603, 190178, 192753, 195329, 197903, 200478, 203053]

    CD = 50

    def 等效百分比(self, 武器类型):
         return (self.数据1[self.等级]+self.数据2[self.等级]+self.数据3[self.等级]+self.数据4[self.等级]+self.数据5[self.等级]+self.数据6[self.等级]+self.数据7[self.等级])*self.倍率

class 真龙星君技能27(主动技能):
    名称 = '式神封灵阵'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据1 = [0, 1234, 1357, 1483, 1609, 1733, 1859, 1984, 2108, 2234, 2359, 2484, 2610, 2735, 2859, 2984, 3110, 3235, 3360,
     3485, 3610, 3736, 3861, 3987, 4110, 4236, 4362, 4486, 4612, 4737, 4862, 4987, 5112, 5237, 5362, 5488, 5612, 5737,
     5863, 5987, 6113, 6238, 6363, 6489, 6614, 6739, 6863, 6990, 7115, 7238, 7364, 7490, 7615, 7740, 7865, 7990, 8115,
     8241, 8365, 8491, 8616, 8740, 8866, 8991, 9115, 9241, 9366, 9492, 9617, 9743, 9868]
    攻击次数1 = 20
    数据2 = [0, 23436, 25813, 28190, 30569, 32945, 35322, 37700, 40077, 42455, 44833, 47210, 49588, 51965, 54343, 56721, 59098,
     61475, 63853, 66230, 68609, 70986, 73363, 75741, 78118, 80496, 82874, 85251, 87630, 90006, 92383, 94762, 97138,
     99516, 101892, 104270, 106648, 109026, 111403, 113781, 116159, 118536, 120913, 123291, 125669, 128047, 130424,
     132801, 135179, 137557, 139934, 142312, 144690, 147067, 149444, 151822, 154200, 156577, 158953, 161331, 163709,
     166086, 168464, 170842, 173218, 175597, 177974, 180352, 182730, 185107, 187485]
    攻击次数2 = 1
    CD = 50

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 真龙星君技能28(主动技能):
    名称 = '真龙焚天'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [0, 2063, 2543, 3021, 3500, 3978, 4457, 4935, 5415, 5893, 6371, 6850, 7328, 7807, 8287, 8765, 9243, 9722, 10201,
     10679, 11158, 11637, 12115, 12594, 13072, 13550, 14030, 14509, 14987, 15465, 15943, 16422, 16903, 17381, 17859,
     18337, 18816, 19295, 19774, 20252, 20730, 21209, 21688, 22166, 22645, 23123, 23603, 24081, 24559, 25037, 25517,
     25997, 26475, 26953, 27431, 27910, 28390, 28868, 29346, 29824, 30303, 30782, 31261, 31740, 32218, 32697, 33176,
     33654, 34133, 34611, 35090]
    攻击次数1 = 30
    数据2 = [0, 29192, 35962, 42731, 49501, 56270, 63039, 69809, 76579, 83347, 90117, 96886, 103656, 110424, 117195, 123963,
     130733, 137503, 144272, 151041, 157810, 164580, 171350, 178118, 184889, 191657, 198427, 205196, 211966, 218734,
     225504, 232274, 239043, 245812, 252582, 259351, 266121, 272890, 279660, 286428, 293198, 299967, 306737, 313505,
     320276, 327045, 333814, 340583, 347353, 354122, 360892, 367661, 374431, 381199, 387970, 394738, 401508, 408277,
     415047, 421815, 428585, 435355, 442124, 448893, 455663, 462432, 469202, 475970, 482741, 489509, 496279]
    攻击次数2 = 1
    数据3 = [0, 107923, 132950, 157975, 183002, 208027, 233054, 258079, 283105, 308131, 333157, 358183, 383210, 408235, 433262,
     458287, 483314, 508339, 533364, 558390, 583417, 608442, 633469, 658494, 683521, 708546, 733571, 758598, 783624,
     808650, 833677, 858703, 883729, 908754, 933781, 958806, 983830, 1008857, 1033883, 1058910, 1083935, 1108961,
     1133987, 1159013, 1184039, 1209065, 1234090, 1259117, 1284143, 1309170, 1334195, 1359221, 1384247, 1409273,
     1434297, 1459324, 1484350, 1509377, 1534402, 1559429, 1584454, 1609480, 1634506, 1659532, 1684558, 1709584,
     1734610, 1759637, 1784662, 1809689, 1834714]
    攻击次数3 = 0
    CD = 180.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * self.倍率

class 真龙星君技能29(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 真龙星君技能30(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class 真龙星君技能31(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


真龙星君技能列表 = []
i = 0
while i >= 0:
    try:
        exec('真龙星君技能列表.append(真龙星君技能' + str(i) + '())')
        i += 1
    except:
        i = -1

真龙星君技能序号 = dict()
for i in range(len(真龙星君技能列表)):
    真龙星君技能序号[真龙星君技能列表[i].名称] = i

真龙星君一觉序号 = 0
真龙星君二觉序号 = 0
真龙星君三觉序号 = 0
for i in 真龙星君技能列表:
    if i.所在等级 == 50:
        真龙星君一觉序号 = 真龙星君技能序号[i.名称]
    if i.所在等级 == 85:
        真龙星君二觉序号 = 真龙星君技能序号[i.名称]
    if i.所在等级 == 100:
        真龙星君三觉序号 = 真龙星君技能序号[i.名称]

真龙星君护石选项 = ['无']
for i in 真龙星君技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        真龙星君护石选项.append(i.名称)

真龙星君符文选项 = ['无']
for i in 真龙星君技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        真龙星君符文选项.append(i.名称)


class 真龙星君角色属性(角色属性):
    职业名称 = '真龙星君'

    武器选项 = ['念珠', '战斧']


    主BUFF = 1.76

    # 基础属性(含唤醒)
    基础力量 = 921
    基础智力 = 909

    # 适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    防具类型 = '板甲'

    # 人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    远古记忆 = 0
    反身空斩打 = 0
    力法及精通 = 0

    def __init__(self):
        self.技能栏 = deepcopy(真龙星君技能列表)
        self.技能序号 = deepcopy(真龙星君技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        if self.技能栏[self.技能序号['潜龙']].等级 != 0:
            self.技能栏[self.技能序号['普通攻击']].基础 += 200
            self.技能栏[self.技能序号['普通攻击']].基础2 *= 1.56 + 0.04 * self.技能栏[self.技能序号['潜龙']].等级
            self.技能栏[self.技能序号['巨旋风']].近身倍率 *= 1.23 + 0.02 * self.技能栏[self.技能序号['潜龙']].等级
            self.技能栏[self.技能序号['巨旋风']].远程倍率 *= 1.36 + 0.04 * self.技能栏[self.技能序号['潜龙']].等级
            self.技能栏[self.技能序号['巨旋风']].持续时间 += 1.3 + 0.05 * self.技能栏[self.技能序号['潜龙']].等级
            self.技能栏[self.技能序号['疾空旋风破']].攻击次数1 += 2
        if self.反身空斩打 == 1:
            self.技能栏[self.技能序号['空斩打']].被动倍率 *= (1 + 0.1 * self.技能栏[self.技能序号['普通攻击']].TP等级) * (2.92 + 0.08 * self.技能栏[self.技能序号['潜龙']].等级)
        else:
            self.技能栏[self.技能序号['空斩打']].被动倍率 *= (1 + 0.1 * self.技能栏[self.技能序号['普通攻击']].TP等级) * (1.96 + 0.04 * self.技能栏[self.技能序号['潜龙']].等级)
        if self.力法及精通 == 0 or self.力法及精通 == 1:
            self.技能栏[self.技能序号['真龙焚天']].攻击次数1 = 0
            self.技能栏[self.技能序号['真龙焚天']].攻击次数2 = 0
            self.技能栏[self.技能序号['真龙焚天']].攻击次数3 = 1
            self.技能栏[self.技能序号['无双击']].倍率 *= 1.2

class 真龙星君(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 真龙星君角色属性()
        self.角色属性A = 真龙星君角色属性()
        self.角色属性B = 真龙星君角色属性()
        self.一觉序号 = 真龙星君一觉序号
        self.二觉序号 = 真龙星君二觉序号
        self.三觉序号 = 真龙星君三觉序号
        self.护石选项 = deepcopy(真龙星君护石选项)
        self.符文选项 = deepcopy(真龙星君符文选项)

    def 界面(self):
        super().界面()

        self.力法及精通选择=MyQComboBox(self.main_frame2)
        self.力法及精通选择.addItem('板甲力驱')
        self.力法及精通选择.addItem('重甲力驱')
        self.力法及精通选择.addItem('布甲法驱')
        self.力法及精通选择.resize(120,20)
        self.力法及精通选择.move(315,480)

        self.反身空斩打=QCheckBox('空斩打冲击波',self.main_frame2)
        self.反身空斩打.resize(100,20)
        self.反身空斩打.move(325,520)
        self.反身空斩打.setStyleSheet(复选框样式)
        self.反身空斩打.setToolTip('触发潜龙冲击波')

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        if self.反身空斩打.isChecked():
            属性.反身空斩打 = 1
        属性.力法及精通 = self.力法及精通选择.currentIndex()
        if 属性.力法及精通 == 0:
            属性.防具类型 = '板甲'
            属性.伤害类型 = '物理百分比'
            属性.防具精通属性 = '力量'
        if 属性.力法及精通 == 1:
            属性.防具类型 = '重甲'
            属性.伤害类型 = '物理百分比'
            属性.防具精通属性 = '力量'
        if 属性.力法及精通 == 2:
            属性.防具类型 = '布甲'
            属性.伤害类型 = '魔法百分比'
            属性.防具精通属性 = '智力'
