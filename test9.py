from google.cloud import BigQuery
from google.cloud import bigquery
from google.oauth2 import service_account

key_path = "/path/to/service-account-key-file.json"
credentials = service_account.Credentials.from_service_account_file(key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])
client = bigquery.Client(credentials=credentials, project=credentials.project_id)


""" #プロジェクト名
zuu-infra
プロジェクト番号
259543728979
プロジェクト ID
zuu-infra
 """
