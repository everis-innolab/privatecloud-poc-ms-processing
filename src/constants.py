## ENDPOINTS
import logging

TRANSACTION_ENDPOINT="/transactions"
LOG_ENDPOINT="/logs"
HEALTH_ENDPOINT="/health"
STATUS_ENDPOINT="/status"
HOMEPAGE_ENDPOINT="/"

## INTERNAL PARAMETERS
DIVIDER = 100
POSITIVE_REMAINDERS = [10,11,12,13,14,15]
RANDOM_SLEEP_BOUNDS_MS = (10,100)
LOG_FILE = "./src/controller/logs/processing_node.log"
DEFAULT_LOGGIN_LEVEL = logging.INFO
FRAUDULENT_CODES = [1,2,3,4,5]
LEGIT_CODE = 0

EUREKA_HEARTBEAT_INTERVAL = 25
EUREKA_APP_NAME = "Processing"

## EXTERNAL SERVICES PARAMETERS
OUTPUT_HANDLER_APP_NAME = "OutputHandler"
OUTPUT_HANDLER_ENDPOINT = "/transactions"

#Kubernetes Enviroment Variables
EUREKA_HOST_ENV = "EUREKA_SERVICE_SERVICE_HOST"
EUREKA_PORT_ENV = "EUREKA_SERVICE_SERVICE_PORT"
PROCESSING_HOST_ENV = "MS_PROCESSING_SERVICE_SERVICE_HOST"
PROCESSING_PORT_ENV = "MS_PROCESSING_SERVICE_SERVICE_PORT"


#Vlues to hard-code into env variables when launching in debug
DEV_EUREKA_HOST_ENV = "eureka-fd.cloud.everis.com"
DEV_EUREKA_PORT_ENV = "80"
DEV_PROCESSING_HOST_ENV = "localhost"
DEV_PROCESSING_PORT_ENV = "9991"
