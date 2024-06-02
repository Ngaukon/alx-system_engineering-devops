### Specifics About This Infrastructure

#### Load Balancer Distribution Algorithm

Current Configuration:
The HAProxy load balancer is configured with the **Round Robin** distribution algorithm. This algorithm works by using each server behind the load balancer in turns, according to their weights. It is considered one of the smoothest and most fair algorithms because it helps ensure that the servers' processing time remains equally distributed. As a dynamic algorithm, Round Robin allows server weights to be adjusted on the go.

Detailed Explanation:
- Round Robin Algorithm
  - Each incoming request is distributed sequentially across all servers in the pool.
  - The distribution is adjusted based on server weights, which can change dynamically.
  - This method helps balance the load effectively by ensuring that each server handles a similar number of requests over time.

#### Load Balancer Setup

Current Setup:
The HAProxy load balancer is enabling an **Active-Passive setup** rather than an Active-Active setup. 

Active-Passive Setup:
- Primary Node: Handles all incoming traffic until it fails or is taken offline.
- Secondary (Passive) Node: Remains on standby, ready to take over if the primary node becomes unavailable.
- This setup ensures redundancy but does not utilize the passive node for load distribution under normal operations.

Comparison with Active-Active Setup:
- Active-Active Setup: All nodes actively handle incoming traffic, improving throughput and response times by leveraging multiple servers simultaneously.

#### Database Primary-Replica (Master-Slave) Cluster

Current Configuration:
A Primary-Replica setup configures one server to act as the **Primary server** and another as the **Replica server**.

**How It Works:**
- **Primary Server**: Capable of performing both read and write operations.
- **Replica Server**: Capable of performing only read operations, which helps offload read traffic from the primary server.
- **Data Synchronization**: The Replica server is synchronized with the Primary server whenever the Primary server executes a write operation, ensuring that the Replica has an up-to-date copy of the data.

Difference Between Primary and Replica Nodes
- Primary Node: Handles all write operations and also serves read requests if necessary.
- Replica Node: Handles read-only operations, reducing the read load on the Primary node and providing high availability for read requests.

### Issues With This Infrastructure

#### Single Points of Failure (SPOF)

Explanation:
There are multiple single points of failure within the current infrastructure:

- Primary MySQL Database Server: If this server fails, the site cannot perform any write operations, which includes critical actions like adding or removing users.
- Load Balancer: If the load balancer fails, all traffic to the website is disrupted.
- Application Server: If the application server fails, the site will be unable to process any requests.

Solutions:
- Implement redundant load balancers.
- Use database clustering or replication with automatic failover.
- Deploy multiple application servers behind the load balancer.

#### Security Issues

Explanation:
The data transmitted over the network isn't encrypted using an SSL certificate, which makes it vulnerable to interception by attackers. Additionally, there is no firewall installed to block unauthorized IP addresses.

Solutions:
- Implement SSL/TLS encryption for all data transmitted over the network.
- Install and configure firewalls to control and filter incoming and outgoing traffic based on predefined security rules.

#### Lack of Monitoring

Explanation:
There is no monitoring system in place to track the status of each server, which means potential issues may go unnoticed until they cause significant problems.

Solutions:
- Implement a comprehensive monitoring solution (e.g., Prometheus, Nagios, or Datadog) to continuously monitor server health, performance metrics, and network traffic.
- Set up alerts to notify administrators of any anomalies or failures in real-time.

### Improved Statements

The infrastructure suffers from several critical issues, including single points of failure (SPOF), security vulnerabilities, and a lack of monitoring. To address these:

- SPOF: Implement redundancy for load balancers, use database clustering with automatic failover, and deploy multiple application servers.
- Security: Ensure all data transmitted over the network is encrypted with SSL/TLS certificates, and install firewalls to block unauthorized IP addresses.
- Monitoring: Implement a robust monitoring system to track server health and performance, and set up alerts for immediate issue detection and response.



