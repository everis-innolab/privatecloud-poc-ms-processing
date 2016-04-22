class ConstantsDTO(object):

    def __init__(self, transaction_endpoint=None, log_endpoint=None,
                 health_endpoint=None, status_endpoint=None,
                 homepage_endpoint=None, divider=None,
                 positive_remainders=None, random_sleep_bounds_ms=None,
                 log_file=None, default_loggin_level=None,
                 fraudulent_codes=None, legit_code=None,
                 eureka_heartbeat_interval=None, eureka_app_name=None,
                 output_handler_app_name=None, output_handler_endpoint=None,
                 eureka_host=None, eureka_port=None, processing_host=None,
                 processing_port=None):
        self.__transaction_endpoint = transaction_endpoint
        self.__log_endpoint = log_endpoint
        self.__health_endpoint = health_endpoint
        self.__status_endpoint = status_endpoint
        self.__homepage_endpoint = homepage_endpoint
        self.__divider = divider
        self.__positive_remainders = positive_remainders
        self.__random_sleep_bounds_ms = random_sleep_bounds_ms
        self.__log_file = log_file
        self.__default_loggin_level = default_loggin_level
        self.__fraudulent_codes = fraudulent_codes
        self.__legit_code = legit_code
        self.__eureka_heartbeat_interval = eureka_heartbeat_interval
        self.__eureka_app_name = eureka_app_name
        self.__output_handler_app_name = output_handler_app_name
        self.__output_handler_endpoint = output_handler_endpoint
        self.__eureka_host = eureka_host
        self.__eureka_port = eureka_port
        self.__processing_host = processing_host
        self.__processing_port = processing_port

##DC:==========================================================================
##DC: GETTERS
##DC:==========================================================================

    @property
    def transaction_endpoint(self):
        return self.__transaction_endpoint

    @property
    def log_endpoint(self):
        return self.__log_endpoint

    @property
    def health_endpoint(self):
        return self.__health_endpoint

    @property
    def status_endpoint(self):
        return self.__status_endpoint

    @property
    def homepage_endpoint(self):
        return self.__homepage_endpoint

    @property
    def divider(self):
        return self.__divider

    @property
    def positive_remainders(self):
        return self.__positive_remainders

    @property
    def random_sleep_bounds_ms(self):
        return self.__random_sleep_bounds_ms

    @property
    def log_file(self):
        return self.__log_file

    @property
    def default_loggin_level(self):
        return self.__default_loggin_level

    @property
    def fraudulent_codes(self):
        return self.__fraudulent_codes

    @property
    def legit_code(self):
        return self.__legit_code

    @property
    def eureka_heartbeat_interval(self):
        return self.__eureka_heartbeat_interval

    @property
    def eureka_app_name(self):
        return self.__eureka_app_name

    @property
    def output_handler_app_name(self):
        return self.__output_handler_app_name

    @property
    def output_handler_endpoint(self):
        return self.__output_handler_endpoint

    @property
    def eureka_host(self):
        return self.__eureka_host

    @property
    def eureka_port(self):
        return self.__eureka_port

    @property
    def processing_host(self):
        return self.__processing_host

    @property
    def processing_port(self):
        return self.__processing_port

