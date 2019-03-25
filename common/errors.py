'''错误码'''

OK = 0


class LogicError(Exception):
    '''逻辑错误的基类'''
    code = None
    data = None

    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return self.__class__.__name__


def gen_logic_err(name, code):
    '''动态创建一个 LogicError 的子类'''
    bases = (LogicError,)
    attr_dict = {'code': code}
    return type(name, bases, attr_dict)


PhonenumErr = gen_logic_err('PhonenumErr', 1000)
VcodeErr = gen_logic_err('VcodeErr', 1001)
LoginReqired = gen_logic_err('LoginReqired', 1002)
UserNotExist = gen_logic_err('UserNotExist', 1003)
ProfileErr = gen_logic_err('ProfileErr', 1004)
StypeErr = gen_logic_err('StypeErr', 1005)
RewindLimited = gen_logic_err('RewindLimited', 1006)
PermissionRequired = gen_logic_err('PermissionRequired', 1007)
