---
title: Cheatsheet
layout: default
grand_parent: Building Blocks
parent: Monitoring Observability
---

# Monitoring & Observability Systems - Cheat Sheet
## One-Page Quick Reference for Interviews

## 🎯 **QUICK DECISION FRAMEWORK**

### **When to Use Monitoring Types**
```
Monitoring Needs? → Choose Monitoring
├─ Performance Issues? → Application Performance Monitoring
├─ Infrastructure Problems? → Infrastructure Monitoring
├─ Security Threats? → Security Monitoring
├─ Business Insights? → Business Intelligence
└─ Distributed Systems? → Distributed Tracing
```

### **Observability Strategy Selection**
```
Observability Requirements?
├─ Basic Monitoring? → Metrics + Logs
├─ Debugging Needs? → Metrics + Logs + Traces
├─ Performance Analysis? → Metrics + Logs + Traces + Profiling
├─ Full Observability? → All pillars + advanced analytics
└─ Compliance Required? → Audit logging + compliance monitoring
```

---

## 📊 **OBSERVABILITY QUICK REFERENCE**

### **Three Pillars of Observability**
<div class="table-wrapper">
<table>
<thead>
<tr>
<th>Pillar</th>
<th>Purpose</th>
<th>Data Type</th>
<th>Performance Impact</th>
<th>Use Case</th>
</tr>
</thead>
<tbody>
<tr>
<td>**Logs**</td>
<td>Event recording</td>
<td>Structured events</td>
<td>Low</td>
<td>Debugging, audit</td>
</tr>
<tr>
<td>**Metrics**</td>
<td>Performance measurement</td>
<td>Time-series data</td>
<td>Very Low</td>
<td>Monitoring, alerting</td>
</tr>
<tr>
<td>**Traces**</td>
<td>Request tracking</td>
<td>Distributed spans</td>
<td>Medium</td>
<td>Performance debugging</td>
</tr>
<tr>
<td>Level</td>
<td>Volume</td>
<td>Value</td>
<td>Use Case</td>
<td>Storage Impact</td>
</tr>
<tr>
<td>-------</td>
<td>--------</td>
<td>-------</td>
<td>----------</td>
<td>----------------</td>
</tr>
<tr>
<td>**DEBUG**</td>
<td>80%</td>
<td>20%</td>
<td>Development</td>
<td>High</td>
</tr>
<tr>
<td>**INFO**</td>
<td>15%</td>
<td>30%</td>
<td>Normal operations</td>
<td>Medium</td>
</tr>
<tr>
<td>**WARN**</td>
<td>3%</td>
<td>25%</td>
<td>Potential issues</td>
<td>Low</td>
</tr>
<tr>
<td>**ERROR**</td>
<td>2%</td>
<td>25%</td>
<td>Actual errors</td>
<td>Low</td>
</tr>
<tr>
<td>**FATAL**</td>
<td><1%</td>
<td>High</td>
<td>Critical failures</td>
<td>Minimal</td>
</tr>
<tr>
<td>Type</td>
<td>Purpose</td>
<td>Example</td>
<td>Storage</td>
<td>Analysis</td>
</tr>
<tr>
<td>------</td>
<td>---------</td>
<td>---------</td>
<td>---------</td>
<td>----------</td>
</tr>
<tr>
<td>**Counter**</td>
<td>Cumulative values</td>
<td>Request count</td>
<td>Minimal</td>
<td>Rate calculation</td>
</tr>
<tr>
<td>**Gauge**</td>
<td>Current values</td>
<td>CPU usage</td>
<td>Medium</td>
<td>Current state</td>
</tr>
<tr>
<td>**Histogram**</td>
<td>Distribution</td>
<td>Response time</td>
<td>High</td>
<td>Percentiles</td>
</tr>
<tr>
<td>**Summary**</td>
<td>Statistical summary</td>
<td>Request duration</td>
<td>Medium</td>
<td>Averages</td>
</tr>
<tr>
<td>Strategy</td>
<td>Advantages</td>
<td>Disadvantages</td>
<td>Use Case</td>
<td>Performance Impact</td>
</tr>
<tr>
<td>----------</td>
<td>------------</td>
<td>---------------</td>
<td>----------</td>
<td>-------------------</td>
</tr>
<tr>
<td>**Head-based**</td>
<td>Complete traces</td>
<td>May miss important</td>
<td>Performance monitoring</td>
<td>5-10% overhead</td>
</tr>
<tr>
<td>**Tail-based**</td>
<td>Captures errors</td>
<td>Incomplete traces</td>
<td>Error analysis</td>
<td>10-20% overhead</td>
</tr>
<tr>
<td>**Adaptive**</td>
<td>Balances visibility</td>
<td>Complex</td>
<td>Production systems</td>
<td>1-5% overhead</td>
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
<td>Purpose</td>
<td>Implementation</td>
<td>Use Case</td>
</tr>
<tr>
<td>----------</td>
<td>---------</td>
<td>----------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Threshold-based**</td>
<td>Static limits</td>
<td>Fixed values</td>
<td>Basic monitoring</td>
</tr>
<tr>
<td>**Dynamic**</td>
<td>Adaptive limits</td>
<td>Historical data</td>
<td>Variable systems</td>
</tr>
<tr>
<td>**Anomaly Detection**</td>
<td>Unusual patterns</td>
<td>ML algorithms</td>
<td>Complex systems</td>
</tr>
<tr>
<td>**Correlation**</td>
<td>Related alerts</td>
<td>Pattern matching</td>
<td>Incident response</td>
</tr>
<tr>
<td>Level</td>
<td>Response Time</td>
<td>Notification</td>
<td>Escalation</td>
</tr>
<tr>
<td>-------</td>
<td>---------------</td>
<td>--------------</td>
<td>------------</td>
</tr>
<tr>
<td>**Info**</td>
<td>24 hours</td>
<td>Email</td>
<td>None</td>
</tr>
<tr>
<td>**Warning**</td>
<td>4 hours</td>
<td>Email, Slack</td>
<td>Team lead</td>
</tr>
<tr>
<td>**Critical**</td>
<td>15 minutes</td>
<td>Phone, SMS</td>
<td>On-call engineer</td>
</tr>
<tr>
<td>**Fatal**</td>
<td>5 minutes</td>
<td>Phone, SMS, Pager</td>
<td>Manager</td>
</tr>
<tr>
<td>Type</td>
<td>Audience</td>
<td>Focus</td>
<td>Metrics</td>
</tr>
<tr>
<td>------</td>
<td>----------</td>
<td>-------</td>
<td>---------</td>
</tr>
<tr>
<td>**Operational**</td>
<td>Engineers</td>
<td>System health</td>
<td>Performance, errors</td>
</tr>
<tr>
<td>**Business**</td>
<td>Executives</td>
<td>Business metrics</td>
<td>Revenue, users</td>
</tr>
<tr>
<td>**Technical**</td>
<td>Developers</td>
<td>Code performance</td>
<td>Latency, throughput</td>
</tr>
<tr>
<td>Technique</td>
<td>Use Case</td>
<td>Implementation</td>
<td>Benefits</td>
</tr>
<tr>
<td>-----------</td>
<td>----------</td>
<td>----------------</td>
<td>----------</td>
</tr>
<tr>
<td>**Time Series**</td>
<td>Trends over time</td>
<td>Line charts</td>
<td>Pattern identification</td>
</tr>
<tr>
<td>**Heatmaps**</td>
<td>Multi-dimensional</td>
<td>Color-coded grids</td>
<td>Correlation analysis</td>
</tr>
<tr>
<td>**Gauges**</td>
<td>Current values</td>
<td>Circular indicators</td>
<td>Quick status</td>
</tr>
<tr>
<td>**Tables**</td>
<td>Detailed data</td>
<td>Sortable tables</td>
<td>Deep analysis</td>
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
<td>**Metrics Collection**</td>
<td>1-5% CPU</td>
<td>Sampling</td>
<td>Collection rate</td>
</tr>
<tr>
<td>**Log Processing**</td>
<td>5-15% CPU</td>
<td>Async processing</td>
<td>Processing latency</td>
</tr>
<tr>
<td>**Tracing**</td>
<td>5-10% latency</td>
<td>Sampling</td>
<td>Trace overhead</td>
</tr>
<tr>
<td>**Health Checks**</td>
<td><1% overhead</td>
<td>Efficient checks</td>
<td>Check duration</td>
</tr>
<tr>
<td>Aspect</td>
<td>Challenge</td>
<td>Solution</td>
<td>Performance</td>
</tr>
<tr>
<td>--------</td>
<td>-----------</td>
<td>----------</td>
<td>-------------</td>
</tr>
<tr>
<td>**Data Volume**</td>
<td>High volume</td>
<td>Sampling, aggregation</td>
<td>1M+ events/sec</td>
</tr>
<tr>
<td>**Storage**</td>
<td>Large datasets</td>
<td>Compression, retention</td>
<td>10-100x compression</td>
</tr>
<tr>
<td>**Queries**</td>
<td>Slow queries</td>
<td>Indexing, caching</td>
<td>Sub-second response</td>
</tr>
<tr>
<td>**Real-time**</td>
<td>High latency</td>
<td>Streaming, caching</td>
<td><1 second latency</td>
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
<td>**Alert Fatigue**</td>
<td>Missed alerts</td>
<td>Reduce noise</td>
<td>Alert metrics</td>
</tr>
<tr>
<td>**False Positives**</td>
<td>Wasted time</td>
<td>Tune thresholds</td>
<td>Alert analysis</td>
</tr>
<tr>
<td>**Incomplete Coverage**</td>
<td>Blind spots</td>
<td>Comprehensive monitoring</td>
<td>Gap analysis</td>
</tr>
<tr>
<td>**Performance Impact**</td>
<td>System degradation</td>
<td>Efficient collection</td>
<td>Performance monitoring</td>
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
<td>**High Cardinality**</td>
<td>Storage explosion</td>
<td>Limit dimensions</td>
<td>Cardinality monitoring</td>
</tr>
<tr>
<td>**Sampling Issues**</td>
<td>Lost data</td>
<td>Appropriate sampling</td>
<td>Sampling validation</td>
</tr>
<tr>
<td>**Correlation Failures**</td>
<td>Debugging difficulty</td>
<td>Consistent IDs</td>
<td>Trace validation</td>
</tr>
<tr>
<td>**Data Retention**</td>
<td>Compliance issues</td>
<td>Proper retention</td>
<td>Retention monitoring</td>
</tr>
<tr>
<td>Use Case</td>
<td>Primary Monitoring</td>
<td>Secondary Monitoring</td>
<td>Key Decision Factors</td>
</tr>
<tr>
<td>----------</td>
<td>-------------------</td>
<td>---------------------</td>
<td>---------------------</td>
</tr>
<tr>
<td>**Web Application**</td>
<td>Application metrics</td>
<td>Infrastructure monitoring</td>
<td>User experience + performance</td>
</tr>
<tr>
<td>**Microservices**</td>
<td>Distributed tracing</td>
<td>Service metrics</td>
<td>Request flow + service health</td>
</tr>
<tr>
<td>**Database System**</td>
<td>Performance metrics</td>
<td>Query analysis</td>
<td>Throughput + latency</td>
</tr>
<tr>
<td>**API Service**</td>
<td>Response times</td>
<td>Error rates</td>
<td>SLA compliance + reliability</td>
</tr>
<tr>
<td>**Security System**</td>
<td>Security events</td>
<td>Access monitoring</td>
<td>Threat detection + compliance</td>
</tr>
<tr>
<td>**Business System**</td>
<td>Business metrics</td>
<td>Operational metrics</td>
<td>Revenue + user engagement</td>
</tr>
<tr>
<td>Standard</td>
<td>Requirements</td>
<td>Implementation</td>
</tr>
<tr>
<td>----------</td>
<td>-------------</td>
<td>----------------</td>
</tr>
<tr>
<td>**SOX**</td>
<td>Audit trails</td>
<td>Comprehensive logging</td>
</tr>
<tr>
<td>**HIPAA**</td>
<td>Access monitoring</td>
<td>User activity tracking</td>
</tr>
<tr>
<td>**PCI DSS**</td>
<td>Security monitoring</td>
<td>Security event logging</td>
</tr>
<tr>
<td>**GDPR**</td>
<td>Data processing</td>
<td>Privacy monitoring</td>
</tr>
</tbody>
</table>
</div>
---

