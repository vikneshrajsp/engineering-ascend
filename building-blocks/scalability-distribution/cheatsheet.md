---
title: Cheatsheet
layout: default
grand_parent: Building Blocks
parent: Scalability Distribution
---

# Scalability & Distribution Systems - Cheat Sheet
## One-Page Quick Reference for Interviews

## 🎯 **QUICK DECISION FRAMEWORK**

### **When to Use Scaling Types**
```
Scaling Requirements? → Choose Scaling
├─ High Traffic? → Horizontal Scaling
├─ Resource Intensive? → Vertical Scaling
├─ Global Users? → Geographic Distribution
├─ Variable Load? → Auto-scaling
└─ Fault Tolerance? → Redundancy + Replication
```

### **Distribution Strategy Selection**
```
Distribution Needs?
├─ Simple Scaling? → Load Balancing
├─ Service Isolation? → Microservices
├─ Event Processing? → Event-Driven Architecture
├─ Data Consistency? → Consensus Algorithms
└─ Complex Transactions? → Saga Pattern
```

### **Consensus Algorithm Selection**
```
Consensus Requirements?
├─ Simple Agreement? → Basic Consensus
├─ Fault Tolerance? → Paxos/Raft
├─ Byzantine Faults? → Byzantine Fault Tolerance
├─ Performance Critical? → Fast Consensus
└─ Consistency Critical? → Strong Consistency
```

---

## 📈 **SCALING QUICK REFERENCE**

