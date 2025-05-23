# codejson-index-generator

Script to create an indexed code.json for agencies.

## About the Project

The GitHub Code.json Index Generator is a Python-based tool that helps federal agencies compile and maintain their code.json files for code.gov compliance. It automatically scans specified GitHub organizations, finds repositories containing code.json files, and combines them into a single indexed file.

### Project Vision

To streamline the process of code.gov compliance for federal agencies by automating the collection and aggregation of code.json files across multiple GitHub organizations.

### Project Mission

To provide agencies with a reliable, efficient tool for maintaining their code.gov inventory while reducing manual effort and potential for errors in the process.

## Core Team

An up-to-date list of core team members can be found in [MAINTAINERS.md](MAINTAINERS.md). At this time, the project is still building the core team and defining roles and responsibilities. We are eagerly seeking individuals who would like to join the community and help us define and fill these roles.

<!--
## Documentation Index

TODO: This is a like a 'table of contents" for your documentation. Tier 0/1 projects with simple README.md files without many sections may or may not need this, but it is still extremely helpful to provide "bookmark" or "anchor" links to specific sections of your file to be referenced in tickets, docs, or other communication channels.

**{list of .md at top directory and descriptions}**
 -->

<!--
## Repository Structure

TODO: Using the "tree -d" command can be a helpful way to generate this information, but, be sure to update it as the project evolves and changes over time.

**{list directories and descriptions}**

-->

<!--
# Development and Software Delivery Lifecycle
The following guide is for members of the project team who have access to the repository as well as code contributors. The main difference between internal and external contributions is that external contributors will need to fork the project and will not be able to merge their own pull requests. For more information on contributing, see: [CONTRIBUTING.md](./CONTRIBUTING.md).
-->

## Local Development

### Prerequisites

- Python 3.x
- GitHub Personal Access Token (optional, but highly recommended for higher rate limits)
  > **_Create a PAT:_** GitHub -> Settings -> Developer Settings -> Personal Access Tokens

### Installation

1. Clone the repository:

```bash
git clone ...
cd codejson-index-generator
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

1. Set up your GitHub Personal Access Token:

```bash
export GITHUB_KEY="your-token-here"
```

> **_NOTE:_** _Use of GitHub PAT is highly recommened due to rate limiting._

### Usage

The script can be run from the command line with the following options:

```bash
python main.py --agency AGENCY_NAME --orgs "org1,org2" --output code.json --version VERSION_NUMBER
```

> **_NOTE:_** _Seperate organizations by comma without any spaces!_

##### Required arguments:

- `--agency`: The name of your agency
- `--orgs`: Comma-separated list of GitHub organizations to scan

##### Optional arguments:

- `--output`: Output filename (default: code.json)
- `--version`: Code.json file version (default: 1.0.0)

##### Example:

```bash
python3 main.py --agency CMS --orgs "DSACMS,CMSgov,CMS-Enterprise" --output code.json --version 1.0.0
```

## Coding Style and Linters

<!-- TODO - Add the repo's linting and code style guidelines -->

Each application has its own linting and testing guidelines. Lint and code tests are run on each commit, so linters and tests should be run locally before committing.

<!--
## Branching Model

TODO - with example below:
This project follows [trunk-based development](https://trunkbaseddevelopment.com/), which means:

* Make small changes in [short-lived feature branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/) and merge to `main` frequently.
* Be open to submitting multiple small pull requests for a single ticket (i.e. reference the same ticket across multiple pull requests).
* Treat each change you merge to `main` as immediately deployable to production. Do not merge changes that depend on subsequent changes you plan to make, even if you plan to make those changes shortly.
* Ticket any unfinished or partially finished work.
* Tests should be written for changes introduced, and adhere to the text percentage threshold determined by the project.

This project uses **continuous deployment** using [Github Actions](https://github.com/features/actions) which is configured in the [./github/workflows](.github/workflows) directory.

Pull-requests are merged to `main` and the changes are immediately deployed to the development environment. Releases are created to push changes to production.
-->

## Contributing

Thank you for considering contributing to an Open Source project of the US Government! For more information about our contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Codeowners

The contents of this repository are managed by **{responsible organization(s)}**. Those responsible for the code and documentation in this repository can be found in [CODEOWNERS.md](CODEOWNERS.md).

## Community

The codejson-index-generator team is taking a community-first and open source approach to the product development of this tool. We believe government software should be made in the open and be built and licensed such that anyone can download the code, run it themselves without paying money to third parties or using proprietary software, and use it as they will.

We know that we can learn from a wide variety of communities, including those who will use or will be impacted by the tool, who are experts in technology, or who have experience with similar technologies deployed in other spaces. We are dedicated to creating forums for continuous conversation and feedback to help shape the design and development of the tool.

We also recognize capacity building as a key part of involving a diverse open source community. We are doing our best to use accessible language, provide technical and process documents, and offer support to community members with a wide variety of backgrounds and skillsets.

### Community Guidelines

Principles and guidelines for participating in our open source community are can be found in [COMMUNITY_GUIDELINES.md](COMMUNITY_GUIDELINES.md). Please read them before joining or starting a conversation in this repo or one of the channels listed below. All community members and participants are expected to adhere to the community guidelines and code of conduct when participating in community spaces including: code repositories, communication channels and venues, and events.

<!--
## Governance
Information about how the **{project_name}** community is governed may be found in [GOVERNANCE.md](GOVERNANCE.md).

<!--
## Feedback
If you have ideas for how we can improve or add to our capacity building efforts and methods for welcoming people into our community, please let us know at **{contact email}**. If you would like to comment on the tool itself, please let us know by filing an **issue on our GitHub repository.**

## Glossary
Information about terminology and acronyms used in this documentation may be found in [GLOSSARY.md](GLOSSARY.md).
-->

## Policies

### Open Source Policy

We adhere to the [CMS Open Source
Policy](https://github.com/CMSGov/cms-open-source-policy). If you have any
questions, just [shoot us an email](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure Policy

_Submit a vulnerability:_ Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt of your report within 3 business days.

For more information about our Security, Vulnerability, and Responsible Disclosure Policies, see [SECURITY.md](SECURITY.md).

### Software Bill of Materials (SBOM)

A Software Bill of Materials (SBOM) is a formal record containing the details and supply chain relationships of various components used in building software.

In the spirit of [Executive Order 14028 - Improving the Nation’s Cyber Security](https://www.gsa.gov/technology/it-contract-vehicles-and-purchasing-programs/information-technology-category/it-security/executive-order-14028), a SBOM for this repository is provided here: https://github.com/DSACMS/codejson-index-generator/network/dependencies.

For more information and resources about SBOMs, visit: https://www.cisa.gov/sbom.

## Public domain

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/) as indicated in [LICENSE](LICENSE).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request or issue, you are agreeing to comply with this waiver of copyright interest.
