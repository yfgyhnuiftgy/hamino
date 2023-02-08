import hamino
import json
clint=hamino.Client()
clint.login(input("email :"),input("password :"))
x = clint.get_from_link(input("chat link in your community :"))
x1 = clint.get_from_link(input("chat link you want get host from :"))
s = hamino.Local(comId=x.comId)
s.transfer_host(chatId=x.objectId,userIds=[clint.uid])
reqId=s.get_chat_info(chatId=x.objectId).json
reqId=reqId['extensions']['organizerTransferRequest']["requestId"]
s2=hamino.Local(comId=x1.comId)
s2.accept_host(chatId=x1.objectId,requestId=reqId)
print('Doin')