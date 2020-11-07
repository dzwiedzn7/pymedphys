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


import pymedphys


def test_dicom_trf_comparison():
    """Focusing on unique DICOM header cases.

    See <https://github.com/pymedphys/pymedphys/issues/1142> for more
    details regarding the use case.
    """

    testing_paths = pymedphys.zip_data_paths("dicom-trf-pairs.zip")

    dicom_paths = [path for path in testing_paths if path.suffix == ".dcm"]

    trf_paths = [path.with_suffix(".trf") for path in dicom_paths]

    for path in trf_paths:
        assert path.exists()
