# Maintainers
<!-- TODO: Who are the points of contact in your project who are responsible/accountable for the project? This can often be an engineering or design manager or leader, who may or may not be the primary maintainers of the project.-->
This is a list of maintainers for this project. See [CODEOWNERS.md](./CODEOWNERS.md) for list of reviewers for different parts of the codebase. Team members include:

## Maintainers:
{list or table including the fields: role, name, affiliation, github username}

|Role |Name |Github Username |Affiliation|
|:-----|:-----|:-----|:-----|
| {role} | {names} | {github usernames} | {affiliations}|

## Contributors

<!-- In order to automatically update the MAINTAINERS.md, you must enter a secret into your Secrets and Variables under Actions within your repository settings. The name of the secret must be PUSH_TO_PROTECTED_BRANCH and the value must be a Personal Access Token with specific permissions. Please follow [this link](https://github.com/CasperWA/push-protected?tab=readme-ov-file#notes-on-token-and-user-permissions) for more information. -->

Total number of contributors: <!--CONTRIBUTOR COUNT START--> <!--CONTRIBUTOR COUNT END-->

<!-- readme: contributors -start -->
<table>
	<tbody>
		<tr>
            <td align="center">
                <a href="https://github.com/IsaacMilarky">
                    <img src="https://avatars.githubusercontent.com/u/24639268?v=4" width="100;" alt="IsaacMilarky"/>
                    <br />
                    <sub><b>Isaac Milarsky</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/sachin-panayil">
                    <img src="https://avatars.githubusercontent.com/u/79382140?v=4" width="100;" alt="sachin-panayil"/>
                    <br />
                    <sub><b>Sachin Panayil</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/natalialuzuriaga">
                    <img src="https://avatars.githubusercontent.com/u/29980737?v=4" width="100;" alt="natalialuzuriaga"/>
                    <br />
                    <sub><b>Natalia Luzuriaga</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/patsier-cms">
                    <img src="https://avatars.githubusercontent.com/u/129543325?v=4" width="100;" alt="patsier-cms"/>
                    <br />
                    <sub><b>patsier-cms</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/decause-gov">
                    <img src="https://avatars.githubusercontent.com/u/107957201?v=4" width="100;" alt="decause-gov"/>
                    <br />
                    <sub><b>decause-gov</b></sub>
                </a>
            </td>
            <td align="center">
                <a href="https://github.com/cms-eo14168">
                    <img src="https://avatars.githubusercontent.com/u/197958188?v=4" width="100;" alt="cms-eo14168"/>
                    <br />
                    <sub><b>cms-eo14168</b></sub>
                </a>
            </td>
		</tr>
	<tbody>
</table>
<!-- readme: contributors -end -->


# Tier 2 Release Guidelines

codejson-index-generator will see regular updates and new releases. This document describes the general guidelines around how and when a new release is cut.

## Table of Contents

* [Versioning](#versioning)
 <!-- * [Breaking vs. non-breaking changes](#breaking-vs-non-breaking-changes) -->
  <!-- * [Ongoing version support](#ongoing-version-support) -->
* [Release Process](#release-process)
  * [Goals](#goals)
  * [Schedule](#schedule)
  * [Communication and Workflow](#communication-and-workflow)
<!-- * [Beta Features](#beta-features) -->
- [Maintainers](#maintainers)
  - [Maintainers:](#maintainers-1)
  - [Contributors](#contributors)
- [Tier 2 Release Guidelines](#tier-2-release-guidelines)
  - [Table of Contents](#table-of-contents)
  - [Versioning](#versioning)
  - [Release Process](#release-process)
    - [Goals](#goals)
    - [Schedule](#schedule)
    - [Communication and Workflow](#communication-and-workflow)
  - [Preparing a Release Candidate](#preparing-a-release-candidate)
    - [Incorporating feedback from review](#incorporating-feedback-from-review)
  - [Making a Release](#making-a-release)
  - [Auto Changelog](#auto-changelog)
  - [Hotfix Releases](#hotfix-releases)

## Versioning

codejson-index-generator uses [Semantic Versioning](https://semver.org/). Each release is associated with a [`git tag`](github.com/DSACMS/codejson-index-generator/tags) of the form `X.Y.Z`.

Given a version number in the `MAJOR.MINOR.PATCH` (eg., `X.Y.Z`) format, here are the differences in these terms:

- **MAJOR** version - make breaking/incompatible API changes
- **MINOR** version - add functionality in a backwards compatible manner
- **PATCH** version - make backwards compatible bug fixes


<!-- ### Breaking vs. non-breaking changes -->

<!--- TODO: Examples and protocol for breaking changes

Definitions for breaking changes will vary depending on the use-case and project but generally speaking if changes break standard workflows in any way then they should be put in a major version update.
-->

<!-- ### Ongoing version support (OPTIONAL)-->

<!-- TODO: Explanation of general thought process 

Explain the project’s thought process behind what versions will and won’t be supported in the future.

This should keep in mind that the audience of a Tier 2 project will be innersource developers and users. As a result there will likely be less of a need to maintain LTS versions.
-->

<!-- TODO: List of supported releases

This section should make clear which versions of the project are considered actively supported.
-->



## Release Process

The sections below define the release process itself, including timeline, roles, and communication best practices.


### Goals

<!-- TODO: Explain the goals of your project’s release structure

This should ideally be a bulleted list of what your regular releases will deliver to key users and stakeholders
-->

### Schedule

<!-- TODO: Communicate the timing of the regular release structure

For example, if you plan on creating regular releases on a weekly basis you should communicate that as well as the typical days upcoming releases will become tagged. 

You should also communicate special cases such as security updates or critical bugfixes and how they would likely be released earlier than what is usually scheduled. 
-->


### Communication and Workflow

<!-- TODO: Communicate proper channels to be notified about releases

Communicate the slack channels, mailing lists, or other means of pushing out release notifications.
-->


<!-- TODO: (OPTIONAL) Support beta feature testing
## Beta Features

When a new beta feature is created for a release, make sure to create a new Issue with a '[Feature Name] - Beta [X.X.x] - Feedback' title and a 'beta' label. Update the spec text for the beta feature with 'Beta feature: Yes (as of X.X.x). Leave feedback' with a link to the new feature Issue.

Once an item is moved out of beta, close its Issue and change the text to say 'Beta feature: No (as of X.X.x)'.
-->

## Preparing a Release Candidate

The following steps outline the process to prepare a Release Candidate of codejson-index-generator. This process makes public the intention and contents of an upcoming release, while allowing work on the next release to continue as usual in `dev`.


1. Create a *Release branch* from the tip of `dev` named `release-x.y.z`, where `x.y.z` is the intended version of the release. This branch will be used to prepare the Release Candidate. For example, to prepare a Release Candidate for `0.5.0`:

    ```bash
    git fetch
    git checkout origin/dev
    git checkout -b release-0.5.0
    git push -u origin release-0.5.0
    ```

    Changes generated by the steps below should be committed to this branch later.




2. Create a tag like `x.y.z-rcN` for this Release Candidate. For example, for the first `0.5.0` Release Candidate:

    ```bash
    git fetch
    git checkout origin/release-0.5.0
    git tag 0.5.0-rc1
    git push --tags
    ```

3. Publish a [pre-Release in GitHub](proj-releases-new):

    ```md
    Tag version: [tag you just pushed]
    Target: [release branch]
    Release title: [X.Y.Z Release Candidate N]
    Description: [copy in ReleaseNotes.md created earlier]
    This is a pre-release: Check
    ```

4. Open a Pull Request to `main` from the release branch (eg. `0.5.0-rc1`). This pull request is where review comments and feedback will be collected.

5. Conduct Review of the Pull Request that was opened.

### Incorporating feedback from review

The review process may result in changes being necessary to the release candidate.

For example, if the second Release Candidate for `0.5.0` is being prepared, after committing necessary changes, create a tag on the tip of the release branch like `0.5.0-rc2` and make a new [GitHub pre-Release](proj-releases-new) from there:

```bash
git fetch
git checkout origin/release-0.5.0
# more commits per OMF review
git tag 0.5.0-rc2
git push --tags
```

Repeat as-needed for subsequent Release Candidates.  Note the release branch will be pushed to `dev` at key points in the approval process to ensure the community is working with the latest code.

## Making a Release

The following steps describe how to make an approved [Release Candidate](#preparing-a-release-candidate) an official release of codejson-index-generator:

1. **Approved**. Ensure review has been completed and approval granted.

2. **Main**. Merge the Pull Request created during the Release Candidate process to `main` to make the release official.

3. **Dev**. Open a Pull Request from the release branch to `dev`. Merge this PR to ensure any changes to the Release Candidate during the review process make their way back into `dev`.

4. **Release**. Publish a [Release in GitHub](proj-releases-new) with the following information

   - Tag version: [X.Y.Z] (note this will create the tag for the `main` branch code when you publish the release)
   - Target: main
   - Release title: [X.Y.Z]
   - Description: copy in Release Notes created earlier
   - This is a pre-release: DO NOT check


5. **Branch**. Finally, keep the release branch and don't delete it. This allows easy access to a browsable spec.

## Auto Changelog

It is recommended to use the provided auto changelog github workflow to populate the project’s CHANGELOG.md file:

```yml
name: Changelog
on:
  release:
    types:
      - created
jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - name: "Auto Generate changelog"
        uses: heinrichreimer/action-github-changelog-generator@v2.3
        with:
          
          token: ${{{{ secrets.GITHUB_TOKEN }}}}
          
```
This provided workflow will automatically populate the CHANGELOG.md with all of the associated changes created since the last release that are included in the current release. 

This workflow will be triggered when a new release is created.

If you do not wish to use automatic changelogs, you can delete the workflow and update the CHANGELOG.md file manually. Although, this is not recommended.

## Hotfix Releases

In rare cases, a hotfix for a prior release may be required out-of-phase with the normal release cycle. For example, if a critical bug is discovered in the `0.3.x` line after `0.4.0` has already been released.

1. Create a *Support branch* from the tag in `main` at which the hotfix is needed. For example if the bug was discovered in `0.3.2`, create a branch from this tag:

    ```bash
    git fetch
    git checkout 0.3.2
    git checkout -b 0.3.x
    git push -u origin 0.3.x
    ```

2. Merge (or commit directly) the hotfix work into this branch.


3. Tag the support branch with the hotfix version. For example if `0.3.2` is the version being hotfixed:

    ```bash
    git fetch
    git checkout 0.3.x
    git tag 0.3.3
    git push --tags
    ```

4. Create a [GitHub Release](proj-releases-new) from this tag and the support branch. For example if `0.3.3` is the new hotfix version:

    ```md
    Tag version: 0.3.3
    Target: 0.3.x
    Release title: 0.3.3
    Description: [copy in ReleaseNotes created earlier]
    This is a pre-release: DO NOT check
    ```






[proj-releases-new]: https://github.com/DSACMS/codejson-index-generator/releases/new



