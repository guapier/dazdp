# from scrapy import cmdline
#
# cmdline.execute("scrapy crawl dazdp".split())


import websocket
ws = websocket.create_connection("ws://web.im.weibo.com/im/req",cookie = 'SINAGLOBAL=8433472914926.123.1499996139220; UOR=rango.swoole.com,widget.weibo.com,login.sina.com.cn; un=toyaowu@163.com; wvr=6; SSOLoginState=1501031092; SCF=Aj966k7h9b0_Y_EoiFRIfRUem-3d_3B7T4NXgcQ5EBsC9z-0BrGb1GCqfB_UOnNpjUJ2Jmj7OzWiz_L-I-ajWWM.; SUB=_2A250c5r2DeRhGedG6lMU9ybNzzuIHXVXCIs-rDV8PUNbmtAKLUHtkW9JZRSc8s2fvMajomvHa97_E5vBfw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWHgYwgbZAPOp8WyGMM-ZvQ5JpX5KMhUgL.Fo2ReK2fS0npShM2dJLoIEXLxK-LBKML1-2LxKBLB.eL12BLxKML1-2L1hBLxK-LB.-LB--LxK-L12BL1-2t; SUHB=0gHTgj5jiOTS0e; ALF=1532567091; _s_tentry=-; Apache=4824463791087.796.1501030988981; ULV=1501030988993:6:6:4:4824463791087.796.1501030988981:1500986662388; BAYEUX_BROWSER=b28c-v8zk47pej6qzj5kclhwkz9o')
print("Sending 'Hello, World'...")
ws.send('"data":{"cmd":"msg","uid":"1703919130","msg":"忙什么呢？"},"id":"29","clientId":"dc3ij1vebdp0j1gnzz2hnb9w8j29t1","timestamp":"Wed, 26 Jul 2017 01:59:46 GMT"}')
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()