## 📊 **MONITORING & ALERTING**

### **Key Monitoring Metrics**
- **System Health**: 99.9%+ uptime
- **Performance**: <100ms response time
- **Error Rates**: <1% error rate
- **Throughput**: 1000+ requests/second
- **Resource Usage**: <80% CPU/memory usage

### **Alerting Thresholds**
- **System Down**: Immediate alert
- **High Error Rate**: >5% error rate
- **Performance Degradation**: >200ms response time
- **Resource Exhaustion**: >90% CPU/memory usage
- **Security Incidents**: Immediate alert

---

## 🎯 **50 MONITORING INTERVIEW QUESTIONS**

### **Monitoring Fundamentals**
1. **How would you design a monitoring system?**
2. **What are the three pillars of observability?**
3. **How do you choose between different monitoring tools?**
4. **What's the difference between monitoring and observability?**
5. **How do you handle monitoring at scale?**

### **Metrics Questions**
6. **What types of metrics should you collect?**
7. **How do you handle high cardinality metrics?**
8. **What's the difference between pull and push models?**
9. **How do you design metric naming conventions?**
10. **How do you handle metric storage and retention?**

### **Logging Questions**
11. **How do you implement structured logging?**
12. **What's the difference between log levels?**
13. **How do you handle log aggregation?**
14. **How do you implement log correlation?**
15. **How do you handle log retention and archival?**

