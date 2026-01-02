# AWS-Serverless-csv-project
AWS Serverless CSV Processing Pipeline
A serverless data processing project built using AWS S3, AWS Lambda, and IAM. This pipeline automatically triggers a Lambda function whenever a CSV file is uploaded to an S3 bucket, processes the data, and stores the transformed output back into S3. The project demonstrates event-driven architecture, IAM role-based access control, and real-time data processing using AWS Serverless Services.


<img width="1600" height="900" alt="Untitled design(3)" src="https://github.com/user-attachments/assets/cb7d1074-4aac-448f-9458-3573f0a373a1" />


**Project Workflow**

User uploads a CSV file to an S3 bucket  
→ S3 event triggers a Lambda function  
→ Lambda uses IAM role permissions  
→ CSV file is processed using Python  
→ Transformed data is stored back in S3  
→ Execution logs are captured in CloudWatch

**CloudWatch**
<img width="1600" height="900" alt="Cloudwatch" src="https://github.com/user-attachments/assets/06c7e07c-ed5e-4126-b925-a4597ce9fe1d" />
