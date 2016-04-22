import logging
import os

from src.controller.constants.constants_dto import ConstantsDTO


class ConstantsFactory():

    @staticmethod
    def get_constants_dto(enviroment=None):
        if enviroment=="development":
            return ConstantsFactory.__get_development_constants()
        elif enviroment=="production":
            return ConstantsFactory.__get_production_constants()
        else:
            return None

    @staticmethod
    def __get_production_constants():
        return ConstantsDTO(
            transaction_endpoint ="/transactions",
            log_endpoint ="/logs",
            health_endpoint ="/health",
            status_endpoint ="/status",
            homepage_endpoint ="/",
            divider =100,
            positive_remainders =[10,11,12,13,14,15],
            random_sleep_bounds_ms =(10,100),
            log_file ="./src/controller/logs/processing_node.log",
            default_loggin_level =logging.INFO,
            fraudulent_codes =[1,2,3,4,5],
            legit_code =0,
            eureka_heartbeat_interval = 15,
            eureka_host= os.environ.get("EUREKA_SERVICE_SERVICE_HOST"),
            eureka_port=int(os.environ.get("EUREKA_SERVICE_SERVICE_PORT")),
            eureka_app_name ="Processing",
            output_handler_app_name ="OutputHandler",
            output_handler_endpoint ="/transactions",
            processing_host = os.environ.get("MS_PROCESSING_SERVICE_SERVICE_HOST"),
            processing_port = int(os.environ.get("MS_PROCESSING_SERVICE_SERVICE_PORT")),
        )

    @staticmethod
    def __get_development_constants():
                return ConstantsDTO(
            transaction_endpoint ="/transactions",
            log_endpoint ="/logs",
            health_endpoint ="/health",
            status_endpoint ="/status",
            homepage_endpoint ="/",
            divider =100,
            positive_remainders =[10,11,12,13,14,15],
            random_sleep_bounds_ms =(10,100),
            log_file ="./src/controller/logs/processing_node.log",
            default_loggin_level =logging.INFO,
            fraudulent_codes =[1,2,3,4,5],
            legit_code =0,
            eureka_heartbeat_interval = 15,
            eureka_host= "192.168.56.102",
            eureka_port=8080,
            eureka_app_name ="Processing",
            output_handler_app_name ="OutputHandler",
            output_handler_endpoint ="/transactions",
            processing_host = "localhost",
            processing_port = 9991
        )






