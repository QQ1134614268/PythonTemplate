import os

# cmd = "sqlacodegen mysql://root:123456@8.129.48.72:30894/wind?charset=utf8 > models.py"

# cmd = "sqlacodegen mysql://root:6HOoIAqc22uw7gc2@119.3.178.32:31862/pledge_risk_01?charset=utf8 > risk_models.py"
cmd = "sqlacodegen mysql://root:123456@127.0.0.1:3306/wind?charset=utf8 > old_ind_models.py"
os.system(cmd)
