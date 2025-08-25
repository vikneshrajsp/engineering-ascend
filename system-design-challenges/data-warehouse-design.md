---
title: Data Warehouse Design - System Design Challenge
description: Comprehensive solution for data warehouse design system design challenge
layout: default
parent: Data Warehouse Design
grand_parent: System Design Challenges
---

# Design Data Warehouse - System Design Challenge

*Complete interview walkthrough showing the thought process from requirement clarification to detailed solution design, following the RESHADED framework.*

## 🎯 **Interview Walkthrough**

### **Step 1: Requirement Clarification & Scoping**

**Interviewer**: "Design a data warehouse for me."

**My Response**: "Great! Before I start designing, I need to understand the scope and requirements better. Let me ask some clarifying questions:

1. **Scale**: Are we talking about BigQuery scale (100PB+ data) or starting from scratch?
2. **Features**: Which core features should I focus on? ETL pipelines, data modeling, analytics, or all of them?
3. **Data Types**: Structured data, semi-structured, or all data types?
4. **Constraints**: Any specific performance, cost, or technical constraints I should consider?"

**Interviewer**: "Let's start with BigQuery scale and focus on the core features: ETL pipelines, data modeling, analytics, and real-time processing."

**My Response**: "Perfect! So I'm designing a data warehouse at scale with:
- 100PB+ data storage
- Core features: ETL pipelines, data modeling, analytics, real-time processing
- Multiple data types and sources
- Global scale with sub-second query response times

Let me start by identifying the core problems we need to solve."

### **Step 2: Identifying Core Problems**

**My Thought Process**: "From the requirements, I can identify several core problems:

1. **Data Ingestion**: How do we ingest petabytes of data from multiple sources efficiently?
2. **Data Storage**: How do we store and organize massive amounts of data for fast querying?
3. **Data Processing**: How do we process and transform data at massive scale?
4. **Query Performance**: How do we provide sub-second response times for complex analytics?
5. **Data Modeling**: How do we design schemas for optimal query performance?
6. **Real-time Processing**: How do we handle real-time data streams and batch processing?

The crux is balancing data ingestion speed with query performance while maintaining data quality and handling massive scale."

### **Step 3: Back-of-the-Envelope Estimation**

**My Response**: "Let me do some quick calculations to understand the scale:

**Data Scale:**
- Total data: 100PB
- Daily ingestion: 1TB/day new data
- Data sources: 1000+ different sources
- Data types: Structured, semi-structured, unstructured

**Processing Scale:**
- ETL jobs: 1000+ daily ETL jobs
- Peak processing: 100TB/day processing
- Query volume: 1M queries/day
- Peak queries per second: 1M ÷ 86400 × 5 = 58 queries/second

**Storage Scale:**
- Raw data: 100PB
- Processed data: 50PB (after compression and optimization)
- Indexes: 10PB for fast querying
- Metadata: 1PB for data catalog and lineage

**Performance Scale:**
- Query response: <1 second for 95% of queries
- Data ingestion: <1 hour for 95% of data
- ETL processing: <24 hours for 95% of jobs
- Real-time latency: <5 minutes for streaming data

These numbers tell me we need a massively distributed system with intelligent data processing and optimization."

### **Step 4: High-Level Approach**

**My Response**: "Based on the scale, here's my high-level approach:

**Architecture Pattern**: Distributed data processing with intelligent storage
**Data Strategy**: Hybrid storage with columnar optimization and intelligent partitioning
**Processing Strategy**: Batch + streaming processing with intelligent scheduling
**Scaling Strategy**: Horizontal scaling with intelligent data distribution

**Key Design Principles:**
1. **Performance First**: Optimize for fast query response times
2. **Data Quality**: Ensure data accuracy, consistency, and lineage
3. **Scalability**: Design for unlimited data growth
4. **Intelligent Processing**: Use ML for query optimization and data management

Let me break this down into building blocks and explain my choices."

### **Step 5: Building Block Trade-offs & Justification**

**My Response**: "Let me walk through each building block and explain my choices:

#### **1. Data Storage Systems**

**Choice**: Hybrid approach (Columnar Database + Object Storage + Distributed File System)

