from bs4 import BeautifulSoup
import requests

def GradeToPoint(Grade:str)->int:
    if(Grade == "O"):
        return 10
    elif(Grade == 'A+'):
        return 9
    elif(Grade == 'A'):
        return 8
    elif(Grade == 'B+'):
        return 7
    elif(Grade == 'B'):
        return 6
    elif(Grade == 'C'):
        return 5
    else:
        return 0

def GPACalculator(result:dict):
    total_credit = 0
    gpa_accum = 0
    for iter in range(0,len(result)):
        gpa_accum += GradeToPoint(result[iter]['GRADE'])*float(result[iter]['CREDIT'])
        total_credit += float(result[iter]['CREDIT']) 
    return gpa_accum/total_credit

def isItValidRollNumber(RollNumber):
    checks = 0
    if(len(RollNumber) != 10):
        return False
    try:
        int(RollNumber[:2])
    except ValueError:
        return False
    try:
        int(RollNumber[-3:], base=16)
    except ValueError:
        return False

    return True


def JNTUResultAPI(RollNumber, ExamCode="1454", etype='r17', _type_="intgrade", server="results.jntuh.ac.in"):
    resultDict = {}
    randbirthday = "2001-11-11"
    if(isItValidRollNumber(RollNumber)):
        pass
    else:
        raise(ValueError, "Roll-Number not Valid")
    jntuResultUrl = f"http://results.jntuh.ac.in/resultAction?degree=btech&examCode={ExamCode}&etype={etype}&type=intgrade&result=null&grad=null&htno={RollNumber}#"
    payload = {}
    headers = {
        'Cookie': 'JSESSIONID=464656A62D7F6AFF4257BFAA544E0A84; cookiesession1=2D2443B1D1ZYJTB8GOLAEVRLKJTO4517'
    }
    response = requests.request("POST", jntuResultUrl, data=payload)
    if(response.status_code >= 300):
        return
        
    soup = BeautifulSoup(response.text, "html.parser")
    resultTable = soup.find_all('table')[1]
    tableRow = resultTable.find_all('tr')
    for i in range(1,len(tableRow)):
        tr = tableRow[i]
        try:
            currentCol = tr.text.split('\n')[1:-1]
            resultDict[i-1] = {
                'SUB_CODE': currentCol[0],
                'SUB_NAME': currentCol[1],
                'INTERNAL': currentCol[2],
                'EXTERNAL': currentCol[3],
                'TOTAL': currentCol[4],
                'GRADE': currentCol[5],
                'CREDIT': currentCol[6]
            }
        except Exception as e:
            print(e)
            break

    return resultDict


if __name__ == "__main__":
    resultDict = JNTUResultAPI("XXXXXXXXXX")
    print(resultDict)
    print(GPACalculator(resultDict))


    
