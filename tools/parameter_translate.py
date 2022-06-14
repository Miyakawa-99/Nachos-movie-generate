import sys
import os
# 相対パス指定ができないようなのでこんなことになっている
sys.path.append(os.path.abspath(".."))
from config import F0Type, SpType, ApType

def parameterTranslate(f0, ap, sp): # まだ未検証
    # ここからF0
    if f0 == 'f-2':
        f0 = F0Type.f_m2
    elif f0 == 'f-1':
        f0 = F0Type.f_m1
    elif f0 == 'f0':
        f0 = F0Type.f_0
    elif f0 == 'f1':
        f0 = F0Type.f_1
    else:
        f0 = F0Type.f_2

    # ここからAp
    if ap == 'a-2':
        ap = ApType.a_m2
    elif ap == 'a-1':
        ap = ApType.a_m1
    elif ap == 'a0':
        ap = ApType.a_0
    elif ap == 'a1':
        ap = ApType.a_1
    else:
        ap = ApType.a_2

    # ここからSp
    if sp == 's-2':
        sp = SpType.s_m2
    elif sp == 's-1':
        sp = SpType.s_m1
    elif sp == 's0':
        sp = SpType.s_0
    elif sp == 's1':
        sp = SpType.s_1
    else:
        sp = SpType.s_2
    return f0, ap, sp