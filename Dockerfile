FROM centos:7

# PROXY
WORKDIR "/tmp" &&\
RUN echo 'proxy=http://10.121.8.100:8080/' >> /etc/yum.conf 
ENV https_proxy="https://10.121.8.100:8080/" 
ENV http_proxy="http://10.121.8.100:8080/"



# YUM Updates and libraries
RUN yum update -y &&\
	yum install lapack-devel -y &&\
	yum install blas-devel -y &&\
	yum install gcc -y &&\
	yum install gcc-c++ -y &&\
	yum install python-devel -y &&\
	yum install net-tools -y &&\
	yum install wget -y 
	
# install pip
RUN echo 'use_proxy = on' >> ~/.wgetrc && \
	echo 'http_proxy = http://10.121.8.100:8080/' >> ~/.wgetrc && \
	echo 'https_proxy = https://10.121.8.100:8080/' >> ~/.wgetrc && \
	wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-1.4.2.tar.gz 

RUN tar -zxvf setuptools-1.4.2.tar.gz &&\
	python setuptools-1.4.2/setup.py install &&\
	easy_install pip

COPY . /tmp/ms-processing
COPY python-eureka-library /tmp/python-eureka-library

RUN cd /tmp/python-eureka-library/ && python setup.py install 
RUN pip install -r /tmp/ms-processing/requirements.txt

# El comando por defecto sera un interprete de Python
EXPOSE 9991
WORKDIR /tmp/ms-processing
ENTRYPOINT ["python"]
CMD ["src/launcher.py"]

# PARA CREAR LA IMAGEN:
# docker build -f Dockerfile .
