
n.n.n / 2023-05-31
==================

  * feat: Added single device get classes and updated readme
  * Added single device methods
  * wip: Started refactor for docs
  * feat: Finished updating unit tests
  * test: Unit test CICD
  * Fixed unit tests and device casing woohoo!
  * wip: Move spec to class ref
  * wip: Casting working now, still more work to do
  * wip: Fixed Search function
  * wip: Fixing CLI test
  * Adde missing funcs
  * wip:Started on class refactor
  * Updated doc gen

v2.3.3 / 2023-05-10
===================

  * Release 2.3.3
  * dev: class rename

v2.3.2 / 2023-05-09
===================

  * Release v2.3.2
  * feat: Added error logging

v2.3.1 / 2023-05-09
===================

  * Release v2.3.1
  * fix: Added exception for missing credentials

v2.3.0 / 2023-05-08
===================

  * Release v2.3.0
  * Merge branch 'fix/temp-sensor-missing'
  * fix: Added specific device type of temp and env sensors
  * fix: Added check for correct attribute
  * feat: Added humidity attribute

v2.2.0 / 2023-04-30
===================

  * ci: Version bump
  * Merge branch 'feat/temp_sensor'
  * Fixed CLI tests and refactored obj lookup
  * wip: Fixed temp data pull, now geting cli errors
  * wip: Added note about EcoBee test failing
  * Added commit actions to run in parellel
  * Added retry to actions
  * Testing new release action
  * Updated action and change log formating
  * Add update existing to tag
  * Updated test run for seperate modules
  * Adjusted cov for GH action not having .env file
  * Added note to readme about change log
  * dev: Added auto release gen
  * dev: Updated taskfile build
  * Added Poetry version based on Git Tag
  * feat: Added Temprature sensor get method wip: Started on Thermostat
  * Added get all devices api call
  * Added Auto change log generation
  * Removed radon from suite, not being used in interactive test
  * Added pause in test

v2.0.0 / 2023-04-08
===================

  * Version bump
  * Merge branch 'feat/cli-interface'
  * Readme update
  * Added keyring check
  * Added env load to keyring check
  * Moved tests to new module
  * fix: Resolved issue with cli unit tests when package is not installed
  * Moved CLI tests
  * Added exception to cli test
  * Added turn on method to cli
  * wip: Need to add device lookup to add turn on fuction
  * wip: Testing CLI options
  * Adding keyring option for easy cli usage

v1.1.2 / 2023-03-31
===================

  * Added CLI entrypoint and updated help
  * Update table output
  * Merge branch 'feat/device-output-cli'
  * Cleaned up table output
  * Added README notes
  * wip: refactored CLI args to two seperate commands
  * Switched to typer

v1.1.1 / 2023-03-24
===================

  * Updated docs
  * Version bump for color map
  * Merge branch 'feat/color-map'
  * Added color map
  * Update taskfile
  * Updated task install
  * Updated task for GH
  * wip: cicd testing
  * Swapping out local runner for GH actions
  * Added timeout
  * Module updates
  * Temp sensor version bump
  * Merge pull request #30
  * Added temp sensor
  * Added TODOs for Roadmaps
  * Taskfile update
  * Swapped docker build to pull and install direct from GitHub, this way we always get a true install
  * Added tartufo security scanning
  * Merge pull request #15
  * Added input checking
  * Merge pull request #14
  * Refactored back to module based layout. Poetry will handle the rest :-)
  * Added black option
  * Re-add todo
  * Create Run-TODO-to-Issue.yml
  * Create tood-to-issue.yml
  * Readme Update
  * Added community files
  * Added black profile to isort
  * Adjusted code base per flake8
  * Added flake8 and refactored init method
  * Added mdformat, starting on flake8
  * Merge branch 'test/sec_scan'
  * Added security scanning
  * Added exception for invalid names
  * Broke Dimmer into seperate class
  * Merge pull request #9
  * Updated docs to include cloud API and tested via unit test
  * Merge pull request #8
  * Version bump
  * Swapped out to dev devices
  * Merge pull request #7
  * Version bump
  * Updated readme

v1.0.7 / 2023-02-02
===================

  * Merge pull request #6
  * Fixing docker file
  * Version bump and docs update
  * Refactored module to src folder
  * Update dev readme
  * Added codeowners

v1.0.6 / 2023-01-25
===================

  * doc: Updated readme w/ Semantic Versioning
  * test: Fixed unit test
  * Added actions
  * Added actions
  * Merge branch 'feat/dyn_device_return'
  * Bump to v1.0 yay
  * Refactored device creation to be based on capability
  * Refactored device creation to be based on capability
  * Read me update
  * Added src pull to readme

v0.8.0 / 2023-01-22
===================

  * Merge remote-tracking branch 'origin/dependabot/pip/python-dotenv-0.21.1'
  * Added CodeQL
  * Create codeql.yml
  * Update coveralls.yml
  * Create coveralls.yml
  * Bump python-dotenv from 0.21.0 to 0.21.1
  * Create dependabot.yml
  * Cleaned up readme tags
  * Updated classifiers
  * Commented out unused libs
  * Version bump for PyPi Readme
  * Actions update
  * Badge update
  * Merge remote-tracking branch 'origin/main'
  * Merge branch 'docker'
  * Moved config options to pyproj
  * Task cleanup
  * Update issue templates
  * Cleaning up task file and build
  * Cleaned up Docker test to only use packages needed for PyTest
  * Pytest working in docker, just need to troubleshoot warnings
  * Added docker support for pytest
  * Added badges
  * Consolidated unit test
  * Updated unit test to just search for device type, so it can be run in other envs
  * fix: Unit test and taskfile
  * Merge branch 'feat/leviton-dimmer'
  * Added commit hooks

v0.7.0 / 2023-01-19
===================

  * Merge branch 'feat/leviton-dimmer'
  * Dimmer finished
  * Linting
  * Added Typeguard and black
  * Tooling re-add
  * Security
  * Updated task file
  * Added dimmer get method
  * Started on dimmer class
  * Roadmap update
  * Version bump
  * task update
  * Swapped to Poetry
  * Swapped for Radon
  * Addde Wily
  * Updated unit test for persistence
  * Added UML gen
  * Started on outlet
  * Readme update
  * Added hub method
  * Started on outlet
  * Docs update
  * Device lookup method
  * Finished library refactor
  * Dynamic object return
  * Updated readme
  * Name space fix

v0.5.0 / 2023-01-14
===================

  * package name
  * Testing src folder
  * Fixed namespace
  * Added init for package
  * namespace tweak
  * lib version bump
  * Updated module path
  * Moved lights to seperate module
  * Update readme
  * Started on device poly return
  * Added RGB bulb
  * Updating todo list
  * Updated task file
  * Added docs
  * Added doc gen
  * Updated tests
  * Install options
  * Proj cleanup
  * Updated Package name
  * Fixed task exec order
  * Fixed unit tests and added isort
  * Still refactoring class
  * Update task with flit build
  * Update task file
  * Update task file
  * Started on Flit Generation
  * Updatd env file info
  * Updatd docs
  * Added project files
  * Update README.md
  * Initial commit
