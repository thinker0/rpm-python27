# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
FROM centos:6

RUN yum install -y centos-release-scl
RUN yum update -y
RUN yum install -y \
    make \
    rpm-build \
    yum-utils \
    apr-devel \
    cyrus-sasl-devel \
    gcc \
    gcc-c++ \
    git \
    java-1.8.0-openjdk-devel \
    krb5-devel \
    libcurl-devel \
    patch \
    python \
    python-devel \
    subversion-devel \
    tar \
    unzip \
    wget \
    zlib-devel \
    bluez-libs-devel \
    bzip2-devel \
    expat-devel \
    gdbm-devel \
    gmp-devel \
    libdb-devel \
    ligGl-devel \
    libX11-devel \
    ncurses-devel \
    openssl-devel \
    readline-devel \
    sqlite-devel \
    systemtap-sdt-devel \
    tcl-devel \
    tix-devel \
    tk-devel \
    valgrint-devel \
    python-setuptools \
    python-pip \
    expat-devel \
    libdb-devel \
    libffi-devel \
    libGL-devel \
    valgrind-devel \
    python-pip \
    tree

ADD ./rpmbuild rpmbuild
ADD build.sh /build.sh
