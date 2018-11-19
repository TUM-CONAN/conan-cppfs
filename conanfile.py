import os
import shutil
from conans import ConanFile, tools, CMake


class rttrConan(ConanFile):
    name = "cppfs"
    version = "1.2.0"
    license = "MIT License"
    homepage = "https://www.github.com/cginternals/cppfs"
    description = """rttr project"""
    url = "https://github.com/ulricheck/conan-cppfs"

    generators = "cmake"

    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        }

    default_options = (
        "shared=True", 
    )

    scm = {
        "type": "git",
        "subfolder": "cppfs",
        "url": "https://github.com/cginternals/cppfs.git",
        # "revision": "rttrorg-rttr-%s"% version
        "revision": "v1.2"
     }


    def build(self):
        cmake = CMake(self)
        cmake.definitions["DBUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(source_dir='cppfs')
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cppfs_d"] if self.settings.build_type == "Debug" else ["cppfs"]
