
from FLM_Banking.com.service.constants import *

def bannerPrinting():
    with open(BANNERPATH) as f:
        data = f.read()
        print(data)
        return None

def exit_banner_printing():
    with open(EXITBANNERPATH) as f:
        data = f.read()
        print(data)
        return None