**Why This Choice:**
- **Columnar Database (BigQuery/Redshift)**: For fast analytical queries and aggregations
- **Object Storage (S3/GCS)**: For raw data storage and archival
- **Distributed File System (HDFS)**: For data processing and intermediate results
- **Metadata Store**: For data catalog, lineage, and governance

**Alternatives Considered:**
- **Single Database**: Would work but can't handle the scale and different data types
- **Traditional RDBMS**: Good for structured data but can't scale to petabytes
- **NoSQL Only**: Could handle scale but lacks analytical capabilities

**Trade-offs:**
- **Complexity**: Managing multiple storage systems vs. single system
- **Performance**: Optimized for each use case vs. one-size-fits-all
- **Cost**: Higher operational cost vs. better performance and scalability

#### **2. Compute & Processing**

**Choice**: Distributed computing with specialized data processing services

**Why This Choice:**
- **ETL Service**: Handle data extraction, transformation, and loading
- **Data Processing Service**: Process and transform data at scale
- **Query Engine**: Execute analytical queries efficiently
- **Streaming Service**: Handle real-time data processing
- **Data Quality Service**: Monitor and maintain data quality

**Alternatives Considered:**
- **Monolithic**: Simpler to develop but impossible to scale to petabytes
- **Serverless**: Good for variable workloads but higher latency for data processing
- **Traditional Servers**: Would work but can't handle the distributed nature

**Trade-offs:**
- **Complexity**: Distributed system complexity vs. operational simplicity
- **Latency**: Network calls between services vs. in-memory calls
- **Scalability**: Independent scaling vs. coupled scaling

#### **3. Message Queuing & Streaming**

**Choice**: Apache Kafka + Apache Flink + Batch processing

**Why This Choice:**
- **Kafka**: For reliable data streaming and event processing
- **Apache Flink**: For real-time stream processing and analytics
- **Batch Processing**: Large-scale data processing and ETL jobs
- **Event Sourcing**: Track all data events for audit and lineage

**Alternatives Considered:**
- **RabbitMQ**: Good for complex routing but higher latency
- **SQS**: Managed service but higher latency than Kafka
- **Direct Communication**: Simpler but can't handle high-throughput data events

**Trade-offs:**
- **Latency**: Stream processing adds latency but provides real-time capabilities
- **Complexity**: Managing streaming vs. simple message delivery
- **Reliability**: Event streaming reliability vs. simple message delivery

#### **4. Networking & Communication**

**Choice**: Global distribution with intelligent data routing

**Why This Choice:**
- **Global Distribution**: Serve users from locations closest to them
- **Intelligent Routing**: Route data processing to optimal regions
- **Load Balancing**: Distribute processing load across multiple services
- **Geographic Optimization**: Optimize for regional data patterns

**Alternatives Considered:**
- **Single Region**: Simpler but higher latency for global users
- **Edge Computing**: Good for static content but limited for data processing
- **Peer-to-Peer**: Could work but complex and unreliable for data

**Trade-offs:**
- **Complexity**: Global distribution complexity vs. operational simplicity
- **Cost**: Higher infrastructure cost vs. better user experience
- **Latency**: Lower latency vs. higher operational complexity

#### **5. Caching & Performance**

**Choice**: Multi-level caching with intelligent optimization

**Why This Choice:**
- **Query Cache**: Cache frequently executed queries and results
- **Data Cache**: Cache frequently accessed data and indexes
- **Metadata Cache**: Cache data catalog and lineage information
- **Result Cache**: Cache query results for fast retrieval

**Alternatives Considered:**
- **Single Cache**: Simpler but less effective for different data types
- **No Caching**: Would work but terrible performance and high costs
- **Application-only Caching**: Good for dynamic data but not for data warehouse

**Trade-offs:**
- **Complexity**: Managing multiple cache layers vs. single layer
- **Memory Usage**: Higher memory cost vs. better performance
- **Consistency**: Cache invalidation complexity vs. performance benefits

#### **6. Security & Authentication**

**Choice**: IAM + Encryption + Data governance

**Why This Choice:**
- **IAM**: Fine-grained access control for data and queries
- **Encryption**: Encrypt data at rest and in transit
- **Data Governance**: Implement data lineage, quality, and compliance
- **Audit Logging**: Track all data access and modifications

