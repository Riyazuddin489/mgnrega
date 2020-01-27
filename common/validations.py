""" this class is used to provide input validation"""
import datetime


class Validation:

    @staticmethod
    def age(user_input):
        try:
            temp = int(user_input)
            if temp > 150:
                return False
            return True
        except:
            return False

    @staticmethod
    def pincode(user_input):
        try:
            temp = int(user_input)
            if len(str(temp))== 6:
                return True
            return False
        except:
            return False

    @staticmethod
    def is_int(user_input):
        try:
            int(user_input)
            return True
        except:
            return False

    @staticmethod
    def is_date(user_input):
        try:
            datetime.datetime.strptime(user_input, '%Y-%m-%d')
            return True
        except:
            return False

    @staticmethod
    def gender(user_input):
        try:
            if str(user_input) == 'M' or str(user_input) == 'F':
                return True

            return False
        except:
            return False

