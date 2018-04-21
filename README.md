Polarizer
===========

Introduction
------------

**Polarizer** is a small tool I built to perform some queries against a [Polarion](https://polarion.plm.automation.siemens.com/) instance. Right now it can output queries to standard output.

**NOTE**: It is expected that the following variables are properly set in your *environment*:

* POLARION_USER
* POLARION_PASSWORD
* POLARION_URL

Installation
------------

Installation is still manual:

1. Clone the `polarizer` repository to your computer.
2. Install it by running `pip install -r requirements.txt`

Usage
-----

    $ polarizer --help
    Usage: polarizer [OPTIONS] COMMAND [ARGS]...

    CLI object.

    Options:
    --help  Show this message and exit.

    Commands:
    plan         Display information about a Plan.
    requirement  Display information about a Requirement.

    $ polarizer plan --help
    Usage: polarizer plan [OPTIONS]

    Display information about a Plan.

    Options:
    --product TEXT     Product name  [required]
    --plan TEXT        Plan ID  [required]
    -s, --server TEXT  Polarion server URL (e.g. https://example.com/polarion/)
    --help             Show this message and exit.

    $ polarizer requirement --help
    Usage: polarizer requirement [OPTIONS]

    Display information about a Requirement.

    Options:
    --product TEXT          Product name  [required]
    -r, --requirement TEXT  Requirement ID  [required]
    -s, --server TEXT       Polarion server URL (e.g.
                            https://example.com/polarion/)
    --help                  Show this message and exit.

Examples
--------

Grab *requirements* information for `product` *RHSAT6* and `plan` *Satellite_6_4_0*:

    $ polarizer plan --product RHSAT6 --plan Satellite_6_4_0
    qe_test_coverage+, sat-6.4.0+ = 2
    +--------------+------------------------------+------------+
    |      id      |            author            | test_cases |
    +--------------+------------------------------+------------+
    | RHSAT6-39819 |         Perry Gagne (pgagne) |         13 |
    | RHSAT6-39820 |         Perry Gagne (pgagne) |         15 |
    | RHSAT6-39821 |         Perry Gagne (pgagne) |          9 |
    | RHSAT6-39822 |         Bruno Rocha (brocha) |          1 |
    | RHSAT6-39824 |  Renzo Nuccitelli (rnuccite) |          4 |
    | RHSAT6-39825 |  Renzo Nuccitelli (rnuccite) |          9 |
    | RHSAT6-39826 |       Lukas Pramuk (lpramuk) |          0 |
    | RHSAT6-39829 |       Roman Plevka (rplevka) |          8 |
    | RHSAT6-39838 |       Lukas Pramuk (lpramuk) |          0 |
    | RHSAT6-39839 |     Jake Callahan (jcallaha) |         14 |
    | RHSAT6-39840 |     Jake Callahan (jcallaha) |          5 |
    | RHSAT6-39841 |     Jake Callahan (jcallaha) |          6 |
    | RHSAT6-39842 |     Jake Callahan (jcallaha) |          1 |
    | RHSAT6-39883 |      Sanket Jagtap (sjagtap) |          5 |
    | RHSAT6-39884 |      Sanket Jagtap (sjagtap) |         16 |
    | RHSAT6-39885 |    Jitendra Yejare (jyejare) |         35 |
    | RHSAT6-39903 |     Radovan Drazny (rdrazny) |          4 |
    | RHSAT6-39940 | Lukas Hellebrandt (lhellebr) |         21 |
    | RHSAT6-39949 |      Ales Dujicek (adujicek) |          3 |
    | RHSAT6-39996 |         Bruno Rocha (brocha) |          0 |
    | RHSAT6-39997 |       Lukas Pramuk (lpramuk) |          0 |
    +--------------+------------------------------+------------+

Grab all `Test Cases` for `product` *RHSAT6* and `Requirement` *RHSAT6-39949*:

    $ polarizer requirement --product RHSAT6 -r RHSAT6-39949
    Requirement: RHSAT6-39949
    Author: Ales Dujicek (adujicek)
    Test Cases: 3
    - subterra:data-service:objects:/default/RHSAT6${WorkItem}RHSAT6-39951
    - subterra:data-service:objects:/default/RHSAT6${WorkItem}RHSAT6-39950
    - subterra:data-service:objects:/default/RHSAT6${WorkItem}RHSAT6-39952

**Override** the `server` URL to fetch information from a different instance:

    $ polarizer plan --product CLOUDTP --plan Satellite_6_2_z -s https://devel.example.com/polarion
    +---------------+-------------+------------+
    |       id      |    author   | test_cases |
    +---------------+-------------+------------+
    | CLOUDTP-24067 | Import User |          0 |
    +---------------+-------------+------------+
