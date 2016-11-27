SRC = remove-duplicates.cpp
EXEC = remove-duplicates.exe

all: move

compile: $(SRC)
	g++ -Wall -std=c++11 -o $(EXEC) $(SRC)

run: compile
	./$(EXEC)

clean:
	rm -f $(EXEC)

move: compile
	mv $(EXEC) ../../$(EXEC)
