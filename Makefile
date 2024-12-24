# Variables genéricas
PROJECT_NAME := my_project           # Nombre del proyecto
SRC_DIR := src                       # Directorio de archivos fuente
BUILD_DIR := build                   # Directorio para archivos generados
DIST_DIR := dist                     # Directorio para distribución final
COMPORT := /dev/ttyACM0

# Definir comandos específicos según la tarea
PYTHON := python3                    # Intérprete Python
TEST_CMD := pytest                   # Comando para pruebas
LINTER := pylint                     # Linter para Python
ZIP_CMD := zip                       # Comando para empaquetar

# Variables para personalizar comportamientos
SRC_FILES := $(wildcard $(SRC_DIR)/*.py)  # Encuentra archivos fuente en src/
OUTPUT_FILE := $(DIST_DIR)/$(PROJECT_NAME).zip

# Reglas principales
.PHONY: all clean lint test build package

# Por defecto: compila y empaqueta
all: dev

# install dev deps
libinstall:
	@echo "installing ampy"
	pip install adafruit-ampy --break-system-packages

# run main on pico
dev:
	@echo "running main on picoboard on ${COMPORT}"
	ampy --port ${COMPORT} run main.py 

set_boothid:
	@echo "setting raspi pico as hid boot"
	ampy --port /dev/ttyACM0 put boot.hid.py boot.py 

set_boot:
	@echo "setting raspi pico as hid boot"
	ampy --port /dev/ttyACM0 put boot.normal.py boot.py 

# Regla para construir archivos (puedes personalizar este paso según el proyecto)
build:
	@echo "Construyendo archivos en $(BUILD_DIR)..."
	@mkdir -p $(BUILD_DIR)
	@cp $(SRC_FILES) $(BUILD_DIR)/
	@echo "Archivos construidos en $(BUILD_DIR)."

# Regla para ejecutar pruebas
test:
	@echo "Ejecutando pruebas..."
	$(TEST_CMD)
	@echo "Pruebas completadas."

# Regla para verificar estilo de código
lint:
	@echo "Analizando estilo de código con $(LINTER)..."
	$(LINTER) $(SRC_DIR)/*.py
	@echo "Análisis completado."

# Regla para empaquetar archivos
package: build
	@echo "Empaquetando proyecto en $(OUTPUT_FILE)..."
	@mkdir -p $(DIST_DIR)
	$(ZIP_CMD) -r $(OUTPUT_FILE) $(BUILD_DIR)/*
	@echo "Empaquetado completado: $(OUTPUT_FILE)."

# Regla para limpiar archivos generados
clean:
	@echo "Limpiando archivos generados..."
	@rm -rf $(BUILD_DIR) $(DIST_DIR)
	@echo "Archivos limpiados."


