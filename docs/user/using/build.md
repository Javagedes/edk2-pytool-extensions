# Building a Platform using Stuart

To take your firmware code tree from freshly cloned to fully built, you only
need to execute three commands. If you've properly [installed](install.md)
edk2-pytool-extensions, then these commands will be available to execute as
seen below:

```cmd
stuart_setup -c path/to/SettingsFile.py
stuart_update -c path/to/SettingsFile.py
stuart_build -c path/to/SettingsFile.py
```

!!! tip
    Review your platform's instructions as it is common to install any
    additional python requirements via the command
    `pip install --upgrade -r pip-requirements.txt`, where pip-requirements.txt
    contains the necessary python requirements.

Stuart provides platforms the ability to customize it's build via command
flags. Due to this **Your platform's build instructions is the single
source of truth.**

!!! tip
    Once you've run `stuart_setup` and `stuart_update`, building your platform
    again is as simple as executing `stuart_build -c path/to/SettingsFile.py`.

As you can see, Each of these commands has a single required flag `-c` that
points towards a platform's settings file. This is a python file that is
typically located in the same directory as the platform's DSC file, however
**refer to your platform's build instructions for the exact name and location
of this file.**

!!! tip
    Common to most command line tools, you can use `-h, --help` on any of
    the commands to find any options. Using it with stuart_build can be
    particularly useful as it will provide you with common env variable
    overrides to customize the build: `stuart_build -c <filepath> --help`

Curious about what each command does? Check out the below sections.

## stuart_setup

Stuart_setup is responsible for downloading all git submodule dependencies as
specified by your platform.

```cmd
stuart_setup -c path/to/SettingsFile.py
```

## stuart_update

Stuart_update is responsible for downloading all other required external
dependencies, including, but not limited to nuget, azure, etc.

```cmd
stuart_update -c path/to/SettingsFile.py
```

## stuart_build

Stuart_build is responsible for building the platform and placing all artifacts
in the /Build/ directory. **Refer to your platform's build instructions for any
additional build flags needed to build.**

```cmd
stuart_build -c path/to/SettingsFile.py
```

As mentioned previously, using the `-h, --help` flag can be particularly useful
as it will provide you with common env variable overrides to customize the build.

```cmd
stuart_build -c path/to/SettingsFile.py --help
```

## FAQ

### Can I pass build values through stuart to the build command?

Yes! Build values can be set and passed to the build command via the command
line or from within your platform build file
[Read More](../integrate/build.md#setting-getting-environment-variables).
You define a build value via `BLD_*_<VAR>=<VALUE>` for all builds,
`BLD_DEBUG_<VAR>=VALUE` for debug builds, and `BLD_RELEASE_<VAR>=VALUE` for release
builds.

Non-valued build defines are also supported! Simply follow the above nomenclature
without providing a value i.e. `VLD_*_<VAR>`

From the command line:

```cmd
\> stuart_build -c Platforms/QemuQ35Pkg/PlatformBuild.py BLD_*_SHIP_MODE=FALSE
\> stuart_build -c Platforms/QemuQ35Pkg/PlatformBuild.py BLD_*_E1000_ENABLE
```

From within the Platform build file:

``` python
def SetPlatformEnv(self):
    ...
    self.env.SetValue("BLD_*_SHIP_MODE", "FALSE", "Default")
    self.env.SetValue("BLD_*_E1000", None, "Default")
    ...
```
