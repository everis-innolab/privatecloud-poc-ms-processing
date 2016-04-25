import sys
import os
sys.path.append(os.getcwd())
from controller.constants.constants_factory import ConstantsFactory
from controller.logs.logger_factory import LoggerFactory
from eurekalab.client import EurekaClient
from controller.endpoint_handlers.processing_endpoint_handler import \
    ProcessingEndpointHandler
from controller.eureka_agent import EurekaAgent
from controller.service_runner import ServiceRunner
from controller.eureka_properties_factory import EurekaPropertiesFactory


class Main():

    def __init__(self, logger, eureka_server_dto, my_app_instace_dto,
                 constants_dto):

        eureka_client = EurekaClient(eureka_server_dto, my_app_instace_dto)
        self.__eureka_agent = EurekaAgent(eureka_client, logger, constants_dto)
        self.__constants_dto = constants_dto

        #We force a pre-load if the output handler url in the cache
        self.__eureka_agent.get_output_handler_url()
        self.__my_app_instance_dto = my_app_instace_dto

    def launch_server(self):
        try:
            my_handler = ProcessingEndpointHandler(
                self.__eureka_agent, logger, self.__constants_dto
            )

            wiring = [(
                self.__constants_dto.transaction_endpoint,
                "POST",
                my_handler.transactions_post
            )]
            runner = ServiceRunner(
                my_handler, wiring, self.__eureka_agent, False,
                self.__constants_dto
            )
            runner.start()
        finally:
            try:
                self.__eureka_agent.de_register_in_eureka()
                logger.info("De-register in eureka")
            except:
                logger.info("Could not De-register in eureka, probably the "
                            "instance was never registered")

if __name__ == "__main__":

    # Launch with WorkingDirectory in ms-cloud\python\ProcessingNode
    if "--develop" in sys.argv or "--development" in sys.argv:
        constants_dto = ConstantsFactory.get_constants_dto("development")
        logger = LoggerFactory.get_logger(
            constants_dto.log_file, constants_dto.default_loggin_level
        )
        logger.info("Launching Processing service in development mode")
    else:
        constants_dto = ConstantsFactory.get_constants_dto("production")
        logger = LoggerFactory.get_logger(
            constants_dto.log_file, constants_dto.default_loggin_level
        )
        logger.info("Launching Processing service")


    eureka_factory = EurekaPropertiesFactory(constants_dto)
    main_launcher = Main(
        logger,
        eureka_factory.get_eureka_server_dto(),
        eureka_factory.get_app_instance_dto(),
        constants_dto
    )
    main_launcher.launch_server()





