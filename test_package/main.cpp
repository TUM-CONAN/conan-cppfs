#include <iostream>
#include <string>

#include <cppfs/fs.h>
#include <cppfs/FileHandle.h>

using namespace cppfs;

int main(){
    std::string path(".");
    FileHandle dir = fs::open(path);

    if (dir.isDirectory())
    {
        for (FileIterator it = dir.begin(); it != dir.end(); ++it)
        {
            std::string path = *it;
        }
    }

	return 0;
}