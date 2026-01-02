import csv
import boto3
import io

s3 = boto3.client('s3')

PROCESSED_BUCKET = "Bucket-Name"

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    csv_content = response['Body'].read().decode('utf-8')

    reader = csv.DictReader(io.StringIO(csv_content))
    processed_rows = []

    for row in reader:
        delay = int(row.get('delay_minutes', 0))

        if delay > 0:
            row['status'] = 'Delayed'
        else:
            row['status'] = 'On-Time'

        processed_rows.append(row)

    output_buffer = io.StringIO()
    writer = csv.DictWriter(output_buffer, fieldnames=processed_rows[0].keys())
    writer.writeheader()
    writer.writerows(processed_rows)

    output_file_name = f"processed-{file_name}"

    s3.put_object(
        Bucket=PROCESSED_BUCKET,
        Key=output_file_name,
        Body=output_buffer.getvalue()
    )

    return {
        "statusCode": 200,
        "message": "CSV processed successfully"
    }
