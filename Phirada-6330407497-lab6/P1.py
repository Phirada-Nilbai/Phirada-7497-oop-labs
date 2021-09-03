def flie():
    t = (2, 123.4567, 10000, 12345.67)
    strformat = 'file_{:0>3d}:{:9.2f},{:.2e},{:.3g}'.format(*t)
    return strformat
print(flie())
