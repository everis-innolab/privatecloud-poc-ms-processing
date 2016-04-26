# -*- encoding: utf8 -*-
import os
import random
from threading import Thread, Event
import time
import datetime



class EurekaAgent():

    def __init__(self, ec_client, logger, constants_dto):
        self.ec_client = ec_client
        self.__constants_dto = constants_dto
        self.heart_beat_thread = None
        self.heart_beat_stop_flag = None
        self.__logger = logger
        self.__output_handler_url_cache = None
        self.__last_cache_refresh_time = None

    def get_output_handler_url(self):

        if self.__output_handler_url_cache is None or \
                self.__is_cache_refreshing_necessary():

            # # TODO reactivate when the kubernetes DNS issue is resolved
            # self.__logger.info("Getting Output Handler URL")
            # self.__logger.info("Getting APP Instance dto List")
            # instance_dto_list = self.ec_client.get_all_instaces_of_app(
            #     self.__constants_dto.output_handler_app_name
            # )
            #
            # self.__logger.info("Chosing Instance dto List")
            # if instance_dto_list is None or len(instance_dto_list)<1:
            #     self.__output_handler_url_cache = None
            #
            # instance_dto = random.choice(instance_dto_list)
            # self.__logger.info("Building URL from APP Instance dto List")
            # self.__output_handler_url_cache = \
            #     self.__get_url_from_app_instance_dto(instance_dto)
            #
            # self.__last_cache_refresh_time = datetime.datetime.now()


            self.__output_handler_url_cache = "http://%s:80/transactions"%\
                os.environ.get("MS_OUTPUT_SERVICE_SERVICE_HOST")
            self.__last_cache_refresh_time = datetime.datetime.now()

        return self.__output_handler_url_cache

    def __is_cache_refreshing_necessary(self):
        return datetime.datetime.now()-self.__last_cache_refresh_time > \
               datetime.timedelta(seconds=300)

    def __get_url_from_app_instance_dto(self, instance_dto):
        return  "http://%s:%s%s"%(
            instance_dto.host_name, str(instance_dto.port),
            self.__constants_dto.output_handler_endpoint
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
            self.heart_beat_stop_flag,
            self.__constants_dto.eureka_heartbeat_interval ,
            self.ec_client.heartbeat,
            self.__logger
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
