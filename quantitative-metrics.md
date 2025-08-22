# Quantitative Metrics for System Design
## Comprehensive Guide for Performance and Capacity Planning

## 📋 **Table of Contents**

1. [Overview](#overview)
2. [Performance Metrics](#performance-metrics)
3. [Capacity Metrics](#capacity-metrics)
4. [Storage Metrics](#storage-metrics)
5. [Network Metrics](#network-metrics)
6. [Cost Metrics](#cost-metrics)
7. [User Metrics](#user-metrics)
8. [Business Metrics](#business-metrics)
9. [Calculation Examples](#calculation-examples)
10. [Key Takeaways](#key-takeaways)

---

## 📋 **Overview**

### **What are Quantitative Metrics?**
Quantitative metrics provide measurable, numerical data to evaluate system performance, capacity, and efficiency. These metrics are essential for making informed decisions in system design and capacity planning.

### **Why Quantitative Metrics Matter**
- **Objective Decision Making**: Data-driven decisions instead of gut feelings
- **Performance Optimization**: Identify bottlenecks and optimization opportunities
- **Capacity Planning**: Accurate resource provisioning and scaling
- **Cost Optimization**: Balance performance with cost efficiency
- **SLA Compliance**: Ensure service level agreements are met

---

## ⚡ **Performance Metrics**

### **Latency Metrics**

#### **Response Time**
```
Response Time = Processing Time + Network Time + Database Time + Cache Time

Typical Values:
- Web Page Load: 100-500ms
- API Response: 50-200ms
- Database Query: 1-10ms
- Cache Hit: 0.1-1ms
- Network Round Trip: 10-100ms
```

#### **Throughput**
```
Throughput = Requests per Second (RPS) = Total Requests / Time Period

Typical Values:
- Web Server: 1,000-10,000 RPS
- API Gateway: 5,000-50,000 RPS
- Database: 1,000-10,000 queries/sec
- Cache: 100,000-1,000,000 ops/sec
- Message Queue: 10,000-100,000 msgs/sec
```

#### **Concurrency**
```
Concurrent Users = Average Session Time × Requests per Session × Total Users / Time Period

Typical Values:
- Web Application: 10-50% of total users
- API Service: 5-20% of total users
- Real-time System: 80-95% of total users
```

### **Efficiency Metrics**

#### **CPU Utilization**
```
CPU Utilization = (CPU Time Used / Total CPU Time) × 100%

Target Values:
- Production: 60-80%
- Development: 30-50%
- Peak Load: 80-90%
- Critical: >90% (requires scaling)
```

#### **Memory Utilization**
```
Memory Utilization = (Used Memory / Total Memory) × 100%

Target Values:
- Production: 70-85%
- Development: 50-70%
- Peak Load: 85-95%
- Critical: >95% (requires scaling)
```

#### **I/O Utilization**
```
I/O Utilization = (I/O Operations / I/O Capacity) × 100%

Target Values:
- Disk I/O: 60-80%
- Network I/O: 70-85%
- Database I/O: 50-75%
```

---

## 📊 **Capacity Metrics**

### **Storage Capacity**

#### **Data Volume Estimation**
```
Daily Data Volume = Users × Actions per User × Data per Action

Example:
- 1M users × 10 actions/day × 1KB per action = 10GB/day
- 1M users × 100 actions/day × 10KB per action = 1TB/day
```

#### **Storage Growth**
```
Annual Storage Growth = Current Storage × (1 + Growth Rate)^Years

Typical Growth Rates:
- User Content: 50-100% per year
- Logs: 200-500% per year
- Analytics: 300-1000% per year
- Media: 100-300% per year
```

#### **Storage Efficiency**
```
Compression Ratio = Original Size / Compressed Size

Typical Ratios:
- Text Data: 2-5x
- Images: 3-10x
- Video: 10-50x
- Logs: 3-8x
```

### **Processing Capacity**

#### **Computational Requirements**
```
CPU Requirements = Operations per Request × Requests per Second × CPU per Operation

Example:
- 1000 ops/request × 1000 RPS × 0.001 CPU/op = 1000 CPU units
```

#### **Memory Requirements**
```
Memory per User = Session Data + Cache Data + Application Data

Typical Values:
- Web Session: 1-10MB
- Application Cache: 10-100MB
- User Data: 1-100KB
```

---

## 💾 **Storage Metrics**

### **Database Metrics**

#### **Read/Write Ratios**
```
Read/Write Ratio = Read Operations / Write Operations

Typical Ratios:
- Content Sites: 90:10 (90% reads, 10% writes)
- E-commerce: 80:20
- Social Media: 70:30
- Analytics: 95:5
- Gaming: 60:40
```

#### **Query Performance**
```
Average Query Time = Total Query Time / Number of Queries

Target Values:
- Simple Queries: <1ms
- Complex Queries: <10ms
- Analytics Queries: <100ms
- Report Queries: <1s
```

#### **Index Efficiency**
```
Index Hit Ratio = Indexed Queries / Total Queries

Target Values:
- Primary Key: 100%
- Secondary Indexes: 80-95%
- Full-text Search: 70-90%
```

### **Cache Metrics**

#### **Cache Hit Rate**
```
Cache Hit Rate = Cache Hits / (Cache Hits + Cache Misses)

Target Values:
- Application Cache: 80-95%
- CDN Cache: 90-98%
- Database Cache: 85-95%
- Memory Cache: 90-99%
```

#### **Cache Performance**
```
Cache Response Time = Cache Hit Time × Hit Rate + Cache Miss Time × Miss Rate

Typical Values:
- Memory Cache: 0.1-1ms
- Redis: 1-5ms
- CDN: 10-50ms
- Database Cache: 1-10ms
```

---

## 🌐 **Network Metrics**

### **Bandwidth Requirements**

#### **Data Transfer**
```
Bandwidth = Data Size × Requests per Second × 8 bits/byte

Example:
- 1KB per request × 1000 RPS × 8 = 8 Mbps
- 10KB per request × 10000 RPS × 8 = 800 Mbps
```

#### **Network Latency**
```
Network Latency = Propagation Delay + Transmission Delay + Processing Delay

Typical Values:
- Local Network: 0.1-1ms
- Same Region: 1-10ms
- Cross Region: 10-100ms
- Cross Continent: 50-200ms
```

### **Connection Metrics**

#### **Connection Pooling**
```
Optimal Pool Size = (Number of Cores × 2) + Number of Disks

Example:
- 8 cores × 2 + 4 disks = 20 connections
- 16 cores × 2 + 8 disks = 40 connections
```

#### **Connection Utilization**
```
Connection Utilization = Active Connections / Total Connections

Target Values:
- Database: 70-85%
- Web Server: 60-80%
- API Gateway: 50-75%
```

---

## 💰 **Cost Metrics**

### **Infrastructure Costs**

#### **Compute Costs**
```
Monthly Compute Cost = Instance Hours × Hourly Rate × Number of Instances

Example:
- 730 hours × $0.10/hour × 10 instances = $730/month
- 730 hours × $0.50/hour × 100 instances = $36,500/month
```

#### **Storage Costs**
```
Monthly Storage Cost = Storage Size × Cost per GB × Replication Factor

Example:
- 1TB × $0.02/GB × 3 replicas = $60/month
- 10TB × $0.05/GB × 2 replicas = $1,000/month
```

#### **Network Costs**
```
Monthly Network Cost = Data Transfer × Cost per GB

Example:
- 100GB × $0.09/GB = $9/month
- 1TB × $0.08/GB = $80/month
```

### **Operational Costs**

#### **Human Resources**
```
Monthly HR Cost = Number of Engineers × Average Salary / 12

Example:
- 5 engineers × $150,000/year / 12 = $62,500/month
- 20 engineers × $200,000/year / 12 = $333,333/month
```

#### **Maintenance Costs**
```
Monthly Maintenance = Infrastructure Cost × Maintenance Percentage

Typical Values:
- Cloud Services: 5-15%
- On-premises: 20-40%
- Managed Services: 10-25%
```

---

## 👥 **User Metrics**

### **User Activity**

#### **Daily Active Users (DAU)**
```
DAU = Total Users × Daily Activity Rate

Typical Activity Rates:
- Social Media: 60-80%
- E-commerce: 10-30%
- Productivity: 40-70%
- Gaming: 20-50%
- News: 15-40%
```

#### **Monthly Active Users (MAU)**
```
MAU = Total Users × Monthly Activity Rate

Typical Activity Rates:
- Social Media: 80-95%
- E-commerce: 30-60%
- Productivity: 70-90%
- Gaming: 50-80%
- News: 40-70%
```

#### **User Engagement**
```
Session Duration = Total Session Time / Number of Sessions

Typical Values:
- Social Media: 20-60 minutes
- E-commerce: 5-15 minutes
- Productivity: 30-120 minutes
- Gaming: 30-180 minutes
- News: 10-30 minutes
```

### **User Growth**

#### **Growth Rate**
```
Monthly Growth Rate = (Current Users - Previous Users) / Previous Users × 100%

Typical Growth Rates:
- Startups: 10-50% per month
- Established: 5-20% per month
- Mature: 1-10% per month
- Declining: -5 to 5% per month
```

#### **User Retention**
```
Retention Rate = Retained Users / Total Users × 100%

Target Values:
- Day 1: 40-60%
- Day 7: 20-40%
- Day 30: 10-30%
- Day 90: 5-20%
```

---

## 📈 **Business Metrics**

### **Revenue Metrics**

#### **Average Revenue Per User (ARPU)**
```
ARPU = Total Revenue / Number of Users

Typical Values:
- Freemium: $1-10/month
- Subscription: $10-100/month
- E-commerce: $50-500/year
- Enterprise: $100-1000/month
```

#### **Customer Lifetime Value (CLV)**
```
CLV = ARPU × Average Customer Lifespan

Example:
- $10/month × 24 months = $240 CLV
- $50/month × 12 months = $600 CLV
```

### **Operational Metrics**

#### **Cost Per Acquisition (CPA)**
```
CPA = Marketing Spend / Number of New Users

Typical Values:
- Social Media: $1-10
- Search Ads: $5-50
- Content Marketing: $10-100
- Enterprise Sales: $100-1000
```

#### **Churn Rate**
```
Churn Rate = Churned Users / Total Users × 100%

Target Values:
- SaaS: <5% per month
- E-commerce: <10% per month
- Social Media: <15% per month
- Gaming: <20% per month
```

---

## 🔢 **Calculation Examples**

### **Example 1: Social Media Platform**

#### **User Growth Projection**
```
Initial Users: 100,000
Monthly Growth Rate: 20%
Projection Period: 12 months

Month 1: 100,000 × 1.20 = 120,000
Month 2: 120,000 × 1.20 = 144,000
Month 3: 144,000 × 1.20 = 172,800
...
Month 12: 100,000 × (1.20)^12 = 891,610 users
```

#### **Storage Requirements**
```
Daily Data per User: 1MB
Daily Active Rate: 70%
Data Retention: 2 years

Daily Storage = 891,610 × 1MB × 0.70 = 624 MB/day
Annual Storage = 624 MB × 365 = 228 GB/year
Total Storage = 228 GB × 2 years = 456 GB
```

#### **Bandwidth Requirements**
```
Average Request Size: 10KB
Requests per User per Day: 100
Peak Load Factor: 3x

Daily Bandwidth = 891,610 × 10KB × 100 = 8.9 GB/day
Peak Bandwidth = 8.9 GB × 3 / 24 hours = 1.1 Mbps
```

### **Example 2: E-commerce Platform**

#### **Transaction Volume**
```
Daily Orders: 10,000
Average Order Value: $100
Conversion Rate: 2%

Daily Revenue = 10,000 × $100 = $1,000,000
Daily Visitors = 10,000 / 0.02 = 500,000
```

#### **Database Load**
```
Read/Write Ratio: 80:20
Queries per Order: 50
Peak Load Factor: 5x

Daily Queries = 10,000 × 50 = 500,000
Peak Queries per Second = 500,000 × 5 / (24 × 3600) = 29 QPS
```

#### **Storage Growth**
```
Product Images: 1MB per product
Product Catalog: 100,000 products
Image Growth: 50% per year

Initial Storage = 100,000 × 1MB = 100 GB
Year 1 Storage = 100 GB × 1.5 = 150 GB
Year 2 Storage = 150 GB × 1.5 = 225 GB
```

### **Example 3: Video Streaming Service**

#### **Bandwidth Calculation**
```
Video Quality: 1080p (5 Mbps)
Average Watch Time: 30 minutes
Concurrent Users: 10,000

Peak Bandwidth = 10,000 × 5 Mbps = 50 Gbps
Daily Bandwidth = 10,000 × 5 Mbps × 0.5 hours = 25 Gbps-hours
```

#### **Storage Requirements**
```
Video Length: 2 hours
Video Quality: 1080p (5 Mbps)
Catalog Size: 10,000 videos

Storage per Video = 2 hours × 5 Mbps × 3600 seconds = 4.5 GB
Total Storage = 10,000 × 4.5 GB = 45 TB
```

---

## 🎯 **Key Takeaways**

### **Performance Optimization**
1. **Measure First**: Always measure before optimizing
2. **Set Targets**: Define clear performance targets
3. **Monitor Continuously**: Track metrics in real-time
4. **Optimize Incrementally**: Make small, measurable improvements

### **Capacity Planning**
1. **Plan for Growth**: Account for future growth in capacity planning
2. **Use Realistic Estimates**: Base estimates on actual usage patterns
3. **Consider Peaks**: Plan for peak load, not average load
4. **Monitor Trends**: Track usage trends to predict future needs

### **Cost Optimization**
1. **Right-size Resources**: Match resources to actual needs
2. **Use Reserved Instances**: Commit to long-term usage for discounts
3. **Monitor Waste**: Track unused or underutilized resources
4. **Optimize Storage**: Use appropriate storage tiers and compression

### **User Experience**
1. **Focus on Latency**: Users are sensitive to response times
2. **Ensure Reliability**: High availability is crucial for user retention
3. **Scale Gracefully**: Handle traffic spikes without degradation
4. **Monitor Engagement**: Track user behavior and engagement metrics

---

*This guide provides comprehensive quantitative metrics for system design. Use these metrics to make data-driven decisions and optimize your systems.*
