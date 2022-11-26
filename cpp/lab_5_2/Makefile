PRO_DIR     := .
PROJ_NAME   := lab_5_2
BUILD       :=  build
$(shell mkdir -p $(BUILD))

BUILD_DIR   := $(PRO_DIR)/$(BUILD)
INC_DIR     := $(PRO_DIR)/inc
SRC_DIR     := $(PRO_DIR)/src

CXX         := g++
CXX11       := -std=c++11
CXXFLAGS        += $(GDB_OPT) -Wall

GDB_OPT     := -g

#include
-include makefile.mk

SOURCE_CXX      += $(notdir $(SRC_CXX_PATH))
OBJ     += $(patsubst %.cpp, $(BUILD_DIR)/%.o, $(SOURCE_CXX))

TARGET  := $(BUILD_DIR)/$(PROJ_NAME)


.PHONY: all
all: $(TARGET)
	file $<
	@echo "finished."

$(TARGET): $(OBJ)
#   $(CC) $(C99) $^ -o $@
	$(CXX) $(CXX11) $^ -o $@
	
$(BUILD_DIR)/%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

    
run:
	$(TARGET)
debug:
	gdb $(TARGET)

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR) folder
	@echo "Clean done"
    
print-%:
	@echo $($(subst print-,,$@))