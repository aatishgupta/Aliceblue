from alice_blue import *
import logging
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    #username and password through which you login to alice blue web portal
    username ='AB166212'
    password ='app#123597'
    #set all your questions answer same
    twoFa ='secret'
    #put a mail to  tradestore@aliceblueindia.com  to get api secret
    api_secret ='AKUCETSC1GMVI6CNCIJT5W4UX2M830JA1DSWZLMOYW6H4GXAL3V1JP8V24PJ6Odfasda9siutyslg'

    access_token = AliceBlue.login_and_get_access_token(username, password, twoFa, api_secret)
    print(access_token)
