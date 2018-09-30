import time
import re
import sys


class Tools(object):
    def get_current_time(self,format_="[%Y-%m-%d %H:%M:%S]"):
        return time.strftime(format_, time.localtime(time.time()))

    def log(self,msg=None):
        print(Tools.get_current_time() + msg)

    def wash_off_html_tag(self,str=None):
        if str is None:
            return str
        return re.sub(self,re.compile(r'<\w+>|</\w+>|<\w+/>|&quot'), '', str)

    def setup_log_mode(self,use_file=False, file_name="record.log"):
        if use_file:
            sys.stdout = open(file_name, "w")