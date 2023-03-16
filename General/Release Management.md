
# Pros & cons
| Pros | Cons |
| --- | --- |
| 1. Faster time to market | 1. Higher risk of introducing bugs or breaking the build |
| 2. Simple and straightforward workflow | 2. May result in more unstable code in the main branch due to frequent commits |
| 3. Encourages continuous integration and delivery | 3. Requires a high level of communication and coordination among team members |
| 4. Allows for quicker feedback loops | 4. May be challenging to roll back changes once they are committed to the main branch |
| 5. Facilitates collaboration and knowledge sharing among team members | 5. Less emphasis on code review as changes are pushed directly to the main branch |


Company 

https://devblogs.microsoft.com/devops/release-flow-how-we-do-branching-on-the-vsts-team/



# Can you compare Trunk-based and Branch-based?
Trunk-based development and branch-based development are two different approaches to managing changes to a software codebase. Here are some key differences between the two:

Integration: In trunk-based development, all changes are immediately integrated into the main codebase, whereas in branch-based development, changes are made in isolated branches and are only merged into the main codebase after they have been thoroughly tested and reviewed.

Code stability: Trunk-based development can lead to a less stable codebase, as changes are immediately integrated and may not be thoroughly tested before they are committed. Branch-based development can lead to a more stable codebase, as changes are isolated and tested before they are merged into the main codebase.

Collaboration: Trunk-based development requires a high level of collaboration among developers, as changes are immediately visible to all team members. Branch-based development allows for more independent work, as developers can work on isolated branches without disrupting the main codebase.

Speed: Trunk-based development can be faster than branch-based development, as changes are immediately integrated and can be quickly deployed. Branch-based development can be slower, as changes must be thoroughly tested and reviewed before they are merged into the main codebase.

Complexity: Branch-based development can be more complex than trunk-based development, as it requires more coordination and management of branches. Trunk-based development can be simpler, as all changes are made directly to the main codebase.

Overall, the choice between trunk-based and branch-based development depends on the specific needs and goals of your project. Trunk-based development can be a good choice for projects with a small team or a simple codebase, where speed is important. Branch-based development can be a good choice for projects with a large team or a complex codebase, where collaboration and code stability are important.

| Aspect | Trunk-Based Development | Branch-Based Development |
| --- | --- | --- |
| Workflow | Continuous integration and delivery with frequent code commits directly to the main branch | Code development is done on separate branches and merged back into the main branch when ready |
| Team collaboration | Requires a high level of communication and coordination among team members | Allows for more independent work among team members |
| Release frequency | Frequent releases with smaller changes | Less frequent releases with larger changes |
| Code stability | May result in more unstable code in the main branch due to frequent commits | Code changes are isolated to branches until they are deemed stable |
| Code review | Less emphasis on code review as changes are pushed directly to the main branch | Allows for more thorough code review on separate branches |
| Risk management | Risk of introducing bugs or breaking the build is higher due to frequent commits to the main branch | Risk of introducing bugs or breaking the build is reduced as changes are isolated to branches |
| Time to market | Faster time to market as code changes are quickly integrated into the main branch | Slower time to market due to the need for code review and integration |
| Complexity | Simple and straightforward workflow | Requires more complex management of multiple branches |



# Trunk Based Development

**Continuous Integration (CI)**
- Practice where code changes are automatically built and tested as soon as they are committed to the trunk
- Helps catch issues early and ensure codebase remains stable

**Code reviews**
- Involves team members reviewing and testing changes before they are committed to the trunk
- Helps catch bugs and ensure changes are of high quality

**Automated testing**
- Involves writing tests that can be automatically run to verify that changes don't break existing functionality
- Helps catch issues early and ensure codebase remains stable

**Canary releases**
- Involves releasing new changes to a small subset of users before rolling them out to the entire user base
- Helps catch issues before they affect a large number of users

**Feature flags**
- Allow developers to enable and disable features in a software application without having to manage separate branches or codebases
- Often used for more fine-grained control, allowing developers to selectively enable or disable features for specific users or user groups

**Blue-green deployments**
- Involves having two identical production environments: "blue" environment serving production traffic while "green" environment is updated with new changes
- Once green environment is updated and tested, traffic is switched over to the green environment and the blue environment is updated with new changes

**Code branching by abstraction**
- Involves using code abstractions to allow for the development of new features or functionality in parallel with the main trunk
- Abstraction can then be swapped in for the old code once feature is complete, allowing for seamless integration into the trunk

**Canary deployments**
- Gradually rolling out changes to a small subset of users before releasing them to the entire user base
- Often involve using load balancers or other infrastructure to route traffic between multiple versions of the application, allowing for more fine-grained control over the rollout process

**Automated deployment pipelines**
- Involve using tools like Jenkins, Travis CI, or CircleCI to automatically build, test, and deploy changes to the trunk
- Allows for rapid, continuous delivery of new changes to the production environment

