import argparse
import messages
parser = argparse.ArgumentParser()


parser.add_argument('--msg',help='Enter the message type',choices=['msg1','msg2','msg3','msg4','msg5'])
args = parser.parse_args()

msg_send = {'msg1': messages.msg1, 'msg2': messages.msg2, 'msg3': messages.msg3, 'msg4': messages.msg4, 'msg5': messages.msg5}


try:
  if args.msg in msg_send.keys():
     print(msg_send[args.msg])
   
except ValueError as ex:
     print("exception %s",ex)