**Alternatives Considered:**
- **Basic Authentication**: Simpler but less secure for enterprise data
- **Third-party Security**: Easier to implement but less control
- **No Encryption**: Simpler but completely insecure for sensitive data

**Trade-offs:**
- **Security**: Comprehensive security vs. simpler implementation
- **Complexity**: Security complexity vs. basic protection
- **Performance**: Security overhead vs. security benefits

#### **7. Monitoring & Observability**

**Choice**: Real-time monitoring with data warehouse-specific metrics

**Why This Choice:**
- **Data Quality Metrics**: Monitor data accuracy, completeness, and freshness
- **Query Performance**: Track query response times and throughput
- **ETL Metrics**: Monitor ETL job performance and success rates
- **Storage Metrics**: Track storage usage and optimization

**Alternatives Considered:**
- **Basic Logging**: Simpler but reactive approach
- **Third-party Tools**: Easier to implement but less control over data warehouse metrics
- **Application-only Monitoring**: Good for app performance but not for data quality

**Trade-offs:**
- **Complexity**: Building monitoring vs. using existing tools
- **Cost**: Development cost vs. operational benefits
- **Customization**: Full control vs. out-of-the-box features

#### **8. Scalability & Distribution**

**Choice**: Horizontal scaling with intelligent data partitioning

**Why This Choice:**
- **Data Partitioning**: Partition data by time, region, and business domain
- **Query Distribution**: Distribute queries across multiple processing nodes
- **Geographic Distribution**: Serve users from optimal regions
- **Auto-scaling**: Scale services based on data processing demand

**Alternatives Considered:**
- **Vertical Scaling**: Simpler but limited by hardware
- **Consistent Hashing**: Good for even distribution but complex to implement
- **Static Distribution**: Simpler but can't adapt to changing demand

**Trade-offs:**
- **Complexity**: Intelligent partitioning complexity vs. static distribution
- **Cost**: Higher infrastructure cost vs. better performance
- **Control**: Automated optimization vs. manual control"

### **Step 6: Scaling to Estimated Volume**

**My Response**: "Now let me address how we scale to handle the estimated volume:

#### **Throughput Requirements:**
- **Peak Queries**: 58 queries/second
- **Data Ingestion**: 1TB/day new data
- **ETL Processing**: 1000+ daily ETL jobs
- **Real-time Processing**: 100GB/day streaming data

**Scaling Strategy:**
1. **Data Distribution**: Distribute data across multiple storage systems
2. **Query Distribution**: Distribute queries across multiple processing nodes
3. **Processing Distribution**: Distribute ETL jobs across multiple services
4. **Auto-scaling**: Scale services based on data processing demand

#### **Latency Requirements:**
- **Query Response**: <1 second for 95% of queries
- **Data Ingestion**: <1 hour for 95% of data
- **ETL Processing**: <24 hours for 95% of jobs
- **Real-time Processing**: <5 minutes for streaming data

**Latency Optimization:**
1. **Query Caching**: Cache frequently executed queries and results
2. **Data Optimization**: Optimize data storage and indexing
3. **Parallel Processing**: Process queries and data in parallel
4. **Intelligent Routing**: Route queries to optimal processing nodes

#### **Availability Requirements:**
- **Target**: 99.99% uptime (52 minutes downtime/year)
- **Strategy**: Multi-region deployment with automatic failover
- **Monitoring**: Real-time health checks and alerting
- **Disaster Recovery**: Regional failover and data replication

#### **Storage Requirements:**
- **Current Storage**: 100PB total data
- **Daily Growth**: 1TB/day new data
- **Processing Storage**: 10PB for intermediate results
- **Strategy**: Intelligent tiering and lifecycle management"

### **Step 7: Detailed Building Block Deep-Dive**

**My Response**: "Let me dive deeper into each building block to show the implementation details:

#### **1. Data Ingestion Deep-Dive**

**Problem We're Solving**: Ingest petabytes of data from multiple sources efficiently while maintaining data quality and lineage.

**Ingestion Architecture:**
- **Source Connectors**: Connect to various data sources (databases, APIs, files)
- **Data Validation**: Validate data quality and schema compliance
- **Change Data Capture**: Capture incremental changes for real-time updates
- **Data Lineage**: Track data flow from source to destination

