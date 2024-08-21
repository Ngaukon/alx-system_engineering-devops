![image](https://github.com/user-attachments/assets/ca7d925b-9c95-4a12-ba47-0e4f8a2f78c5)


Issue Summary

On August 15, 2024, from 2:30 PM to 4:15 PM EAT, WebNest experienced a partial outage that impacted approximately 40% of users. During this period, users encountered slow loading times and frequent "502 Bad Gateway" errors when trying to access the website. The root cause was traced to an overloaded Nginx server due to an unoptimized caching layer, which caused a bottleneck in traffic handling. The incident was identified through automated monitoring alerts and escalated to the DevOps team for resolution.

Timeline

- 2:30 PM EAT - Automated monitoring alerts triggered, indicating elevated response times and increased 502 errors.
- 2:35 PM EAT - Initial investigation by the on-call engineer confirmed the issue, with users unable to access the site reliably.
- 2:40 PM EAT - Traffic routing and load balancing mechanisms were checked, with a hypothesis that the issue was network-related.
- 2:50 PM EAT - Misleading assumption that a recent DNS update might have caused the issue led to a thorough review of DNS records.
- 3:05 PM EAT - Escalation to the DevOps team after network-related issues were ruled out.
- 3:20 PM EAT - Investigation shifted to the Nginx server, revealing high CPU and memory usage.
- 3:30 PM EAT - Cache misconfiguration was identified as the root cause; Nginx was failing to efficiently handle requests.
- 3:45 PM EAT - Cache settings were optimized, and additional resources were allocated to the Nginx server.
- 4:00 PM EAT - Monitoring confirmed that the site was returning to normal operation, with error rates dropping.
- 4:15 PM EAT - Incident resolved, with all services restored to full functionality.

Root Cause and Resolution

The root cause of the outage was a misconfiguration in the caching mechanism of the Nginx server. Specifically, the server's cache size was set too small, causing frequent cache evictions and an excessive number of requests to be passed directly to the backend servers. This overwhelmed the Nginx server, leading to high CPU usage and eventually causing it to serve 502 errors to users.

The issue was resolved by increasing the cache size in the Nginx configuration and adjusting the cache expiration settings to reduce the frequency of evictions. Additionally, the server's resources (CPU and memory) were temporarily scaled up to handle the increased load while the cache settings were fine-tuned. Once the changes were applied, the server performance stabilized, and users were able to access the site without further issues.

Corrective and Preventative Measures

To prevent similar incidents in the future, the following steps will be implemented:

1. Optimize Caching Configuration: Review and optimize the Nginx caching settings to ensure they are suitable for current traffic levels.
2. Implement Load Testing: Conduct regular load testing on the Nginx server to identify potential bottlenecks under high traffic conditions.
3. Enhance Monitoring: Add more granular monitoring for Nginx cache performance and server resource usage, with alerts for abnormal behavior.
4. Automate Scaling: Implement auto-scaling for Nginx servers based on traffic load to prevent resource exhaustion.
5. Review DNS Changes Process: Establish a protocol to verify that DNS changes are not contributing to outages, minimizing time spent on misleading investigation paths.

Task List:

-  Increase Nginx cache size and adjust cache expiration settings.
-  Conduct a full load test on the Nginx server to identify optimal configuration settings.
-  Enhance monitoring with specific metrics for cache performance and resource usage.
-  Set up auto-scaling for Nginx servers in response to traffic spikes.
-  Develop a checklist to rule out DNS issues quickly in future incidents.

By implementing these measures, WebNest will strengthen its infrastructure and reduce the likelihood of similar outages in the future.


