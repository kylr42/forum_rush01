RESET   := \033[0m
GREEN   := \033[0;32m
BROWN   := \033[0;33m
PURPLE  := \033[0;35m

all: up

up:
	@mkdir -p ./data/media
	@mkdir -p ./data/static
	@docker-compose -f docker-compose.yaml up --build
	@echo "${GREEN}Containers running...${RESET}"

down:
	@docker-compose -f docker-compose.yaml down
	@echo "${BROWN}Containers down success${RESET}"


clean:
	@docker stop $(docker ps -qa) 2>/dev/null || true;
	@docker rm $(docker ps -qa) 2>/dev/null || true;
	@docker rmi -f $(docker images -qa) 2>/dev/null || true;

fclean: clean
	@echo "${PURPLE}Docker cleaninig...${RESET}"
	@docker volume rm $(docker volume ls -q) 2>/dev/null || true;
	@docker network rm $(docker network ls -q) 2>/dev/null || true;

remove:
	@docker system prune -a --force
	@rm -rf ~/data

re: fclean all

.PHONY: all up down clean fclean remove re