### **Tracing Questions**
16. **How do you implement distributed tracing?**
17. **What sampling strategies should you use?**
18. **How do you propagate trace context?**
19. **How do you analyze trace data?**
20. **How do you handle trace storage?**

### **Health Checks Questions**
21. **What types of health checks should you implement?**
22. **How do you design health check endpoints?**
23. **How do you handle health check failures?**
24. **How do you implement health check aggregation?**
25. **How do you handle health check performance?**

### **Alerting Questions**
26. **How do you design an alerting system?**
27. **How do you reduce alert fatigue?**
28. **How do you implement alert correlation?**
29. **How do you handle alert escalation?**
30. **How do you design alert suppression?**

### **Dashboard Questions**
31. **How do you design monitoring dashboards?**
32. **What types of visualizations should you use?**
33. **How do you implement real-time dashboards?**
34. **How do you handle dashboard performance?**
35. **How do you design role-based dashboards?**

### **Performance Questions**
36. **How do you minimize monitoring overhead?**
37. **How do you handle monitoring at scale?**
38. **How do you optimize monitoring queries?**
39. **How do you handle monitoring data retention?**
40. **How do you implement monitoring caching?**

### **Compliance Questions**
41. **How do you implement audit logging?**
42. **How do you handle compliance monitoring?**
43. **How do you implement data retention policies?**
44. **How do you handle security monitoring?**
45. **How do you implement privacy monitoring?**

