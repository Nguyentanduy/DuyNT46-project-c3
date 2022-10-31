import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    # postgres://user:pass@example.com:5432/dbname'
    DEBUG = True
    POSTGRES_URL="duynt46-postgre-db.postgres.database.azure.com:5432"  #TODO: Update value
    POSTGRES_USER="db@duynt46-postgre-db" #TODO: Update value
    POSTGRES_PW="Tanduy2510!"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgres://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://duynt46-servicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=Bq9SBjXqCoEXZw9x5IDepDGEhs20xMl56IevmAp5fwk=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False