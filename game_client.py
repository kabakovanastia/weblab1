from mysocket import DataTransferClient

transfer = DataTransferClient('127.0.0.1', 4088)

while True:
    transfer.send_direction()