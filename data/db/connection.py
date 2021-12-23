from boto3 import resource

from data.constants import DB_ENDPOINT_URL


def get_connection() -> resource:
    return resource('dynamodb', endpoint_url=DB_ENDPOINT_URL)
