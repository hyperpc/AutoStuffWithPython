import json

def jsonString():
    stringOfJsonData = '{"name":"Zophie", "isCat":"True", "miceCaught":0, "felineIQ":null}'
    print('stringOfJsonData = ', stringOfJsonData)
    jsonToDict = json.loads(stringOfJsonData)
    print('jsonToDict = ', jsonToDict)
    stringOfJsonData = json.dumps(jsonToDict)
    print('stringOfJsonData = ', stringOfJsonData)

def main():
    jsonString()

if __name__ == '__main__':
    main()