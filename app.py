
from flask import Flask
import boto3

app = Flask(__name__)

@app.route("/")
def home():
    return "My AWS Web Application Running"

@app.route("/s3")
def s3():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()

    output = ""

    for bucket in buckets['Buckets']:
        output += bucket['Name'] + "<br>"

    return output

app.run(host="0.0.0.0", port=80)