### **Horizontal vs Vertical Scaling**
<div class="table-wrapper">
<table>
<thead>
<tr>
<th>Aspect</th>
<th>Horizontal Scaling</th>
<th>Vertical Scaling</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Approach**</td>
<td>Add more machines</td>
<td>Add more resources</td>
</tr>
<tr>
<td>**Complexity**</td>
<td>High</td>
<td>Low</td>
</tr>
<tr>
<td>**Cost**</td>
<td>Linear</td>
<td>Exponential</td>
</tr>
<tr>
<td>**Fault Tolerance**</td>
<td>High</td>
<td>Low</td>
</tr>
<tr>
<td>**Performance**</td>
<td>Distributed</td>
<td>Centralized</td>
</tr>
<tr>
<td>Strategy</td>
<td>Purpose</td>
<td>Implementation</td>
<td>Benefits</td>
</tr>
<tr>
<td>----------</td>
<td>---------</td>
<td>----------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Stateless Scaling**</td>
<td>Scale services independently</td>
<td>External state management</td>
<td>Linear scaling</td>
</tr>
<tr>
<td>**Data Partitioning**</td>
<td>Distribute data across nodes</td>
<td>Hash/range partitioning</td>
<td>Data locality</td>
</tr>
<tr>
<td>**Service Decomposition**</td>
<td>Break monoliths into services</td>
<td>Microservices architecture</td>
<td>Independent scaling</td>
</tr>
<tr>
<td>**Load Distribution**</td>
<td>Spread load across resources</td>
<td>Load balancers, CDNs</td>
<td>Better performance</td>
</tr>
<tr>
<td>Method</td>
<td>Use Case</td>
<td>Advantages</td>
<td>Disadvantages</td>
</tr>
<tr>
<td>--------</td>
<td>----------</td>
<td>------------</td>
<td>---------------</td>
</tr>
<tr>
<td>**Hash-based**</td>
<td>Even distribution</td>
<td>Balanced load</td>
<td>Range queries difficult</td>
</tr>
<tr>
<td>**Range-based**</td>
<td>Ordered data</td>
<td>Range queries efficient</td>
<td>Uneven distribution</td>
</tr>
<tr>
<td>**Directory-based**</td>
<td>Flexible mapping</td>
<td>Easy rebalancing</td>
<td>Centralized directory</td>
</tr>
<tr>
<td>**Composite**</td>
<td>Complex requirements</td>
<td>Multiple strategies</td>
<td>Increased complexity</td>
</tr>
<tr>
<td>Algorithm</td>
<td>Use Case</td>
<td>Performance</td>
<td>Fairness</td>
</tr>
<tr>
<td>-----------</td>
<td>----------</td>
<td>-------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Round Robin**</td>
<td>Simple distribution</td>
<td>O(1)</td>
<td>Equal</td>
</tr>
<tr>
<td>**Least Connections**</td>
<td>Dynamic load</td>
<td>O(n)</td>
<td>Load-based</td>
</tr>
<tr>
<td>**Weighted Round Robin**</td>
<td>Different capacities</td>
<td>O(1)</td>
<td>Capacity-based</td>
</tr>
<tr>
<td>**IP Hash**</td>
<td>Session affinity</td>
<td>O(1)</td>
<td>Client-based</td>
</tr>
<tr>
<td>Type</td>
<td>Layer</td>
<td>Use Case</td>
<td>Features</td>
</tr>
<tr>
<td>------</td>
<td>-------</td>
<td>----------</td>
<td>----------</td>
</tr>
<tr>
<td>**Application (ALB)**</td>
<td>Layer 7</td>
<td>Web applications</td>
<td>Content-based routing</td>
</tr>
<tr>
<td>**Network (NLB)**</td>
<td>Layer 4</td>
<td>High performance</td>
<td>TCP/UDP support</td>
</tr>
<tr>
<td>**Global (GLB)**</td>
<td>DNS</td>
<td>Geographic distribution</td>
<td>Multi-region</td>
</tr>
<tr>
<td>Type</td>
<td>Purpose</td>
<td>Frequency</td>
<td>Timeout</td>
<td>Action</td>
</tr>
<tr>
<td>------</td>
<td>---------</td>
<td>-----------</td>
<td>---------</td>
<td>--------</td>
</tr>
<tr>
<td>**Liveness**</td>
<td>Is service alive?</td>
<td>30-60s</td>
<td>5-10s</td>
<td>Restart</td>
</tr>
<tr>
<td>**Readiness**</td>
<td>Ready for traffic?</td>
<td>5-10s</td>
<td>1-5s</td>
<td>Remove from LB</td>
</tr>
<tr>
<td>**Startup**</td>
<td>Started successfully?</td>
<td>5-10s</td>
<td>1-5s</td>
<td>Restart</td>
</tr>
<tr>
<td>Strategy</td>
<td>Response Time</td>
<td>Accuracy</td>
<td>Use Case</td>
</tr>
<tr>
<td>----------</td>
<td>---------------</td>
<td>----------</td>
<td>----------</td>
</tr>
<tr>
<td>**Reactive**</td>
<td>1-5 minutes</td>
<td>High</td>
<td>Predictable patterns</td>
</tr>
<tr>
<td>**Predictive**</td>
<td>Pre-emptive</td>
<td>Variable</td>
<td>ML-based prediction</td>
</tr>
<tr>
<td>**Scheduled**</td>
<td>Scheduled</td>
<td>High</td>
<td>Known patterns</td>
</tr>
<tr>
<td>Metric</td>
<td>Threshold (Scale Up)</td>
<td>Threshold (Scale Down)</td>
<td>Window</td>
</tr>
<tr>
<td>--------</td>
<td>---------------------</td>
<td>----------------------</td>
<td>--------</td>
</tr>
<tr>
<td>**CPU Usage**</td>
<td>70-80%</td>
<td>30-40%</td>
<td>5-15 minutes</td>
</tr>
<tr>
<td>**Memory Usage**</td>
<td>80-90%</td>
<td>50-60%</td>
<td>5-15 minutes</td>
</tr>
<tr>
<td>**Request Rate**</td>
<td>Based on capacity</td>
<td>Based on capacity</td>
<td>1-5 minutes</td>
</tr>
<tr>
<td>**Response Time**</td>
<td>Based on SLA</td>
<td>Based on SLA</td>
<td>5-15 minutes</td>
</tr>
<tr>
<td>Benefit</td>
<td>Description</td>
<td>Implementation</td>
</tr>
<tr>
<td>---------</td>
<td>-------------</td>
<td>----------------</td>
</tr>
<tr>
<td>**Cost Optimization**</td>
<td>Pay only for needed resources</td>
<td>Dynamic provisioning</td>
</tr>
<tr>
<td>**Performance**</td>
<td>Maintain performance under load</td>
<td>Automatic scaling</td>
</tr>
<tr>
<td>**Availability**</td>
<td>Handle traffic spikes</td>
<td>Proactive scaling</td>
</tr>
<tr>
<td>**Operational Efficiency**</td>
<td>Reduce manual intervention</td>
<td>Automated scaling</td>
</tr>
<tr>
<td>Pattern</td>
<td>Purpose</td>
<td>Benefits</td>
<td>Challenges</td>
</tr>
<tr>
<td>---------</td>
<td>---------</td>
<td>----------</td>
<td>------------</td>
</tr>
<tr>
<td>**Domain-driven**</td>
<td>Business alignment</td>
<td>Clear ownership</td>
<td>Domain boundaries</td>
</tr>
<tr>
<td>**Bounded Context**</td>
<td>Domain isolation</td>
<td>Simplified models</td>
<td>Context mapping</td>
</tr>
<tr>
<td>**API Gateway**</td>
<td>Client simplification</td>
<td>Single entry point</td>
<td>Gateway bottleneck</td>
</tr>
<tr>
<td>Type</td>
<td>Protocol</td>
<td>Use Case</td>
<td>Performance</td>
</tr>
<tr>
<td>------</td>
<td>----------</td>
<td>----------</td>
<td>-------------</td>
</tr>
<tr>
<td>**Synchronous**</td>
<td>HTTP/REST</td>
<td>Simple requests</td>
<td>Medium</td>
</tr>
<tr>
<td>**High Performance**</td>
<td>gRPC</td>
<td>Internal services</td>
<td>High</td>
</tr>
<tr>
<td>**Flexible**</td>
<td>GraphQL</td>
<td>Complex queries</td>
<td>Variable</td>
</tr>
<tr>
<td>**Asynchronous**</td>
<td>Message Queues</td>
<td>Decoupled services</td>
<td>High</td>
</tr>
<tr>
<td>Pattern</td>
<td>Implementation</td>
<td>Benefits</td>
<td>Challenges</td>
</tr>
<tr>
<td>---------</td>
<td>----------------</td>
<td>----------</td>
<td>------------</td>
</tr>
<tr>
<td>**Client-side**</td>
<td>Client finds services</td>
<td>Direct communication</td>
<td>Client complexity</td>
</tr>
<tr>
<td>**Server-side**</td>
<td>Load balancer finds services</td>
<td>Simple clients</td>
<td>Load balancer dependency</td>
</tr>
<tr>
<td>**Service Registry**</td>
<td>Centralized directory</td>
<td>Service management</td>
<td>Registry availability</td>
</tr>
<tr>
<td>Algorithm</td>
<td>Complexity</td>
<td>Performance</td>
<td>Use Case</td>
</tr>
<tr>
<td>-----------</td>
<td>------------</td>
<td>-------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Paxos**</td>
<td>High</td>
<td>Medium</td>
<td>Distributed databases</td>
</tr>
<tr>
<td>**Raft**</td>
<td>Medium</td>
<td>Medium</td>
<td>General consensus</td>
</tr>
<tr>
<td>**Byzantine**</td>
<td>Very High</td>
<td>Low</td>
<td>Security-critical systems</td>
</tr>
<tr>
<td>Property</td>
<td>Definition</td>
<td>Importance</td>
</tr>
<tr>
<td>----------</td>
<td>------------</td>
<td>------------</td>
</tr>
<tr>
<td>**Safety**</td>
<td>No two nodes decide different values</td>
<td>Consistency</td>
</tr>
<tr>
<td>**Liveness**</td>
<td>Eventually a value is decided</td>
<td>Progress</td>
</tr>
<tr>
<td>**Fault Tolerance**</td>
<td>Works despite node failures</td>
<td>Reliability</td>
</tr>
<tr>
<td>Application</td>
<td>Consensus Use</td>
<td>Benefits</td>
<td>Trade-offs</td>
</tr>
<tr>
<td>-------------</td>
<td>---------------</td>
<td>----------</td>
<td>------------</td>
</tr>
<tr>
<td>**Distributed Databases**</td>
<td>Write consensus</td>
<td>Strong consistency</td>
<td>Performance</td>
</tr>
<tr>
<td>**Service Coordination**</td>
<td>Leader election</td>
<td>Consistent coordination</td>
<td>Overhead</td>
</tr>
<tr>
<td>**Configuration Management**</td>
<td>Config consensus</td>
<td>Consistent config</td>
<td>Complexity</td>
</tr>
<tr>
<td>Pattern</td>
<td>Purpose</td>
<td>Implementation</td>
<td>Benefits</td>
</tr>
<tr>
<td>---------</td>
<td>---------</td>
<td>----------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Shared State**</td>
<td>Multiple nodes access</td>
<td>Centralized storage</td>
<td>Consistency</td>
</tr>
<tr>
<td>**Partitioned State**</td>
<td>Large state distribution</td>
<td>Hash/range partitioning</td>
<td>Scalability</td>
</tr>
<tr>
<td>**Replicated State**</td>
<td>High availability</td>
<td>Multiple copies</td>
<td>Availability</td>
</tr>
<tr>
<td>Model</td>
<td>Guarantees</td>
<td>Performance</td>
<td>Use Case</td>
</tr>
<tr>
<td>-------</td>
<td>------------</td>
<td>-------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Strong Consistency**</td>
<td>Immediate consistency</td>
<td>Low</td>
<td>Critical data</td>
</tr>
<tr>
<td>**Eventual Consistency**</td>
<td>Eventually consistent</td>
<td>High</td>
<td>User data</td>
</tr>
<tr>
<td>**Causal Consistency**</td>
<td>Causally consistent</td>
<td>Medium</td>
<td>Social applications</td>
</tr>
<tr>
<td>Strategy</td>
<td>Purpose</td>
<td>Implementation</td>
<td>Benefits</td>
</tr>
<tr>
<td>----------</td>
<td>---------</td>
<td>----------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Hash Partitioning**</td>
<td>Even distribution</td>
<td>Consistent hashing</td>
<td>Balanced load</td>
</tr>
<tr>
<td>**Range Partitioning**</td>
<td>Ordered access</td>
<td>Key ranges</td>
<td>Range queries</td>
</tr>
<tr>
<td>**Replication**</td>
<td>High availability</td>
<td>Multiple copies</td>
<td>Fault tolerance</td>
</tr>
<tr>
<td>Scaling Type</td>
<td>Performance Gain</td>
<td>Cost</td>
<td>Complexity</td>
</tr>
<tr>
<td>--------------</td>
<td>------------------</td>
<td>------</td>
<td>------------</td>
</tr>
<tr>
<td>**Horizontal**</td>
<td>Linear scaling</td>
<td>Linear</td>
<td>High</td>
</tr>
<tr>
<td>**Vertical**</td>
<td>Limited by hardware</td>
<td>Exponential</td>
<td>Low</td>
</tr>
<tr>
<td>**Auto-scaling**</td>
<td>Dynamic scaling</td>
<td>Variable</td>
<td>Medium</td>
</tr>
<tr>
<td>**Load Balancing**</td>
<td>Better distribution</td>
<td>Low</td>
<td>Medium</td>
</tr>
<tr>
<td>Component</td>
<td>Performance Impact</td>
<td>Optimization</td>
<td>Monitoring</td>
</tr>
<tr>
<td>-----------</td>
<td>-------------------</td>
<td>--------------</td>
<td>------------</td>
</tr>
<tr>
<td>**Network Communication**</td>
<td>Latency overhead</td>
<td>Service locality</td>
<td>Network monitoring</td>
</tr>
<tr>
<td>**Consensus Algorithms**</td>
<td>Coordination overhead</td>
<td>Efficient algorithms</td>
<td>Consensus monitoring</td>
</tr>
<tr>
<td>**State Management**</td>
<td>Consistency overhead</td>
<td>Appropriate models</td>
<td>State monitoring</td>
</tr>
<tr>
<td>**Service Discovery**</td>
<td>Lookup overhead</td>
<td>Caching</td>
<td>Discovery monitoring</td>
</tr>
<tr>
<td>Vulnerability</td>
<td>Impact</td>
<td>Prevention</td>
<td>Detection</td>
</tr>
<tr>
<td>---------------</td>
<td>--------</td>
<td>------------</td>
<td>-----------</td>
</tr>
<tr>
<td>**Premature Optimization**</td>
<td>Wasted effort</td>
<td>Measure first</td>
<td>Performance monitoring</td>
</tr>
<tr>
<td>**Over-engineering**</td>
<td>Complexity</td>
<td>Start simple</td>
<td>Architecture reviews</td>
</tr>
<tr>
<td>**Single Point of Failure**</td>
<td>System downtime</td>
<td>Redundancy</td>
<td>Failure testing</td>
</tr>
<tr>
<td>**Poor Load Distribution**</td>
<td>Uneven load</td>
<td>Proper load balancing</td>
<td>Load monitoring</td>
</tr>
<tr>
<td>Vulnerability</td>
<td>Impact</td>
<td>Prevention</td>
<td>Detection</td>
</tr>
<tr>
<td>---------------</td>
<td>--------</td>
<td>------------</td>
<td>-----------</td>
</tr>
<tr>
<td>**Network Partitions**</td>
<td>Inconsistency</td>
<td>Partition tolerance</td>
<td>Network monitoring</td>
</tr>
<tr>
<td>**Consensus Failures**</td>
<td>No progress</td>
<td>Proper consensus</td>
<td>Consensus monitoring</td>
</tr>
<tr>
<td>**State Inconsistency**</td>
<td>Data corruption</td>
<td>Consistency models</td>
<td>Data validation</td>
</tr>
<tr>
<td>**Service Dependencies**</td>
<td>Cascading failures</td>
<td>Circuit breakers</td>
<td>Dependency monitoring</td>
</tr>
<tr>
<td>Use Case</td>
<td>Primary Scaling</td>
<td>Secondary Scaling</td>
<td>Key Decision Factors</td>
</tr>
<tr>
<td>----------</td>
<td>----------------</td>
<td>------------------</td>
<td>---------------------</td>
</tr>
<tr>
<td>**Web Application**</td>
<td>Horizontal scaling</td>
<td>Load balancing</td>
<td>Traffic distribution + performance</td>
</tr>
<tr>
<td>**API Service**</td>
<td>Auto-scaling</td>
<td>Load balancing</td>
<td>Variable load + response time</td>
</tr>
<tr>
<td>**Database System**</td>
<td>Vertical scaling</td>
<td>Horizontal scaling</td>
<td>Data consistency + performance</td>
</tr>
<tr>
<td>**Microservices**</td>
<td>Service scaling</td>
<td>Load balancing</td>
<td>Independent scaling + communication</td>
</tr>
<tr>
<td>**Real-time System**</td>
<td>Horizontal scaling</td>
<td>Load balancing</td>
<td>Low latency + high throughput</td>
</tr>
<tr>
<td>**Batch Processing**</td>
<td>Horizontal scaling</td>
<td>Auto-scaling</td>
<td>Resource utilization + cost</td>
</tr>
<tr>
<td>System Type</td>
<td>Load Balancing</td>
<td>Consensus</td>
<td>State Management</td>
</tr>
<tr>
<td>-------------</td>
<td>----------------</td>
<td>-----------</td>
<td>------------------</td>
</tr>
<tr>
<td>**Monolithic**</td>
<td>Simple load balancing</td>
<td>Basic consensus</td>
<td>Centralized state</td>
</tr>
<tr>
<td>**Microservices**</td>
<td>Service mesh</td>
<td>Service coordination</td>
<td>Distributed state</td>
</tr>
<tr>
<td>**Event-driven**</td>
<td>Message routing</td>
<td>Event ordering</td>
<td>Event sourcing</td>
</tr>
<tr>
<td>**Real-time**</td>
<td>Low-latency LB</td>
<td>Fast consensus</td>
<td>In-memory state</td>
</tr>
<tr>
<td>**Batch Processing**</td>
<td>Job distribution</td>
<td>Job coordination</td>
<td>Shared state</td>
</tr>
<tr>
<td>Metric</td>
<td>Target</td>
<td>Monitoring</td>
<td>Optimization</td>
</tr>
<tr>
<td>--------</td>
<td>--------</td>
<td>------------</td>
<td>--------------</td>
</tr>
<tr>
<td>**Throughput**</td>
<td>1000+ requests/sec</td>
<td>Request rate monitoring</td>
<td>Load balancing</td>
</tr>
<tr>
<td>**Latency**</td>
<td><100ms response time</td>
<td>Response time monitoring</td>
<td>Caching, optimization</td>
</tr>
<tr>
<td>**Availability**</td>
<td>99.9%+ uptime</td>
<td>Uptime monitoring</td>
<td>Redundancy, health checks</td>
</tr>
<tr>
<td>**Scalability**</td>
<td>Linear scaling</td>
<td>Scaling metrics</td>
<td>Proper architecture</td>
</tr>
<tr>
<td>Metric</td>
<td>Target</td>
<td>Monitoring</td>
<td>Optimization</td>
</tr>
<tr>
<td>--------</td>
<td>--------</td>
<td>------------</td>
<td>--------------</td>
</tr>
<tr>
<td>**Network Latency**</td>
<td><10ms inter-service</td>
<td>Network monitoring</td>
<td>Service locality</td>
</tr>
<tr>
<td>**Consensus Time**</td>
<td><100ms agreement</td>
<td>Consensus monitoring</td>
<td>Efficient algorithms</td>
</tr>
<tr>
<td>**State Consistency**</td>
<td><1s consistency</td>
<td>State monitoring</td>
<td>Appropriate models</td>
</tr>
<tr>
<td>**Service Discovery**</td>
<td><1s lookup time</td>
<td>Discovery monitoring</td>
<td>Caching, optimization</td>
</tr>
</tbody>
</table>
</div>
---

