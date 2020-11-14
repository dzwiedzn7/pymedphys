# Copyright (C) 2020 Simon Biggs

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import pathlib
import re
import subprocess
import textwrap

from pymedphys._imports import black, tomlkit

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent.parent
PYPROJECT_TOML_PATH = REPO_ROOT.joinpath("pyproject.toml")

LIBRARY_PATH = REPO_ROOT.joinpath("lib", "pymedphys")
DOCS_PATH = LIBRARY_PATH.joinpath("docs")

VERSION_PATH = LIBRARY_PATH.joinpath("_version.py")

DIST_DIR = REPO_ROOT.joinpath("dist")
SETUP_PY = REPO_ROOT.joinpath("setup.py")

REQUIREMENTS_TXT = REPO_ROOT.joinpath("requirements.txt")
REQUIREMENTS_DEV_TXT = REPO_ROOT.joinpath("requirements-dev.txt")
REQUIREMENTS_USER_TXT = REPO_ROOT.joinpath("requirements-deploy.txt")

ROOT_PYLINT = REPO_ROOT.joinpath(".pylintrc")
LIBRARY_PYLINT = LIBRARY_PATH.joinpath(".pylintrc")

ROOT_README = REPO_ROOT.joinpath("README.rst")
DOCS_README = DOCS_PATH.joinpath("README.rst")

ROOT_CHANGELOG = REPO_ROOT.joinpath("CHANGELOG.md")
DOCS_CHANGELOG = DOCS_PATH.joinpath("CHANGELOG.md")

AUTOGEN_MESSAGE = [
    "# DO NOT EDIT THIS FILE!",
    "# This file has been autogenerated by `pymedphys dev propagate`",
]


def propagate_all(_):
    propagate_version()
    propagate_extras()
    propagate_requirements()
    propagate_pylintrc()
    propagate_readme()
    propagate_changelog()


def read_pyproject():
    with open(PYPROJECT_TOML_PATH) as f:
        pyproject_contents = tomlkit.loads(f.read())

    return pyproject_contents


def get_version_string():
    pyproject_contents = read_pyproject()
    version_string = pyproject_contents["tool"]["poetry"]["version"]

    return version_string


def propagate_version():
    version_string = get_version_string()
    version_list = re.split(r"[-\.]", version_string)

    for i, item in enumerate(version_list):
        try:
            version_list[i] = int(item)
        except ValueError:
            pass

    version_contents = textwrap.dedent(
        f"""\
        {AUTOGEN_MESSAGE[0]}
        {AUTOGEN_MESSAGE[1]}

        version_info = {version_list}
        __version__ = "{version_string}"
        """
    )

    version_contents = black.format_str(version_contents, mode=black.FileMode())

    with open(VERSION_PATH, "w") as f:
        f.write(version_contents)


def copy_file_with_autogen_message(
    original_path, target_path, comment_syntax=("# ", "")
):
    with open(original_path) as f:
        original_contents = f.read()

    new_autogen = [
        comment_syntax[0] + original_autogen[2::] + comment_syntax[1]
        for original_autogen in AUTOGEN_MESSAGE
    ]

    contents_with_autogen_warning = "\n".join(new_autogen) + "\n\n" + original_contents

    with open(target_path, "w+") as f:
        f.write(contents_with_autogen_warning)


def propagate_pylintrc():
    copy_file_with_autogen_message(ROOT_PYLINT, LIBRARY_PYLINT)


def propagate_readme():
    copy_file_with_autogen_message(ROOT_README, DOCS_README, ("..\n    ", ""))


def propagate_changelog():
    copy_file_with_autogen_message(ROOT_CHANGELOG, DOCS_CHANGELOG, ("<!-- ", " -->"))


def propagate_requirements():
    subprocess.check_call("poetry update pymedphys", shell=True)
    subprocess.check_call(
        "poetry export --without-hashes -E docs -E user -f requirements.txt --output requirements.txt",
        shell=True,
    )
    subprocess.check_call(
        "poetry export --without-hashes -E dev -f requirements.txt --output requirements-dev.txt",
        shell=True,
    )

    # TODO: Once the hashes pinning issue in poetry is fixed, remove the
    # --without-hashes. See <https://github.com/python-poetry/poetry/issues/1584>
    # for more details.
    subprocess.check_call(
        "poetry export --without-hashes -E user -E tests -f requirements.txt --output requirements-deploy.txt",
        shell=True,
    )

    with open(REQUIREMENTS_TXT, "a") as f:
        f.write(".[user,docs]\n")

    with open(REQUIREMENTS_DEV_TXT, "a") as f:
        f.write(".[dev]\n")


def propagate_extras():
    pyproject_contents = read_pyproject()

    deps = pyproject_contents["tool"]["poetry"]["dependencies"]

    extras = {}

    for key in deps:
        value = deps[key]
        comment = value.trivia.comment

        if comment.startswith("# groups"):
            split = comment.split("=")
            assert len(split) == 2
            groups = json.loads(split[-1])

            for group in groups:
                try:
                    extras[group].append(key)
                except KeyError:
                    extras[group] = [key]

    if pyproject_contents["tool"]["poetry"]["extras"] != extras:
        pyproject_contents["tool"]["poetry"]["extras"] = extras

        with open(PYPROJECT_TOML_PATH, "w") as f:
            f.write(tomlkit.dumps(pyproject_contents))
