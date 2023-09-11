CC = clang++
CFLAGS += -fcolor-diagnostics -fansi-escape-codes -g -Og -Wall -pthread -pedantic
SANITIZER = -fsanitize=address -fsanitize=undefined

SRC = $(shell find . -name '*.cpp' -print)
OBJ = $(SRC:.cpp=.o)
DSYM = $(shell find . -name '*.dSYM' -print)
TRG = $(SRC:.cpp=)

all: $(TRG)

%: %.cpp
	@$(CXX) -c $< $(CXXFLAGS) -o $@.o $(SANITIZER)
	@$(CXX) $@.o $(CXXFLAGS) -o $@ $(SANITIZER)

clean:
	@rm -f $(TRG)
	@rm -f $(OBJ)
	@rm -rf $(DSYM)

.PHONY: all clean
