# Installing and Setting up Stuart

Stuart is a powerful command line interface (CLI) and core feature of the
python package [edk2-pytool-extensions](https://pypi.org/project/edk2-pytool-extensions/).
It provides a simple and easy way to build and maintain an Edk2 based UEFI
Firmware code tree.

This section goes into how to install stuart, how to build a platform with
stuart, and how to perform continuous integration (CI) on a project with
stuart.

!!! note
        It is suggested to use python virtual environments to avoid dependency
        pollution and conflicts.
        [Read More](https://docs.python.org/3/library/venv.html)

## Installing on Windows

1. Ensure the latest version of [Python3](https://www.python.org/downloads/) is
installed on your system.

1. Ensure git 2.36.0 or greater is installed

1. Install edk2-pytool-extensions:

    ```cmd
    pip install --upgrade edk2-pytool-extensions
    ```

## Installing on Linux

If using WSL, review
[Getting Started with WSL](../features/using_linux.md#getting-started-with-wsl).

1. Ensure the latest version of
[Python3](https://www.python.org/downloads/) is installed on your system.

    ```cmd
    sudo apt install python3, python3-pip, python3-venv
    ```

1. Ensure git 2.36.0 or greater is installed

1. Install Nuget and dependencies:

    ```cmd
    sudo apt-get install mono-complete, nuget, make
    ```

1. Install edk2-pytool-extensions:

    ```cmd
    pip install --upgrade edk2-pytool-extensions
    ```

## Summary

That's it, you are ready to go!

[Click Here](build.md) to learn how to build a platform with Stuart.

[Click Here](ci.md) to learn how to perform platform CI with Stuart.