**Ingestion Optimization:**
- **Parallel Ingestion**: Ingest data from multiple sources in parallel
- **Batch Processing**: Process data in batches for efficiency
- **Streaming Ingestion**: Handle real-time data streams
- **Error Handling**: Implement robust error handling and retry mechanisms

#### **2. Data Storage Deep-Dive**

**Problem We're Solving**: Store and organize massive amounts of data for fast querying and analytics.

**Storage Strategy:**
- **Columnar Storage**: Use columnar format for analytical queries
- **Data Partitioning**: Partition data by time, region, and business domain
- **Compression**: Use efficient compression algorithms for storage optimization
- **Indexing**: Create indexes for fast data access and query performance

**Storage Optimization:**
- **Data Clustering**: Cluster related data for optimal query performance
- **Storage Tiering**: Implement intelligent storage tiering
- **Data Lifecycle**: Manage data lifecycle and archival
- **Storage Monitoring**: Monitor storage usage and performance

#### **3. Data Processing Deep-Dive**

**Problem We're Solving**: Process and transform data at massive scale while maintaining quality and performance.

**Processing Architecture:**
- **ETL Pipelines**: Extract, transform, and load data efficiently
- **Data Transformation**: Transform data for business requirements
- **Data Quality**: Monitor and maintain data quality
- **Processing Orchestration**: Orchestrate complex data processing workflows

**Processing Optimization:**
- **Parallel Processing**: Process data in parallel across multiple nodes
- **Intelligent Scheduling**: Schedule jobs based on dependencies and resources
- **Resource Management**: Manage computing resources efficiently
- **Performance Monitoring**: Monitor processing performance and optimization

#### **4. Query Engine Deep-Dive**

**Problem We're Solving**: Provide sub-second response times for complex analytical queries across massive datasets.

**Query Architecture:**
- **Query Optimization**: Optimize queries for best performance
- **Execution Planning**: Plan query execution across multiple nodes
- **Resource Allocation**: Allocate resources for query execution
- **Result Caching**: Cache query results for fast retrieval

**Query Optimization:**
- **Cost-based Optimization**: Use cost-based optimization for query planning
- **Parallel Execution**: Execute queries in parallel across multiple nodes
- **Index Usage**: Optimize index usage for query performance
- **Query Monitoring**: Monitor query performance and optimization

#### **5. Data Modeling Deep-Dive**

**Problem We're Solving**: Design schemas and data models for optimal query performance and business requirements.

**Modeling Strategy:**
- **Dimensional Modeling**: Use dimensional modeling for analytical queries
- **Normalization**: Balance normalization with query performance
- **Denormalization**: Denormalize data for specific query patterns
- **Schema Evolution**: Handle schema changes and evolution

**Modeling Optimization:**
- **Query Patterns**: Design schemas based on common query patterns
- **Performance Testing**: Test schema performance with real queries
- **Iterative Improvement**: Continuously improve schemas based on usage
- **Documentation**: Maintain comprehensive schema documentation"

### **Step 8: System Architecture & Data Flow**

**My Response**: "Let me show you the complete system architecture:

