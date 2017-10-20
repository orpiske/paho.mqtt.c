VERSION=1.2.0

check:
	rpmlint -i dist/paho-c.spec

rpm-prep:
	mkdir -p ${HOME}/rpmbuild/SOURCES/
	tar --transform="s/\./paho.mqtt.c-${VERSION}/" -cf ${HOME}/rpmbuild/SOURCES/v${VERSION}.tar.gz --exclude=./build.paho --exclude=.git --exclude=*.bz ./ --gzip

rpm-submit:
	mkdir -p ${HOME}/rpmbuild/SOURCES/
	wget -c https://github.com/eclipse/paho.mqtt.c/archive/v${VERSION}.tar.gz -O ${HOME}/rpmbuild/SOURCES/v${VERSION}.tar.gz

rpm-local: rpm-prep
	rpmbuild -ba dist/paho-c.spec

rpm-release: rpm-submit
	rpmbuild -ba dist/paho-c.spec

rpm: rpm-release
