import os
import shutil
from conans import ConanFile, tools, CMake


class rttrConan(ConanFile):
    name = "cppfs"
    version = "1.3.0"
    license = "MIT License"
    homepage = "https://www.github.com/cginternals/cppfs"
    description = """cppfs project"""
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
        "revision": "v%s" % version
     }


    def _cmake_configure(self):
        cmake = CMake(self)
        cmake.definitions["DBUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(source_dir='cppfs')
        return cmake

    def build(self):
        cmake = self._cmake_configure()
        cmake.build()

    def package(self):
        cmake = self._cmake_configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