## 🎯 **50 SCALING INTERVIEW QUESTIONS**

### **Scaling Fundamentals**
1. **How would you design a scalable system?**
2. **What's the difference between horizontal and vertical scaling?**
3. **When would you choose horizontal vs vertical scaling?**
4. **How do you measure system scalability?**
5. **What are the limits of scaling?**

### **Load Balancing Questions**
6. **How do you design a load balancer?**
7. **What load balancing algorithms do you know?**
8. **How do you handle session affinity?**
9. **How do you implement health checks?**
10. **How do you handle load balancer failures?**

### **Auto-scaling Questions**
11. **How do you design an auto-scaling system?**
12. **What metrics do you use for auto-scaling?**
13. **How do you prevent scaling thrashing?**
14. **How do you handle scaling during failures?**
15. **How do you optimize auto-scaling costs?**

### **Microservices Questions**
16. **How do you decompose a monolith into microservices?**
17. **How do services communicate in a microservices architecture?**
18. **How do you handle service discovery?**
19. **How do you manage distributed transactions?**
20. **How do you handle service failures?**

### **Consensus Questions**
21. **How do you implement distributed consensus?**
22. **What's the difference between Paxos and Raft?**
23. **How do you handle Byzantine failures?**
24. **How do you optimize consensus performance?**
25. **How do you handle consensus failures?**

