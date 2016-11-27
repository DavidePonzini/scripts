#include <fstream>
#include <string>
#include <iostream>

using namespace std;

struct cell {
	string content;
	cell* next;
};

bool read_file(const string&, cell*&);
void write_file(const string&, cell*);
void write_screen(cell*);

bool write_to_stdout = false;

cell* list;
cell* aux1;
cell* aux2;
cell* aux2_old;

unsigned int words_left = 0;

int main(int arg_c, char** arg_v) {
	if(arg_c == 1) {
		if(!write_to_stdout)
			cout	<< "Removes all duplicate entries from a file, leaving only the first occurrence." << endl
				<< "Usage:" << endl
				<< "\tremove-duplicates <file1> [<file2> <file3> ...]" << endl;
		return 200;
	}

	for(int i = 1; i < arg_c; i++) {
		list = NULL;

		if(read_file(arg_v[i], list)) {
			if(!write_to_stdout)
				cout << "Beginning convertion of file " << arg_v[i] << "..." << endl;

			if(list != NULL && list -> next != NULL) {
				aux1 = list;

				while(aux1 -> next != NULL) {
					if(!write_to_stdout) {
						words_left--;
						cout << "\rWords remaining: " << words_left << flush;
					}

					aux2 = aux1 -> next;
					aux2_old = aux1;

					while(aux2 != NULL) {
						if(aux1 -> content.compare(aux2 -> content) == 0) {
							aux2_old -> next = aux2 -> next;
							delete aux2;

							if(aux2_old == NULL)
								aux2 = NULL;
							else
								aux2 = aux2_old -> next;
							words_left--;
						} else {
							aux2_old = aux2_old -> next;
							aux2 = aux2 -> next;
						}
					}
					aux1 = aux1 -> next;
				}

				if(!write_to_stdout) {
					write_file(arg_v[i], list);
					cout << endl << "File " << arg_v[i] << " converted." << endl << endl;
				} else
					write_screen(list);
			} else if(!write_to_stdout)
				cout << "There is no need to convert file " << arg_v[i] << "." << endl;
		}
	}
	return 0;
}

bool read_file(const string& name, cell*& list) {
	if(!write_to_stdout)
		cout << "Loading file: " << name << "... " << flush;

	ifstream file(name.c_str());
	if(!file) {
		if(!write_to_stdout)
			cout << "file does not exist." << endl << flush;
		return false;
	}

	string s;
	cell* aux;

	while(file) {
		getline(file, s);
		if(s.compare("") != 0) {
			cell* nc = new cell;
			nc -> content = s;
			nc -> next = NULL;
			if(list == NULL)
				list = nc;
			else
				aux -> next = nc;
			aux = nc;
			words_left++;
		}
	}
	file.close();

	if(!write_to_stdout)
		cout << "done." << endl << flush;
	return true;
}

void write_file(const string& name, cell* list) {
	cell* aux = list;
	ofstream file(name.c_str());
	while(aux != NULL) {
		file << aux -> content << endl;
		aux = aux -> next;
	}
	file.close();
}

void write_screen(cell* list) {
	cout << endl;
	cell* aux = list;
	while(aux) {
		cout << aux -> content << endl;
		aux = aux -> next;
	}
}
