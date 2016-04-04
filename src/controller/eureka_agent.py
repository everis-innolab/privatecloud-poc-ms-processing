# -*- encoding: utf8 -*-
import random
from threading import Thread, Event
import time
from src.constants import EUREKA_HEARTBEAT_INTERVAL, OUTPUT_HANDLER_APP_NAME, \
    OUTPUT_HANDLER_ENDPOINT


class EurekaAgent():

    def __init__(self, ec_client, logger):
        self.ec_client = ec_client
        self.heart_beat_thread = None
        self.heart_beat_stop_flag = None
        self.__logger = logger

    def get_output_handler_url(self):

        instance_dto_list = \
            self.ec_client.get_all_instaces_of_app(OUTPUT_HANDLER_APP_NAME)

        if instance_dto_list is None or len(instance_dto_list)<1:
            return None

        instance_dto = random.choice(instance_dto_list)
        return self.__get_url_from_app_instance_dto(instance_dto)

    def __get_url_from_app_instance_dto(self, instance_dto):
        return  "http://%s:%s%s"%(
            instance_dto.host_name, str(instance_dto.port),
            OUTPUT_HANDLER_ENDPOINT
        )

    def register_in_eureka(self):
        self.ec_client.register()
        time.sleep(2)
        self.ec_client.take_back_to_service()
        time.sleep(2)
        self.__start_heartbeat_thread()

    def de_register_in_eureka(self):
        self.ec_client.de_register()
        self.__stop_heartbeat_thread()

    def __start_heartbeat_thread(self):
        self.heart_beat_stop_flag = Event()
        self.heart_beat_thread =  MyThread(
            self.heart_beat_stop_flag, EUREKA_HEARTBEAT_INTERVAL,
            self.ec_client.heartbeat, self.__logger
        )
        self.heart_beat_thread.start()

    def __stop_heartbeat_thread(self):
        self.heart_beat_stop_flag.set()


class MyThread(Thread):

    def __init__(self, event, time_interval_in_segs, function, logger):
        Thread.__init__(self)
        self.stopped = event
        self.time_interval_in_segs = time_interval_in_segs
        self.function = function
        self.logger = logger

    def run(self):
        while not self.stopped.wait(self.time_interval_in_segs):
            try:
                self.function()
            except:
                self.logger.exception("Error al enviar el heartBeat")
