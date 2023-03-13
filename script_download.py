from boto3.session import Session
session = Session()
s3 = session.resource("s3")
bucket = s3.Bucket(meadocumentsbucket43148-aigprod)

for fileobj in bucket.objects.all():
        if` fileobj`.last_modified.month == "September" \
                and fileobj.last_modified.year == 2022 \
                              and fileobj.key.endswith("pdf"):
           command = ["aws", "s3",
                       "cp",
                       f'"s3://{meadocumentsbucket43148-aigprod}/{fileobj.key}"',
                       f"{meadocumentsbucket43148-aigprod}/{month}/"]
          os.system(" ".join(command))