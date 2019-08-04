import BunalabPy.function as bunlab

# config 
bs = bunlab.Service(username="Phichit",password="0xd9af776a579f2eae8082a03d3d40f5a3")

# send mqtt
bs.SendMQ(msg=1)

# send save data in db
bs.SendDB(table='test',tag='ok',value=1)

# send plot map
bs.SendMap(table='test',lat='123',longt='456',tag='ok',value=1)