```
┌─────────────────────────────────────────────────────────┐
│                Data Warehouse System                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Data      │    │   Data      │    │   Data      │  │
│   Sources     │    │  Sources    │    │  Sources    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                   │                   │        │
│         └───────────────────┼───────────────────┘        │
│                             │                            │
│                    ┌─────────┴─────────┐                 │
│                    │   Data Ingestion  │                 │
│                    └─────────┬─────────┘                 │
│                              │                            │
│  ┌─────────────┐    ┌─────────┴─────────┐    ┌─────────┐ │
│  │ ETL         │    │   Data             │    │  Query  │ │
│  │ Service     │    │  Processing       │    │ Engine  │ │
│  └─────────────┘    └─────────┬─────────┘    └─────────┘ │
│         │                      │                          │
│         │              ┌───────┴───────┐                  │
│         │              │  Data Quality │                  │
│         │              │  Service      │                  │
│         │              └───────────────┘                  │
│         │                      │                          │
│         └──────────────────────┼──────────────────────────┘
│                                │                            │
│                    ┌───────────┴───────────┐                │
│                    │    Data Layer         │                │
│                    └───────────┬───────────┘                │
│                                │                            │
│  ┌─────────────┐    ┌──────────┴──────────┐    ┌─────────┐ │
│  │ Columnar    │    │   Object            │    │  Metadata│ │
│  │ Database    │    │   Storage           │    │ Store   │ │
│  └─────────────┘    └──────────┬──────────┘    └─────────┘ │
│         │                       │                          │
│         │              ┌───────┴───────┐                  │
│         │              │   Distributed │                  │
│         │              │   File System │                  │
│         │              └───────────────┘                  │
│         │                      │                          │
│         └──────────────────────┼──────────────────────────┘
│                                │                            │
│                    ┌───────────┴───────────┐                │
│                    │   Infrastructure      │                │
│                    └───────────┬───────────┘                │
│                                │                            │
│  ┌─────────────┐    ┌──────────┴──────────┐    ┌─────────┐ │
│  │ Multi-      │    │   Monitoring        │    │  Kafka  │ │
│  │ Region      │    │   & Analytics       │    │ (Events)│ │
│  └─────────────┘    └─────────────────────┘    └─────────┘ │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Data Flow:**
1. **Data Ingestion**: Sources → Ingestion Service → Validation → Storage
2. **Data Processing**: Storage → ETL Service → Processing → Storage
3. **Query Processing**: Client → Query Engine → Optimization → Execution → Results
4. **Data Quality**: Data → Quality Service → Monitoring → Alerts"

### **Step 9: Follow-up Questions & Edge Cases**

**My Response**: "Let me address some potential follow-up questions and edge cases:

#### **Edge Cases:**
1. **Data Quality Issues**: What happens when data quality problems are detected?
   - **Solution**: Automated alerts, data validation, quality monitoring
   - **Monitoring**: Real-time data quality monitoring and alerting

2. **Schema Changes**: How do we handle schema evolution and changes?
   - **Solution**: Schema versioning, backward compatibility, migration tools
   - **Trade-off**: Schema flexibility vs. stability

3. **Query Performance**: How do we handle slow queries and performance issues?
   - **Solution**: Query optimization, resource allocation, performance monitoring
   - **Trade-off**: Query complexity vs. performance

4. **Data Lineage**: How do we track data flow and dependencies?
   - **Solution**: Automated lineage tracking, dependency mapping, impact analysis
   - **Trade-off**: Lineage complexity vs. traceability

#### **Scaling Challenges:**
1. **Data Scaling**: How do we handle unlimited data growth?
   - **Solution**: Intelligent partitioning, lifecycle management, storage optimization
   - **Trade-off**: Storage complexity vs. unlimited scale

2. **Query Scaling**: How do we provide fast queries across massive datasets?
   - **Solution**: Query optimization, parallel execution, intelligent caching
   - **Trade-off**: Query complexity vs. performance

3. **Processing Scaling**: How do we scale ETL and data processing?
   - **Solution**: Distributed processing, intelligent scheduling, resource management
   - **Trade-off**: Processing complexity vs. throughput"

### **Step 10: Summary & Key Takeaways**

**My Response**: "Let me summarize the key design decisions and their rationale:

#### **Key Design Decisions:**
1. **Distributed Architecture**: Scale horizontally across multiple regions
2. **Hybrid Storage**: Different storage systems for different data types
3. **Event-driven Processing**: Use events for data processing and lineage tracking
4. **Intelligent Optimization**: ML-powered query optimization and data management
5. **Global Distribution**: Serve users from optimal regions worldwide

#### **Trade-offs Made:**
1. **Complexity vs. Scale**: Chose complexity for unlimited scalability
2. **Cost vs. Performance**: Higher infrastructure cost for optimal performance
3. **Latency vs. Features**: Balance query speed with advanced analytics
4. **Storage vs. Performance**: Balance storage costs with query performance

#### **Scaling Strategy:**
1. **Horizontal Scaling**: Scale out rather than up across all services
2. **Intelligent Partitioning**: Partition data by time, region, and business domain
3. **Event-driven Architecture**: Use events for data processing and system decoupling
4. **Global Distribution**: Serve users from locations closest to them

This design demonstrates how to build a globally distributed data warehouse that can handle unlimited scale while maintaining sub-second query response times and 99.99% availability."

---

*This interview walkthrough shows the complete thought process from requirement clarification to detailed solution design, demonstrating how to approach data warehouse system design challenges systematically and justify every design decision.*
