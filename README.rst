|logo|

.. |logo| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/pymedphys_title.png
    :target: https://docs.pymedphys.com/

.. START_OF_DOCS_IMPORT

**A community effort to develop an open standard library for Medical Physics
in Python. Building quality transparent software together via peer review
and open source distribution. Open code is better science.**

|streamlit| |build| |docs| |pypi| |python| |license|

.. |streamlit| image:: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
    :target: https://share.streamlit.io/pymedphys/pymedphys/main/app.py

.. |build| image:: https://img.shields.io/github/workflow/status/pymedphys/pymedphys/PullRequest
    :target: https://github.com/pymedphys/pymedphys/actions

.. |docs| image:: https://img.shields.io/netlify/c702e3b2-f436-46a3-b461-00a8a55bcdba
    :target: https://app.netlify.com/sites/pymedphys/deploys

.. |pypi| image:: https://img.shields.io/pypi/v/pymedphys
    :target: https://pypi.org/project/pymedphys/

.. |python| image:: https://img.shields.io/pypi/pyversions/pymedphys
    :target: https://pypi.org/project/pymedphys/

.. |license| image:: https://img.shields.io/pypi/l/pymedphys
    :target: https://choosealicense.com/licenses/apache-2.0/


What is PyMedPhys?
------------------

An open-source Medical Physics python library with a focus on being
a place to share, review, improve, and transparently learn off of each
other's code. It is inspired by the collaborative work of our physics peers
in astronomy and their `Astropy Project`_. PyMedPhys is available on `PyPI`_
and `GitHub`_.

.. _`Astropy Project`: http://www.astropy.org/
.. _`PyPI`: https://pypi.org/project/pymedphys/
.. _`GitHub`: https://github.com/pymedphys/pymedphys


Mailing list
------------

If you would like to dive into the community a great place to get started is
to sign up to `the mailing list`_ and say hi by introducing yourself with
where you're from, and what you hope to achieve with PyMedPhys.

.. _`the mailing list`: https://groups.google.com/g/pymedphys


Table of contents
-----------------

`Tutorials`_
........................

Get started with a hands-on introduction to PyMedPhys for beginners

`How-To guides`_
........................

Guides and recipes for common problems and tasks

`Reference`_
............................

Technical reference for the `library`_ (modules, functions and classes),
as well as the available `command line tools`_.

`Background`_
..............................

Explanation and discussion of key topics and concepts


Beta level of development
-------------------------

PyMedPhys is currently within the ``beta`` stage of its life-cycle. It will
stay in this stage until the version number leaves ``0.x.x`` and enters
``1.x.x``. While PyMedPhys is in ``beta`` stage, **no API is guaranteed to be
stable from one release to the next.** In fact, it is very likely that the
entire API will change multiple times before a ``1.0.0`` release. In practice,
this means that upgrading ``pymedphys`` to a new version will possibly break
any code that was using the old version of pymedphys. We try to be abreast of
this by providing details of any breaking changes from one release to the next
within the `Release Notes`_.

Our Team
--------

PyMedPhys is what it is today due to its maintainers and contributors both past
and present. Here is our team.

Maintainers
...........

* `Simon Biggs`_
    * `Riverina Cancer Care Centre`_, Australia

.. _`Simon Biggs`: https://github.com/SimonBiggs

* `Stuart Swerdloff`_
    * `ELEKTA Pty Ltd`_: New Zealand

.. _`Stuart Swerdloff`: https://github.com/sjswerdloff

|rccc| |sjs|

Active contributors
...................

* `Phillip Chlap`_
    * `University of New South Wales`_, Australia
    * `Ingham Institute`_, Australia

.. _`Phillip Chlap`: https://github.com/pchlap

* `Matthew Cooper`_

.. _`Matthew Cooper`: https://github.com/matthewdeancooper

* `Jake Rembish`_
    * `UT Health San Antonio`_, USA

.. _`Jake Rembish`: https://github.com/rembishj

* `Pedro Martinez`_
    * `University of Calgary`_, Canada
    * `Tom Baker Cancer Centre`_, Canada

.. _`Pedro Martinez`: https://github.com/peterg1t

* `Rafael Ayala`_
    * `Hospital General Universitario Gregorio Marañón`_, Spain

.. _`Rafael Ayala`: https://github.com/ayalalazaro


|uth| |uoc| |hgugm|


Maintainer emeritus
...................

* `Matthew Jennings`_
    * `Royal Adelaide Hospital`_, Australia

.. _`Matthew Jennings`: https://github.com/Matthew-Jennings

|rah|

Past contributors
.................

* `Matthew Sobolewski <https://github.com/msobolewski>`_
* `Paul King <https://github.com/kingrpaul>`_
* `Jacob McAloney <https://github.com/JacobMcAloney>`_


.. |rccc| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/rccc_200x200.png
    :target: `Riverina Cancer Care Centre`_

.. |rah| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/gosa_200x200.png
    :target: `Royal Adelaide Hospital`_

.. |jarmc| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/jarmc_200x200.png
    :target: `Anderson Regional Cancer Center`_

.. |nbcc| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/nbcc_200x200.png
    :target: `Northern Beaches Cancer Care`_

.. |uoc| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/uoc_200x200.png
    :target: `University of Calgary`_

.. |uth| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/UTHSA_logo.png
    :target: `UT Health San Antonio`_

.. |hgugm| image:: https://github.com/pymedphys/pymedphys/raw/3f8d82fc3b53eb636a75336477734e39fa406110/docs/logos/HGUGM_200x200.png
    :target: `Hospital General Universitario Gregorio Marañón`_

.. |sjs| image:: https://github.com/pymedphys/pymedphys/raw/7e9204656e0468b0843533472553a03a99387386/logos/swerdloff.png
    :target: `Swerdloff Family`_

.. _`Riverina Cancer Care Centre`: https://www.riverinacancercare.com.au/

.. _`ELEKTA Pty Ltd`: https://www.elekta.com/

.. _`Royal Adelaide Hospital`: https://www.rah.sa.gov.au/

.. _`University of New South Wales`: https://www.unsw.edu.au/

.. _`South Western Sydney Local Health District`: https://www.swslhd.health.nsw.gov.au/

.. _`Anderson Regional Cancer Center`: https://www.andersonregional.org/services/cancer-care/

.. _`Northern Beaches Cancer Care`: https://www.northernbeachescancercare.com.au/

.. _`University of Calgary`: https://www.ucalgary.ca/

.. _`Tom Baker Cancer Centre`: https://www.ahs.ca/tbcc

.. _`UT Health San Antonio`: https://www.uthscsa.edu/academics/biomedical-sciences/programs/radiological-sciences-phd

.. _`Hospital General Universitario Gregorio Marañón`: https://www.comunidad.madrid/hospital/gregoriomaranon/

.. _`Swerdloff Family`: https://github.com/sjswerdloff

.. _`Ingham Institute`: https://inghaminstitute.org.au/

.. END_OF_DOCS_IMPORT

.. _`Tutorials`: https://docs.pymedphys.com/tutes
.. _`How-To guides`: https://docs.pymedphys.com/howto
.. _`Reference`: https://docs.pymedphys.com/ref
.. _`Background`: https://docs.pymedphys.com/background

.. _`library`: https://docs.pymedphys.com/ref/lib
.. _`command line tools`: https://docs.pymedphys.com/ref/cli

.. _`Release Notes`: http://docs.pymedphys.com/release-notes.html
