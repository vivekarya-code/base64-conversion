#base64 conversion - 2 step process to get the successful conversion message
def getBase64String(string):
    import base64
    return base64.b64encode(string.encode('utf-8'))

def getStringFromBase64String(string):
    import base64
    return base64.b64decode(string).decode('utf-8')

# Enter the string to be converted to base64
string = 'plain text' 
convertedBase64Value = getBase64String(string)
print('Converted base64 value: (successful!) \n',convertedBase64Value)

# Paste the output from above print statement here and look for successful conversion
base64Value = 'copy the output from above print statement here and look for successful conversion'
# print(getStringFromBase64String(base64Value))

#convert convertedBase64Value to string
convertedBase64Value = convertedBase64Value.decode('utf-8')

if convertedBase64Value == base64Value:
    print('Validation successful')
else:
    print('Validation not completed')
