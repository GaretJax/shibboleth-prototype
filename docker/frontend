FROM centos:latest
MAINTAINER Jonathan Stoppani "jonathan.stoppani@wsfcomp.com"

# Setup environment
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

ADD http://download.opensuse.org/repositories/security://shibboleth/CentOS_7/security:shibboleth.repo /etc/yum.repos.d/shibboleth.repo

# Update the system and add additional sources
RUN /usr/bin/yum update -y

# Install apache
RUN /usr/bin/yum install -y shibboleth.x86_64 httpd
RUN /usr/bin/yum install -y mod_wsgi python-setuptools
RUN /usr/bin/easy_install pip
RUN /usr/bin/pip install flask
RUN /usr/sbin/useradd www

EXPOSE 80

# Configure webserver
ADD contrib/start.sh /usr/bin/runserver
RUN chmod +x /usr/bin/runserver
ADD contrib/mime.types /etc/httpd/conf/mime.types
ADD contrib/httpd.conf /etc/httpd/conf/httpd.conf
ADD contrib/sp2config.xml /etc/shibboleth/shibboleth2.xml
RUN chmod 644 /etc/shibboleth/shibboleth2.xml
ADD contrib/shib.conf /etc/httpd/conf.d/shib.conf

CMD ["/usr/bin/runserver"]
