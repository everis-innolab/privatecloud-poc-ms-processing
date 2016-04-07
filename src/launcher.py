import sys
import os
sys.path.append(os.getcwd())
import constants
from controller.logs.logger_factory import LoggerFactory
from eurekalab.client import EurekaClient
from constants import *
from controller.endpoint_handlers.processing_endpoint_handler import \
    ProcessingEndpointHandler
from controller.eureka_agent import EurekaAgent
from controller.service_runner import ServiceRunner
from src.controller.eureka_properties_factory import EurekaPropertiesFactory


class Main():

    def __init__(self, logger, eureka_server_dto, my_app_instace_dto):
        eureka_client = EurekaClient(eureka_server_dto, my_app_instace_dto)
        self.__eureka_agent = EurekaAgent(eureka_client, logger)

        #Pre cargamos la cache de url al inicio
        self.__eureka_agent.get_output_handler_url()
        self.__my_app_instance_dto = my_app_instace_dto

    def launch_server(self):
        try:
            my_handler = ProcessingEndpointHandler(self.__eureka_agent, logger)
            wiring = [
                    (TRANSACTION_ENDPOINT, "POST",my_handler.transactions_post)
                ]
            runner = ServiceRunner(my_handler, wiring, self.__eureka_agent)
            runner.start()
        finally:
            self.__eureka_agent.de_register_in_eureka()
            logger.info("De-register in eureka")

if __name__ == "__main__":

    # Lanzar con WorkingDirectory en ms-cloud\python\ProcessingNode
    logger = LoggerFactory.get_logger(
        constants.LOG_FILE, constants.DEFAULT_LOGGIN_LEVEL
    )

    factory = EurekaPropertiesFactory()

    if "--develop" in sys.argv or "--development" in sys.argv:
        eureka_dto = factory.get_development_eureka_server_dto()
        my_app_dto = factory.get_development_app_instance_dto()
        logger.info("Launching Processing service in development mode")
    else:
        eureka_dto = factory.get_eureka_server_dto()
        my_app_dto = factory.get_app_instance_dto()
        logger.info("Launching Processing service")

    main_launcher = Main(logger, eureka_dto, my_app_dto)
    main_launcher.launch_server()




