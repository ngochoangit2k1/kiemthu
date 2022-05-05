import configparser
config = configparser.RawConfigParser()
config.read('F:\\baitap\\kiemthu\\Configuration\\config2.ini')

class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get('common-info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common-info', 'userName')
        return username

    @staticmethod
    def getnewUserName():
        username = config.get('common-info', 'newuserName')
        return username

    @staticmethod
    def getName():
        name = config.get('common-info', 'name')
        return name

    @staticmethod
    def getPassword():
        password = config.get('common-info', 'password')
        return password

    @staticmethod
    def getRePassword():
        password = config.get('common-info', 'password')
        return password

    @staticmethod
    def getEmail():
        email = config.get('common-info', 'email')
        return email