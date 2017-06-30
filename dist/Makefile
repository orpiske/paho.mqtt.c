VERSION?=1.2.0
BUILD?=0

rpm-prep:
	mkdir -p ${HOME}/rpmbuild/SOURCES/
	tar --transform="s/\./paho-c-${VERSION}/" -cf ${HOME}/rpmbuild/SOURCES/paho-c-${VERSION}.tar.gz --exclude=./build.paho --exclude=.git --exclude=*.bz ./ --gzip

rpm: rpm-prep
	rpmbuild -ba --define "_user_defined_version ${VERSION}" --define "_user_defined_build ${BUILD}" dist/paho-c.spec
