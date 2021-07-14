import pywhatkit

print('Make sure your browser is open during execution of this application like number and msg and keep it running in background')
print('and make sure your browser can use your whatsapp without scanning qr code!!!\n')

number = '+91' + input('Enter receivers mobile number with country code example 1234456789 : ')
hour = 0
minute = 0
msg = input('Enter Message : ')

while True:
    hour = int(input('At what hour you what to send the message enter from 1-24 : '))
    if hour < 1 or hour > 24:
        print("Enter Hour in Range")
    else:
        break;

while True:
    minute = int(input('At what minute you what to send the message enter from 1-60 : '))
    if minute < 1 or minute > 60:
        print("Enter Minute in Range")
    else:
        break;

pywhatkit.sendwhatmsg(number, msg, hour, minute)