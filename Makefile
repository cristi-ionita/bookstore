COLOR_RESET  := \033[0m
COLOR_GREEN  := \033[32m
COLOR_YELLOW := \033[33m

MAX_NAME_WIDTH := 20

help:
	@echo "$(COLOR_YELLOW)Available targets:$(COLOR_RESET)"
	@awk -v width=$(MAX_NAME_WIDTH) '\
		/^[a-zA-Z0-9_-]+:/ { \
			split($$0, desc, "##"); \
			if (length(desc) > 1) { \
				split($$1, tgt, ":"); \
				printf "$(COLOR_GREEN)%-*s$(COLOR_RESET)  %s\n", width, tgt[1], desc[2]; \
			} \
		}' $(MAKEFILE_LIST)

install_precommit:
	@echo "$(COLOR_GREEN)Installing pre-commit hooks...$(COLOR_RESET)"
	poetry run pre-commit install

run_precommit:
	@echo "$(COLOR_GREEN)Running pre-commit checks...$(COLOR_RESET)"
	poetry run pre-commit run --all-files

run:
	uvicorn book_store.app:app --reload

.PHONY: test

test:
	pytest -v

.PHONY: black

black:
	black .
