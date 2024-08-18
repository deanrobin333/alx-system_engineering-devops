![Debugging Shopright](./web_debugging_shopright.jpeg).
**Postmortem Report: Web Stack Debugging Issue**

**Issue Summary**

**Duration:** August 18, 2024, 17:30 - 19:00 GMT+3 (1 hour 30 minutes)

**Impact:** The e-commerce website "ShopRight" (my portfolio project) experienced a significant slowdown, with page load times increasing from an average of 2 seconds to 20 seconds. Approximately 80% of users were affected, leading to a 60% drop in sales during the outage period. Users reported slow browsing and frequent timeouts while attempting to add items to their carts and proceed to checkout.

**Root Cause:** A misconfiguration in the Nginx server's caching mechanism caused a bottleneck in handling dynamic content, leading to excessive load times and server resource exhaustion.

* * *

**Timeline**

- **17:30 GMT+3:** The issue was detected when monitoring systems triggered an alert about elevated response times on the ShopRight website.
- **17:32 GMT+3:** The on-call engineer noticed a spike in server CPU usage and initiated an investigation into the server logs.
- **17:35 GMT+3:** Initial assumption was a potential DDoS attack due to the unusual traffic patterns observed.
- **17:40 GMT+3:** Network traffic analysis was conducted, but no evidence of a DDoS attack was found.
- **17:50 GMT+3:** The issue was escalated to the web infrastructure team to further investigate the server-side components.
- **18:00 GMT+3:** The team checked database performance, suspecting a potential deadlock, but the database appeared healthy.
- **18:15 GMT+3:** A deeper investigation into the Nginx server revealed a recent change in the caching configuration.
- **18:20 GMT+3:** The Nginx configuration was rolled back to the previous version.
- **18:30 GMT+3:** Server performance returned to normal, with response times decreasing to 2 seconds.
- **19:00 GMT+3:** The incident was fully resolved, and monitoring confirmed that the system was stable.

* * *

**Root Cause and Resolution**

- The root cause of the outage was a misconfigured caching directive in the Nginx server. The change, intended to optimize the delivery of static content, inadvertently caused dynamic content to be cached improperly. This led to outdated or incorrect content being served to users and a significant increase in CPU load as the server struggled to handle the malformed requests.

- The issue was resolved by rolling back the Nginx configuration to a previous stable version. Once the configuration was restored, the server began handling requests as expected, reducing the CPU load and restoring normal page load times.

* * *

**Corrective and Preventative Measures**

**Improvements Needed:**

- **Review and test configuration changes:** All server configuration changes should be thoroughly tested in a staging environment before being applied to production.
- **Enhanced monitoring:** Implement more granular monitoring of server configurations to detect potential misconfigurations early.
- **Documentation:** Improve documentation for server configuration changes to ensure all team members understand the potential impact.

**TODO:**

- Patch Nginx server to include better safeguards against caching misconfigurations.
- Add monitoring alerts for unusual patterns in caching behavior.
- Conduct a review session to ensure all team members are familiar with the proper procedures for making configuration changes.
- Develop a checklist for testing server configurations in the staging environment before deployment.

* * *

This postmortem report aims to document the issue, its resolution, and the steps we will take to prevent similar occurrences in the future. The lessons learned will help us improve our processes and ensure a more robust infrastructure.