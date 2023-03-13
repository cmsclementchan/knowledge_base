
# Can you compare Trunk-based and Branch-based?
Trunk-based development and branch-based development are two different approaches to managing changes to a software codebase. Here are some key differences between the two:

Integration: In trunk-based development, all changes are immediately integrated into the main codebase, whereas in branch-based development, changes are made in isolated branches and are only merged into the main codebase after they have been thoroughly tested and reviewed.

Code stability: Trunk-based development can lead to a less stable codebase, as changes are immediately integrated and may not be thoroughly tested before they are committed. Branch-based development can lead to a more stable codebase, as changes are isolated and tested before they are merged into the main codebase.

Collaboration: Trunk-based development requires a high level of collaboration among developers, as changes are immediately visible to all team members. Branch-based development allows for more independent work, as developers can work on isolated branches without disrupting the main codebase.

Speed: Trunk-based development can be faster than branch-based development, as changes are immediately integrated and can be quickly deployed. Branch-based development can be slower, as changes must be thoroughly tested and reviewed before they are merged into the main codebase.

Complexity: Branch-based development can be more complex than trunk-based development, as it requires more coordination and management of branches. Trunk-based development can be simpler, as all changes are made directly to the main codebase.

Overall, the choice between trunk-based and branch-based development depends on the specific needs and goals of your project. Trunk-based development can be a good choice for projects with a small team or a simple codebase, where speed is important. Branch-based development can be a good choice for projects with a large team or a complex codebase, where collaboration and code stability are important.


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