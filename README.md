# conan-rttr


[Conan.io](https://conan.io) package for [cppfs](https://github.com/cginternals/cppfs) project.

The packages generated with this *conanfile.py* .

## Basic setup

    $ conan install cppfs/1.2.0@camposs/testing

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    cppfs/1.2.0@camposs/testing

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)
