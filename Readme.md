# Loan Prediction: ชัชชาย จันทร์เพ็ชร์ 6210450059
---
อธิบาย folder
- model Analysis : เป็นไฟล์ ipynb ใช้สำหรับ อธิบาย dataset และ algorithms ที่นำมาใช้ในตัว app
- Report : ไฟล์จาก model Analysis ที่เป็น pdf และ silde ที่ใช้ในการpresent
- templates : หน้า html ที่ใช้ในเว็บ
---
นอก folder
- app.py : หน้า application หลักที่ใช้ในการ run
- model : ตัวmodel ไว้ใช้สำหรับ predict ค่า input จาก app.py
- procfile,requirements.txt : เอาไว้ใช้ในการ deploy
---
Note: ใช้ huroku ในการ deploy

Dataset: https://www.kaggle.com/kmldas/loan-default-prediction
---
web: https://bankloanpredictions.herokuapp.com/
---
## requirement
---
python : https://www.python.org/downloads/

flask : https://flask.palletsprojects.com/en/2.0.x/installation/
---
วิธี Run : ไปที่ app.py run คำสั่ง flask run
รายละเอียด : https://flask.palletsprojects.com/en/2.0.x/quickstart/