##DC:==========================================================================
##DC: SETTERS
##DC:==========================================================================

    @transaction_endpoint.setter
    def transaction_endpoint(self, transaction_endpoint):
        self.__transaction_endpoint = transaction_endpoint

    @log_endpoint.setter
    def log_endpoint(self, log_endpoint):
        self.__log_endpoint = log_endpoint

    @health_endpoint.setter
    def health_endpoint(self, health_endpoint):
        self.__health_endpoint = health_endpoint

    @status_endpoint.setter
    def status_endpoint(self, status_endpoint):
        self.__status_endpoint = status_endpoint

    @homepage_endpoint.setter
    def homepage_endpoint(self, homepage_endpoint):
        self.__homepage_endpoint = homepage_endpoint

    @divider.setter
    def divider(self, divider):
        self.__divider = divider

    @positive_remainders.setter
    def positive_remainders(self, positive_remainders):
        self.__positive_remainders = positive_remainders

    @random_sleep_bounds_ms.setter
    def random_sleep_bounds_ms(self, random_sleep_bounds_ms):
        self.__random_sleep_bounds_ms = random_sleep_bounds_ms

    @log_file.setter
    def log_file(self, log_file):
        self.__log_file = log_file

    @default_loggin_level.setter
    def default_loggin_level(self, default_loggin_level):
        self.__default_loggin_level = default_loggin_level

    @fraudulent_codes.setter
    def fraudulent_codes(self, fraudulent_codes):
        self.__fraudulent_codes = fraudulent_codes

    @legit_code.setter
    def legit_code(self, legit_code):
        self.__legit_code = legit_code

    @eureka_heartbeat_interval.setter
    def eureka_heartbeat_interval(self, eureka_heartbeat_interval):
        self.__eureka_heartbeat_interval = eureka_heartbeat_interval

    @eureka_app_name.setter
    def eureka_app_name(self, eureka_app_name):
        self.__eureka_app_name = eureka_app_name

    @output_handler_app_name.setter
    def output_handler_app_name(self, output_handler_app_name):
        self.__output_handler_app_name = output_handler_app_name

    @output_handler_endpoint.setter
    def output_handler_endpoint(self, output_handler_endpoint):
        self.__output_handler_endpoint = output_handler_endpoint

    @eureka_host.setter
    def eureka_host(self, eureka_host):
        self.__eureka_host = eureka_host

    @eureka_port.setter
    def eureka_port(self, eureka_port):
        self.__eureka_port = eureka_port

    @processing_host.setter
    def processing_host(self, processing_host):
        self.__processing_host = processing_host

    @processing_port.setter
    def processing_port(self, processing_port):
        self.__processing_port = processing_port

    def __eq__(self, other):
        return (
            self.transaction_endpoint == other.transaction_endpoint and
            self.log_endpoint == other.log_endpoint and
            self.health_endpoint == other.health_endpoint and
            self.status_endpoint == other.status_endpoint and
            self.homepage_endpoint == other.homepage_endpoint and
            self.divider == other.divider and
            self.positive_remainders == other.positive_remainders and
            self.random_sleep_bounds_ms == other.random_sleep_bounds_ms and
            self.log_file == other.log_file and
            self.default_loggin_level == other.default_loggin_level and
            self.fraudulent_codes == other.fraudulent_codes and
            self.legit_code == other.legit_code and
            self.eureka_heartbeat_interval == other.eureka_heartbeat_interval and
            self.eureka_app_name == other.eureka_app_name and
            self.output_handler_app_name == other.output_handler_app_name and
            self.output_handler_endpoint == other.output_handler_endpoint and
            self.eureka_host == other.eureka_host and
            self.eureka_port == other.eureka_port and
            self.processing_host == other.processing_host and
            self.processing_port == other.processing_port
        )

    def __str__(self):
        return (
            'transaction_endpoint: %s\n'%str(self.__transaction_endpoint)+
            'log_endpoint: %s\n'%str(self.__log_endpoint)+
            'health_endpoint: %s\n'%str(self.__health_endpoint)+
            'status_endpoint: %s\n'%str(self.__status_endpoint)+
            'homepage_endpoint: %s\n'%str(self.__homepage_endpoint)+
            'divider: %s\n'%str(self.__divider)+
            'positive_remainders: %s\n'%str(self.__positive_remainders)+
            'random_sleep_bounds_ms: %s\n'%str(self.__random_sleep_bounds_ms)+
            'log_file: %s\n'%str(self.__log_file)+
            'default_loggin_level: %s\n'%str(self.__default_loggin_level)+
            'fraudulent_codes: %s\n'%str(self.__fraudulent_codes)+
            'legit_code: %s\n'%str(self.__legit_code)+
            'eureka_heartbeat_interval: %s\n'%str(self.__eureka_heartbeat_interval)+
            'eureka_app_name: %s\n'%str(self.__eureka_app_name)+
            'output_handler_app_name: %s\n'%str(self.__output_handler_app_name)+
            'output_handler_endpoint: %s\n'%str(self.__output_handler_endpoint)+
            'eureka_host: %s\n'%str(self.__eureka_host)+
            'eureka_port: %s\n'%str(self.__eureka_port)+
            'processing_host: %s\n'%str(self.__processing_host)+
            'processing_port: %s\n'%str(self.__processing_port)
        )