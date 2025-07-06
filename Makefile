COLOR_RESET  := \033[0m
COLOR_GREEN  := \033[32m
COLOR_YELLOW := \033[33m

MAX_NAME_WIDTH := 20

help:
	@echo "$(COLOR_YELLOW)Available targets:$(COLOR_RESET)"
	@awk -v width=$(MAX_NAME_WIDTH) ' \
		/^[a-zA-Z0-9_-]+:/ { \
			split($$0, desc, "##"); \
			if (length(desc) > 1) { \
				printf "  $(COLOR_GREEN)%-*s$(COLOR_RESET) %s\n", width, $$1, desc[2]; \
			} \
		} \
	' $(MAKEFILE_LIST)

run_locally: ## Run the application
	@echo "$(COLOR_GREEN)Running the application...$(COLOR_RESET)"
	docker compose up --build db -d
	poetry run uvicorn book_store.app:app --host 127.0.0.1 --port 8000 --reload
	

run_in_docker: ## Run the application in Docker
	@echo "$(COLOR_GREEN)Running the application in Docker...$(COLOR_RESET)"
	docker compose up --build

install_precommit: ## Install pre-commit hooks
	@echo "$(COLOR_GREEN)Installing pre-commit hooks...$(COLOR_RESET)"
	poetry run pre-commit install