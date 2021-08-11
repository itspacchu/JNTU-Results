# jntu-scraper
Results page scraping of jntuh website

## Basic usage
 
```python jnturesultscrap.py ROLLNO EXAMCODE SAVETOFILE``` 

Eg: ```python jnturesultscrap.py 18AG1A0420 1454``` 


<br>

## To use it as an import
```
from jnturesultscrap import *
ResultOfPerson = JNTUResult(rno, 1454)
```

## Output format
```
$python3 .\jnturesultscrap.py XXXXXXXXXX XXXX

{'user': ['XXXXXXXXXX', 'XXXX XXXXXXXX', 'XXXX XXXXXXXX', 'XX'], 'result': [{'SUB_CODE': '15501', 'SUB_NAME': 'ADVANCED COMMUNICATION SKILLS LAB', 'INTERNAL': '23', 'EXTERNAL': '67', 'TOTAL': '90', 'GRADE': 'O', 'CREDIT': '1'}, {'SUB_CODE': '15507', 'SUB_NAME': 'DATA COMMUNICATIONS AND NETWORKS LAB', 
'INTERNAL': '25', 'EXTERNAL': '73', 'TOTAL': '98', 'GRADE': 'O', 'CREDIT': '1.5'}, {'SUB_CODE': '15522', 'SUB_NAME': 'MICROPROCESSORS & MICROCONTROLLERS LAB', 'INTERNAL': '22', 'EXTERNAL': '65', 'TOTAL': '87', 'GRADE': 'A+', 'CREDIT': '1.5'}, {'SUB_CODE': '15531', 'SUB_NAME': 'INTELLECTUAL PROPERTY RIGHTS', 'INTERNAL': '67', 'EXTERNAL': '0', 'TOTAL': '67', 'GRADE': 'B+', 'CREDIT': '0'}, {'SUB_CODE': '15533', 'SUB_NAME': 'CYBER SECURITY', 'INTERNAL': '62', 'EXTERNAL': '0', 'TOTAL': '62', 'GRADE': 'B+', 'CREDIT': '0'}, {'SUB_CODE': '155AG', 'SUB_NAME': 'BUSINESS ECONOMICS & FINANCIAL ANALYSIS', 'INTERNAL': '22', 'EXTERNAL': '26', 'TOTAL': '48', 'GRADE': 'C', 'CREDIT': '3'}, {'SUB_CODE': '155AR', 'SUB_NAME': 'CONTROL SYSTEMS', 'INTERNAL': '17', 'EXTERNAL': '13', 'TOTAL': '30', 'GRADE': 'F', 'CREDIT': '0'}, {'SUB_CODE': '155AV', 'SUB_NAME': 'DATA COMMUNICATIONS AND NETWORKS', 'INTERNAL': '17', 'EXTERNAL': '5', 'TOTAL': '22', 'GRADE': 'F', 'CREDIT': '0'}, {'SUB_CODE': '155BC', 'SUB_NAME': 'ELECTRONIC MEASUREMENTS AND INSTRUMENTATION', 'INTERNAL': '16', 'EXTERNAL': '6', 'TOTAL': '22', 'GRADE': 'F', 'CREDIT': '0'}, {'SUB_CODE': '155CF', 'SUB_NAME': 'MICROPROCESSORS & MICROCONTROLLERS', 'INTERNAL': '20', 'EXTERNAL': '4', 'TOTAL': '24', 'GRADE': 'F', 'CREDIT': '0'}], 'sgpa': 0}
```

---






## in API format
[![itspacchu/APIs - GitHub](https://gh-card.dev/repos/itspacchu/APIs.svg)](https://github.com/itspacchu/APIs)
<br>
<br>
## [Live Website](http://api.itspacchu.tk/results)

