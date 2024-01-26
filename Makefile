OPTS:= -it --network ex3_dev_containers_default ex3_dev_containers-gnd

up:
	docker compose up -d --build

down:
	docker compose down -v

gnd:
	docker run $(OPTS) /app/gnd.py

gnd-sh:
	docker run $(OPTS) /bin/sh

sub:
	docker compose logs sub -f


.PHONY:
	up down gnd gnd-sh sub