### **Advanced Questions**
46. **How do you implement anomaly detection?**
47. **How do you handle ML-based monitoring?**
48. **How do you implement predictive monitoring?**
49. **How do you handle multi-cloud monitoring?**
50. **How do you implement monitoring automation?**

---

## ❓ **FREQUENTLY ASKED QUESTIONS (FAQs)**

### **Common Misconceptions & Quick Answers**

#### **Q1: "Monitoring is too expensive"**
**A: FALSE** - Monitoring is an investment that prevents costly outages:
- **Cost of Outage**: $300K+ average cost per hour of downtime
- **Monitoring Investment**: 1-3% of infrastructure cost typically sufficient
- **ROI**: Monitoring investments typically pay for themselves

#### **Q2: "Logs are enough for monitoring"**
**A: FALSE** - Logs alone are insufficient for comprehensive monitoring:
- **Log Limitations**: Logs don't provide real-time metrics
- **Observability Need**: Need metrics and traces for full observability
- **Best Practice**: Implement all three pillars (logs, metrics, traces)

#### **Q3: "Alert on everything"**
**A: FALSE** - Too many alerts cause alert fatigue:
- **Alert Fatigue**: 90%+ of alerts are ignored when there are too many
- **Best Practice**: Alert only on actionable issues
- **Strategy**: Use correlation and suppression to reduce noise

#### **Q4: "Monitoring has no performance impact"**
**A: FALSE** - Monitoring has overhead that must be considered:
- **Performance Impact**: 1-15% overhead depending on implementation
- **Optimization**: Use sampling and efficient collection
- **Trade-off**: Balance visibility with performance

#### **Q5: "Set up monitoring once and forget it"**
**A: FALSE** - Monitoring requires ongoing maintenance:
- **Evolving Systems**: Systems change, monitoring must adapt
- **Tuning Required**: Alerts and thresholds need regular tuning
- **Maintenance**: Regular review and optimization needed

---

*Use this cheatsheet for quick reference during interviews. Remember: monitoring and observability are essential for production systems.*
