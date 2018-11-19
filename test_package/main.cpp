#include <iostream>
#include <string>

#include <cppfs/fs.h>
#include <cppfs/FileHandle.h>

using namespace cppfs;

int main(){
    std::string path(".");
    FileHandle dir = fs::open(path);

	return 0;
}