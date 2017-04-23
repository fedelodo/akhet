.PHONY: all
all: repl

.PHONY: repl
repl:
	docker image build \
		-t akhet/sys/base:latest \
	 	akhet/sys/base/
	docker image build \
		-t akhet/sys/api:latest \
	  akhet/sys/api/
	docker image build \
		-t akhet/sys/agent:latest \
		akhet/sys/agent/
	docker image build \
		-t akhet/sys/proxy:latest \
		akhet/sys/proxy/

.PHONY: demoui
demoui:
	docker image build \
		-t akhet/demo/ui:latest \
		akhet/demo/ui/

.PHONY: base
base:
	docker image build \
		-t akhet/base/image-ubuntu-16-04:latest \
		akhet/base/image-ubuntu-16-04/
	docker image build \
		-t akhet/base/firewall:latest	\
		akhet/base/firewall/

.PHONY: xterm
xterm:
	docker image build \
		-t akhet/images/ubuntu-16-04-xterm:latest \
		akhet/images/ubuntu-16-04-xterm/


.PHONY: gnome-base
gnome-base:
	docker image build \
		-t akhet/images/ubuntu-16-04-gnome:latest \
		akhet/images/ubuntu-16-04-gnome/

.PHONY: gnome-dev
gnome-dev:
	docker image build \
		-t akhet/images/ubuntu-16-04-gnome-cpp:latest \
		akhet/images/ubuntu-16-04-gnome-cpp/
	docker image build \
		-t akhet/images/ubuntu-16-04-gnome-r-lang:latest \
		akhet/images/ubuntu-16-04-gnome-r-lang/

.PHONY: gnome-science
gnome-science:
	docker image build \
		-t akhet/images/ubuntu-16-04-gnome-root6:latest \
		akhet/images/ubuntu-16-04-gnome-root6/
	docker image build \
		-t akhet/images/ubuntu-16-04-gnome-geant4:latest \
		akhet/images/ubuntu-16-04-gnome-geant4/


.PHONY: plasma-base
plasma-base:
	docker image build \
		-t akhet/images/ubuntu-16-04-plasma:latest \
		akhet/images/ubuntu-16-04-plasma/

.PHONY: plasma-dev
plasma-dev:
	docker image build \
		-t akhet/images/ubuntu-16-04-plasma-cpp:latest \
		akhet/images/ubuntu-16-04-plasma-cpp/
	docker image build \
		-t akhet/images/ubuntu-16-04-plasma-r-lang:latest \
		akhet/images/ubuntu-16-04-plasma-r-lang/

.PHONY: plasma-science
plasma-science:
	docker image build \
		-t akhet/images/ubuntu-16-04-plasma-root6:latest \
		akhet/images/ubuntu-16-04-plasma-root6/
	docker image build \
		-t akhet/images/ubuntu-16-04-plasma-geant4:latest \
akhet/images/ubuntu-16-04-plasma-geant4/
