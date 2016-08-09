import re
def getOTPinSMS(FullString):    
    OTP = re.search( r"\d\d\d\d", FullString)
    return OTP.group()

