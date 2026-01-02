# AWS-Serverless-csv-project
AWS Serverless CSV Processing Pipeline
A serverless data processing project built using AWS S3, AWS Lambda, and IAM. This pipeline automatically triggers a Lambda function whenever a CSV file is uploaded to an S3 bucket, processes the data, and stores the transformed output back into S3. The project demonstrates event-driven architecture, IAM role-based access control, and real-time data processing using AWS Serverless Services.


<img width="1600" height="900" alt="Untitled design(1)" src="https://github.com/user-attachments/assets/a4d2d2b5-067b-46ae-b327-001d937f0143" />


User uploads CSV file
        ↓
AWS S3 Bucket (Input)
        ↓
S3 Event Trigger
        ↓
AWS Lambda Function (Python)
        ↓
IAM Role (Permissions: S3 Read/Write, CloudWatch Logs)
        ↓
CSV Data Processing (Read, Transform, Validate)
        ↓
Processed Output Stored in S3 (Output Bucket)
        ↓
Logs & Monitoring via CloudWatch