### **State Management Questions**
26. **How do you manage state in distributed systems?**
27. **What consistency models do you know?**
28. **How do you handle state partitioning?**
29. **How do you handle state replication?**
30. **How do you handle state conflicts?**

### **Performance Questions**
31. **How do you optimize system performance?**
32. **How do you identify performance bottlenecks?**
33. **How do you handle high traffic?**
34. **How do you optimize network communication?**
35. **How do you handle resource contention?**

### **Fault Tolerance Questions**
36. **How do you design for fault tolerance?**
37. **How do you handle node failures?**
38. **How do you implement circuit breakers?**
39. **How do you handle cascading failures?**
40. **How do you implement retry logic?**

### **Monitoring Questions**
41. **How do you monitor distributed systems?**
42. **How do you track system performance?**
43. **How do you handle monitoring at scale?**
44. **How do you implement alerting?**
45. **How do you handle monitoring failures?**

### **Advanced Questions**
46. **How do you handle global distribution?**
47. **How do you implement edge computing?**
48. **How do you handle multi-cloud scaling?**
49. **How do you implement serverless scaling?**
50. **How do you handle quantum-resistant scaling?**

---

## ❓ **FREQUENTLY ASKED QUESTIONS (FAQs)**

### **Common Misconceptions & Quick Answers**

