from bs4 import BeautifulSoup
import requests


class JNTUResult:
    SERVERS = ['http://results.jntuh.ac.in', 'http://202.63.105.184/results']

    def __init__(self, rollNum: str, examCode: int, **kwargs):
        self.user = None
        self.rollNum = self.isValidRollNumber(rollNum)
        self.examCode = str(examCode)
        self.degree = kwargs.get('degree', "btech")  # Defaults to btech
        self.eType = kwargs.get('eType', "r17")  # Defaults to R18 results
        # Defaults to Sem results
        self.out_type = kwargs.get('out_type', "intgrade")

        self.url = self.get_url()

    def __call__(self):
        self.result = self.JNTUResultAPI()
        self.sgpa = self.SGPACalculator(self.result)
        return {
            'user': self.user,
            'result': self.result,
            'sgpa': self.sgpa
        }

    @staticmethod
    def isValidRollNumber(rollNum: str = None) -> str:
        if(len(rollNum) != 10):
            raise ValueError("Roll-Number not 10 digit")
        try:
            int(rollNum[:2])
            int(rollNum[-3:], base=16)
        except ValueError:
            raise ValueError("Roll-Number not Valid")
        return rollNum

    def get_url(self) -> str:
        params = [
            f"degree={self.degree}",
            f"&examCode={self.examCode}",
            f"&etype={self.eType}",
            f"&type={self.out_type}",
            f"&htno={self.rollNum}",
            f"&result=null&grad=null"
        ]
        final = f'{self.SERVERS[0]}/resultAction?'+''.join(params)
        print(final)
        return final

    @staticmethod
    def gradeToPoints(grade: str) -> int:
        if(grade == 'F' or grade == 'Ab'):
            return 0
        elif(grade == 'C'):
            return 5
        elif(grade == 'B'):
            return 6
        elif(grade == 'B+'):
            return 7
        elif(grade == 'A'):
            return 8
        elif(grade == 'A+'):
            return 9
        elif(grade == "O"):
            return 10
        else:
            return 0

    def SGPACalculator(self, result: dict) -> float:
        if not result:
            return
        total_credit = 0
        gpa_accum = 0
        for item in result:
            gpa_accum += self.gradeToPoints(item['GRADE']) * \
                float(item['CREDIT'])
            total_credit += float(item['CREDIT'])
        return round(gpa_accum/total_credit, 2)

    def JNTUResultAPI(self):
        resultDict = []
        response = requests.request("POST", self.url)
        if(response.status_code >= 300):
            return
        soup = BeautifulSoup(response.text, "html.parser")
        resultTable = soup.find_all('table')
        nameRow = resultTable[0].find_all('b')
        self.user = [nameRow[n+1].text for n in range(0, len(nameRow), 2)]
        tableRow = resultTable[1].find_all('tr')
        for i in range(1, len(tableRow)):
            tr = tableRow[i]
            try:
                currentCol = tr.text.split('\n')[1:-1]
                resultDict.append({
                    'SUB_CODE': currentCol[0],
                    'SUB_NAME': currentCol[1],
                    'INTERNAL': currentCol[2],
                    'EXTERNAL': currentCol[3],
                    'TOTAL': currentCol[4],
                    'GRADE': currentCol[5],
                    'CREDIT': currentCol[6]
                })
            except Exception as e:
                print(e)
                break

        return resultDict


if __name__ == "__main__":
    result = JNTUResult("18P61A0469", 1454)
    print(result())
