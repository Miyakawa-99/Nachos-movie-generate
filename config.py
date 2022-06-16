import enum

# F0, SP, APの値をまとめているところ（暫定版なので適当）

class F0Type(enum.Enum):
    f_m2 = 0.2
    f_m1 = 0.4
    f_0 = 0.6
    f_1 = 1.5
    f_2 = 2.2

class ApType(enum.Enum):
    a_m2 = 0.2
    a_m1 = 0.4
    a_0 = 0.6
    a_1 = 1.0
    a_2 = 1.2

class SpType(enum.Enum):
    s_m2 = 0.2
    s_m1 = 1.4
    s_0 = 0.6
    s_1 = 1.0
    s_2 = 1.2