#### **Q1: "Scaling is just adding more servers"**
**A: FALSE** - Scaling requires proper architecture and design:
- **Load Distribution**: Need proper load balancing
- **State Management**: Need distributed state management
- **Consistency**: Need consensus for consistency
- **Monitoring**: Need comprehensive monitoring

#### **Q2: "Horizontal scaling is always better than vertical"**
**A: FALSE** - Each has its place:
- **Vertical Scaling**: Better for simple systems, lower complexity
- **Horizontal Scaling**: Better for complex systems, higher fault tolerance
- **Hybrid Approach**: Often the best solution
- **Cost Considerations**: Vertical scaling can be more cost-effective initially

#### **Q3: "Auto-scaling solves all scaling problems"**
**A: FALSE** - Auto-scaling has limitations:
- **Configuration**: Requires careful configuration
- **Predictability**: May not handle unpredictable load
- **Cost**: Can lead to unexpected costs
- **Complexity**: Adds operational complexity

#### **Q4: "Consensus is only for databases"**
**A: FALSE** - Consensus has many applications:
- **Service Coordination**: Leader election, configuration management
- **Distributed Systems**: State replication, fault tolerance
- **Blockchain**: Distributed ledger consensus
- **IoT Systems**: Device coordination

#### **Q5: "State management is simple in distributed systems"**
**A: FALSE** - Distributed state is complex:
- **Consistency**: Trade-offs between consistency and performance
- **Partitioning**: Complex data partitioning strategies
- **Replication**: Multiple replication strategies
- **Conflicts**: Complex conflict resolution

---

*Use this cheatsheet for quick reference during interviews. Remember: scaling and distribution are essential for modern systems.*