**Automated rollbacks**
- In the event that a new change causes issues in the production environment, automated rollbacks can be used to quickly revert to the previous version of the application
- Helps minimize downtime and ensure that the application remains stable and functional

**Progressive delivery**
- Involves gradually rolling out changes to users or user groups, using techniques like canary releases or feature flags to manage the rollout
- Allows for more fine-grained control over the rollout process and helps minimize the impact of any issues that may arise

**Infrastructure as code**
- Involves using code to manage and provision infrastructure resources like servers, databases, and networking
- By treating infrastructure as code, teams can more easily manage and deploy changes to their infrastructure alongside changes to their software applications

**Metrics-based development**
- Involves using data and analytics to inform software development decisions
- By tracking metrics like user engagement, page load times, and error rates, teams can make data-driven decisions about which features to prioritize and how to optimize their applications for performance and usability

**Chaos engineering**
- Involves intentionally introducing failures into a system in order to test its resilience and reliability
- By running controlled experiments to simulate different failure scenarios, teams can identify and address weaknesses in their systems before they cause issues in production

**Continuous delivery (CD)**
- Involves automatically deploying code changes to production as soon as they are tested and approved
- By automating the deployment process, teams

# can you provide some detailed example?
Sure, here's an example of how a company might use trunk-based development:

Suppose there's a software development company called XYZ that develops and maintains an e-commerce website. The company has a team of developers working on the website codebase, and they use trunk-based development to manage their workflow.

Here's how they might go about it:

They start with a mainline branch called "trunk," which contains the latest stable version of the codebase.

Whenever a developer needs to make changes to the code, they create a feature branch off of the trunk branch. For example, a developer might create a branch called "feature/shipping-updates" to work on improving the shipping functionality of the website.

The developer makes their changes on the feature branch and tests them locally to ensure everything is working as expected.

Once the changes are complete and the tests pass, the developer merges their feature branch back into the trunk branch. This ensures that their changes are integrated into the latest stable version of the codebase.

The company has a continuous integration (CI) pipeline set up that runs automated tests on the codebase every time a change is merged into the trunk branch. This helps to catch any issues early on and ensures that the codebase stays stable.

If any issues are found, the developers can quickly fix them and merge the fixes back into the trunk branch. This keeps the codebase up-to-date and stable at all times.

Overall, trunk-based development allows the XYZ development team to work collaboratively on the website codebase while ensuring that the code stays stable and up-to-date. By merging changes back into the mainline trunk branch as soon as they're complete, the team can avoid long-lived feature branches and reduce the risk of conflicts and integration issues down the line.



# is that trunk branch as main branch to deploy?

In trunk-based development, the trunk branch (also known as the mainline or master branch) is used as the main branch for development and deployment. All changes are integrated directly into the trunk branch, and there is no long-lived development branch.

After a change is made and reviewed, it is merged directly into the trunk branch. This means that the trunk branch is always in a releasable state, and any change made to it is considered production-ready.

When a release is needed, a new version is created from the trunk branch. This version is then deployed to the production environment.

So to answer your question, yes, in trunk-based development, the trunk branch is typically used as the main branch for deployment.


# how to do everything using github?
Sure! Here are some steps to follow for using trunk-based development with GitHub:

Create a new repository on GitHub.
Set up your development environment and create a new branch to start working on a new feature or bug fix.
Make changes to the code on your branch and commit them to the branch.
Once the feature or bug fix is complete, push the changes to the branch on GitHub.
Create a pull request to merge your branch into the main branch (trunk) on GitHub.
Assign a reviewer to review the code changes and provide feedback or approve the changes.
Once the changes have been approved, merge the branch into the main branch (trunk) on GitHub.
Deploy the changes to your production environment.
It's important to note that you should only merge code changes into the main branch (trunk) once they have been fully tested and approved. This helps to ensure that your production environment remains stable and bug-free.

# What is the use of the release in github ?
In GitHub, a release is a way to package and distribute a specific version of your project. It is a snapshot of your code at a particular point in time, along with any associated assets such as binaries, documentation, and release notes.

Releases provide a way for users to easily download and install your project's software, without having to build it themselves. They also enable you to communicate important information about the release, such as new features, bug fixes, and breaking changes.

When you create a release in GitHub, you can assign a version number to it, which helps to keep track of different versions of your software. You can also add release notes, which describe the changes in the release, and attach any relevant files, such as installers or documentation.

Releases are useful for open source projects that have a community of contributors and users. By making it easy for people to download and use your software, you can increase the reach and impact of your project.

# What is the difference of unit test, integration and functional test?
Unit tests, integration tests, and functional tests are different types of tests that are used in software development. Here is a brief explanation of each:

Unit Tests: Unit tests are automated tests that verify the behavior of a small piece of code, such as a function or method, in isolation from the rest of the application. The goal of unit testing is to catch errors and bugs early in the development cycle and ensure that each individual component of the application works as intended.

Integration Tests: Integration tests are automated tests that verify the interaction between different components or modules of the application. The goal of integration testing is to catch errors and bugs that arise when different components are combined together, and to ensure that the application as a whole works as intended.

Functional Tests: Functional tests are automated tests that verify the behavior of the application as a whole, by testing its functionality from the user's perspective. The goal of functional testing is to ensure that the application meets its intended requirements and performs as expected in real-world scenarios.

In summary, unit tests focus on individual pieces of code, integration tests focus on the interaction between different pieces of code, and functional tests focus on the behavior of the application as a whole. All three types of tests are important for ensuring the quality and reliability of software.



# Workflow Diagram
https://trunkbaseddevelopment.com/styles/


# How to do it in action?

https://launchdarkly.com/blog/introduction-to-trunk-based-development/

# People Expereince 
https://www.reddit.com/r/ExperiencedDevs/comments/zg4l6h/handling_releases_and_qa_environments_while_using/

Our the workflow Ive implemented looks like exactly like what you’re looking for.

Previously were were using feature branches, staging branches and a production branch, with a develop branch. Changes would be made to a feature branch, then when reviewed and ready for QA would be merged into the staging branch, so it could be tested by QA. Once approved, it’d be merged into develop, which was then merged into production at the end of the sprint. This didn’t work well for many reasons.

We’ve now moved to TBD and continuous delivery. It works like:

Developer makes a PR for a change

2 Developers review the change

Once passed code review, we add a label to the PR to deploy it to a QA environment

We run a QA environment on K8S which will create a deployment for each PR. This creates a branch new environment, very similar to staging, but with its own ephemeral database and AWS infra using Localstack. Any tagged PRs will automatically be deployed to this environment, and the deployment deleted once the PR is closed

Once the change is approved by QA, the PR is merged to our trunk branch, where it automatically deploys to staging

Once deployed to staging, we run thousands of acceptance E2E tests against the whole system, and now some Cypress tests against the frontend

Once the tests have passed, we run a manual deployment to production, using the version number that was deployed to staging. We can specify any version number here, so it can help for rollbacks too. The version number refers to a docker image that was built before the staging deployment, so it ensures we’re using exactly the same build across environments

We aim to deploy every staging deployment to production shortly after, so we do about 5-10 prod deployments a week

This seems to be working very well, and we’ve had no production incidents since implementing it. It allows us to deploy hotfixes very fast as the trunk should always be in a deployable state. The only way it wouldn’t be is if the acceptance tests failed, then we’d probably revert the merged change in order to make it deployable asap. Ideally we’d be running the acceptance tests against the QA environment before merging, and not just against staging, but there’s legacy reasons why this isn’t possible.

I can go into more detail on our implementation of the QA environment if you like, as that’s been the key to all this

EDIT: Just to add, we also make use of feature flags where necessary so that we aren’t holding large changes back from production, as in the past these have often caused problems and been hard to debug. So we aim to split features into lots of small parts and deploy them incrementally, only releasing via feature flag once they’ve been verified to work in production


# Can you also explain more with leveraging the feature in github for the workflow?
Sure, here's how you can leverage some of the features in GitHub for the trunk-based development workflow:

Create a new branch from the trunk branch using the "git checkout -b" command.

Once you've made your changes, create a pull request (PR) using GitHub's built-in PR functionality.

Use the code review features in GitHub to collaborate with your team members and ensure that the code meets the necessary quality standards.

If you're using continuous integration (CI), set up your CI tool to automatically run tests and checks on the code as part of the PR process.

Use GitHub's labels and milestones to track the status of the PR and ensure that it's being reviewed and tested in a timely manner.

Once the code has been approved by your team, merge the changes into the trunk branch using GitHub's merge functionality.

If you're using deployment automation, use GitHub's webhooks to trigger automated deployments to your various environments (e.g. QA, staging, production) when code is merged into the trunk branch.

Use GitHub's release functionality to tag specific commits as releases, making it easier to track which versions of the code are deployed to which environments.

Finally, use GitHub's issue tracking functionality to track any issues that arise in your various environments, and use pull requests to make changes to fix those issues and merge them back into the trunk branch.

By leveraging these features in GitHub, you can streamline your trunk-based development workflow and ensure that your code is being reviewed, tested, and deployed in a consistent and efficient manner.

Reference 

truck based development

https://www.atlassian.com/continuous-delivery/software-delivery-trunk-based-development
https://cloud.google.com/architecture/devops/devops-tech-trunk-based-development

book like

https://trunkbaseddevelopment.com/

branchbyabstraction....

https://www.branchbyabstraction.com/



gitflow
https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
