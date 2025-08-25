---
title: Cheatsheet
layout: default
grand_parent: Building Blocks
parent: Security Authentication
---

# Security & Authentication Systems - Cheat Sheet
## One-Page Quick Reference for Interviews

## 🎯 **QUICK DECISION FRAMEWORK**

### **When to Use Authentication Types**
```
Security Requirements? → Choose Authentication
├─ High Security? → Multi-Factor Authentication
├─ User Convenience? → Biometric Authentication
├─ Third-Party Access? → OAuth 2.0
├─ Enterprise Integration? → SAML
└─ Stateless Systems? → JWT
```

### **Authorization Model Selection**
```
Access Control Needs?
├─ Simple Roles? → RBAC
├─ Complex Policies? → ABAC
├─ Dynamic Rules? → PBAC
├─ Fine-Grained Control? → ACLs
└─ Hybrid Requirements? → Combined Models
```

### **Security Level Selection**
```
Security Level Required?
├─ Basic Security? → Password + HTTPS
├─ Enhanced Security? → MFA + Encryption
├─ High Security? → Zero Trust + Advanced Monitoring
├─ Compliance Required? → Audit Logging + Compliance Tools
└─ Critical Systems? → Defense in Depth + Redundancy
```

---

## 🔐 **AUTHENTICATION QUICK REFERENCE**

### **Authentication Methods**
| Method | Security | User Experience | Implementation | Use Case |
|--------|----------|-----------------|----------------|----------|
| **Password** | Low | Good | Simple | Basic systems |
| **MFA (TOTP)** | High | Good | Medium | High security |
| **Biometric** | High | Excellent | Complex | Mobile devices |
| **OAuth 2.0** | High | Good | Complex | Third-party access |
| **SAML** | High | Good | Complex | Enterprise SSO |
| **JWT** | Medium | Good | Simple | Stateless systems |

### **Password Security Levels**
| Method | Security Level | Attack Resistance | Storage Overhead |
|--------|---------------|------------------|------------------|
| **Plain Text** | 0% | None | Minimal |
| **Simple Hash** | 20% | Rainbow tables | Minimal |
| **Salted Hash** | 60% | Dictionary attacks | Low |
| **Adaptive Hash** | 80% | Brute force | Medium |
| **Password Manager** | 95% | Most attacks | None |

### **MFA Factor Types**
| Factor | Examples | Security Gain | User Experience |
|--------|----------|---------------|-----------------|
| **Knowledge** | Password, PIN | 50% | Familiar |
| **Possession** | TOTP, SMS | 90% | Good |
| **Inherence** | Fingerprint, Face | 95% | Excellent |
| **Location** | GPS, IP | 70% | Transparent |
| **Time** | Time-based tokens | 80% | Good |

---

## 🚪 **AUTHORIZATION QUICK REFERENCE**

### **Access Control Models**
| Model | Complexity | Flexibility | Performance | Best For |
|-------|------------|-------------|-------------|----------|
| **ACL** | Low | Low | High | Simple systems |
| **RBAC** | Medium | Medium | High | Organizations |
| **ABAC** | High | High | Medium | Dynamic environments |
| **PBAC** | Very High | Very High | Low | Complex compliance |

### **RBAC Role Hierarchy**
```
CEO
├── VP Engineering
│   ├── Engineering Manager
│   │   ├── Senior Engineer
│   │   └── Junior Engineer
│   └── QA Manager
│       └── QA Engineer
└── VP Sales
    ├── Sales Manager
    └── Sales Representative
```

### **ABAC Policy Example**
```
IF user.role = "manager" 
   AND user.department = resource.department
   AND current_time BETWEEN "9:00" AND "17:00"
   AND user.location = "office"
THEN ALLOW access
```

---

## 🔒 **CRYPTOGRAPHIC QUICK REFERENCE**

### **Encryption Algorithms**
| Algorithm | Type | Key Size | Security | Performance |
|-----------|------|----------|----------|-------------|
| **AES-256** | Symmetric | 256 bits | High | High |
| **RSA-2048** | Asymmetric | 2048 bits | Medium | Low |
| **ECC-256** | Asymmetric | 256 bits | High | Medium |
| **ChaCha20** | Symmetric | 256 bits | High | Very High |

### **Hash Functions**
| Algorithm | Output Size | Security | Performance | Status |
|-----------|-------------|----------|-------------|--------|
| **SHA-256** | 256 bits | High | Very High | Recommended |
| **SHA-384** | 384 bits | Very High | High | Recommended |
| **SHA-512** | 512 bits | Very High | High | Recommended |
| **MD5** | 128 bits | Broken | Very High | Deprecated |

### **TLS Cipher Suites**
| Cipher Suite | Key Exchange | Encryption | Hash | Security |
|--------------|--------------|------------|------|----------|
| **TLS_AES_256_GCM_SHA384** | ECDHE | AES-256-GCM | SHA-384 | High |
| **TLS_CHACHA20_POLY1305_SHA256** | ECDHE | ChaCha20-Poly1305 | SHA-256 | High |
| **TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384** | ECDHE | AES-256-GCM | SHA-384 | High |

---

## 🌐 **NETWORK SECURITY QUICK REFERENCE**

### **TLS Versions**
| Version | Security | Performance | Compatibility | Recommendation |
|---------|----------|-------------|---------------|----------------|
| **TLS 1.0** | Low | High | Legacy | Disable |
| **TLS 1.1** | Low | High | Legacy | Disable |
| **TLS 1.2** | Medium | High | Widely supported | Accept |
| **TLS 1.3** | High | Very High | Modern browsers | Prefer |

### **VPN Types**
| VPN Type | Security | Performance | Use Case | Implementation |
|----------|----------|-------------|----------|----------------|
| **IPSec** | High | Medium | Site-to-site | Hardware |
| **OpenVPN** | High | Medium | Remote access | Software |
| **WireGuard** | High | High | Modern VPN | Kernel |
| **SSL VPN** | Medium | High | Web-based | Browser |

---

## 📊 **PERFORMANCE METRICS**

### **Security Performance Impact**
| Security Feature | Performance Impact | Security Gain | ROI |
|------------------|-------------------|---------------|-----|
| **MFA** | 2-5x auth time | 99%+ improvement | High |
| **Strong Encryption** | 5-15% CPU | 1000x+ resistance | High |
| **Audit Logging** | 1-5% I/O | 100% compliance | Medium |
| **Rate Limiting** | 1-2% latency | 90%+ prevention | High |

### **Scalability Considerations**
| Aspect | Challenge | Solution | Performance |
|--------|-----------|----------|-------------|
| **Authentication** | High volume | Distributed auth | 10K+ users/sec |
| **Authorization** | Complex policies | Cached decisions | 100K+ decisions/sec |
| **Encryption** | Key management | Centralized KMS | 1GB+ encrypted/sec |
| **Monitoring** | High events | Distributed SIEM | 1M+ events/sec |

---

## ⚠️ **COMMON VULNERABILITIES**

### **Authentication Vulnerabilities**
| Vulnerability | Impact | Prevention | Detection |
|---------------|--------|------------|----------|
| **Weak Passwords** | Account compromise | Strong policies | Password audits |
| **Password Reuse** | Multiple compromise | Password managers | Breach monitoring |
| **Brute Force** | Account takeover | Rate limiting, MFA | Failed login alerts |
| **Session Hijacking** | Unauthorized access | Secure sessions | Session monitoring |

### **Authorization Vulnerabilities**
| Vulnerability | Impact | Prevention | Detection |
|---------------|--------|------------|----------|
| **Privilege Escalation** | Unauthorized access | Least privilege | Access reviews |
| **Missing Authorization** | Unauthorized actions | Always check | Code reviews |
| **Insecure Direct Object References** | Data access bypass | Indirect references | Penetration testing |
| **Horizontal Privilege Escalation** | Other users' data | Resource-level auth | Access monitoring |

### **Cryptographic Vulnerabilities**
| Vulnerability | Impact | Prevention | Detection |
|---------------|--------|------------|----------|
| **Weak Algorithms** | Data compromise | Strong algorithms | Security scanning |
| **Poor Key Management** | Key compromise | Secure KMS | Key rotation |
| **Random Number Generation** | Predictable values | Secure RNG | Entropy testing |
| **Timing Attacks** | Key extraction | Constant-time ops | Security testing |

---

## 🎯 **INTERVIEW QUICK TIPS**

### **When Asked About Security:**
1. **Start with Requirements**: "What are the security requirements?"
2. **Analyze Threats**: "What are the potential threats?"
3. **Consider Compliance**: "What compliance requirements exist?"
4. **Evaluate Trade-offs**: "What's the security vs usability trade-off?"
5. **Discuss Implementation**: "How would you implement this securely?"

### **Quick Decision Framework for Interviews:**
```
Step 1: "What's the security requirement?"
├─ High Security → Multi-factor, encryption, monitoring
├─ Medium Security → Strong passwords, HTTPS, logging
├─ Basic Security → Passwords, HTTPS
└─ Compliance Required → Audit logging, access controls

Step 2: "What are the threats?"
├─ External Attacks → Firewalls, intrusion detection
├─ Internal Threats → Access controls, monitoring
├─ Data Breaches → Encryption, access controls
└─ Compliance Violations → Audit logging, policies

Step 3: "What's the implementation approach?"
├─ Authentication strategy
├─ Authorization model
├─ Encryption requirements
└─ Monitoring and alerting
```

### **Common Interview Scenarios & Quick Answers:**

#### **"Design a Secure Authentication System"**
- **Authentication**: Multi-factor authentication (password + TOTP)
- **Authorization**: Role-based access control (RBAC)
- **Security**: HTTPS, rate limiting, audit logging
- **Trade-offs**: Security vs user experience

#### **"Design OAuth 2.0 for Third-Party Access"**
- **Flow**: Authorization Code Flow (most secure)
- **Security**: Short-lived tokens, refresh tokens
- **Implementation**: OAuth 2.0 server, client applications
- **Trade-offs**: Security vs complexity

#### **"Design a Secure API"**
- **Authentication**: JWT tokens or API keys
- **Authorization**: Role-based or attribute-based
- **Security**: HTTPS, rate limiting, input validation
- **Trade-offs**: Performance vs security

#### **"Design a Zero Trust Architecture"**
- **Principle**: Never trust, always verify
- **Implementation**: Continuous verification, micro-segmentation
- **Security**: Identity-based access, least privilege
- **Trade-offs**: Complexity vs security

### **Red Flags to Avoid in Interviews:**
- ❌ **"Security doesn't matter for this"** - Security always matters
- ❌ **"We'll add security later"** - Security by design is better
- ❌ **"Passwords are fine"** - Multi-factor is standard
- ❌ **"No need for encryption"** - Data protection is essential
- ❌ **"We don't need monitoring"** - Security monitoring is critical

### **Green Flags for Interviews:**
- ✅ **"Let me understand the security requirements first"** - Systematic approach
- ✅ **"What are the compliance requirements?"** - Regulatory awareness
- ✅ **"How do we handle key management?"** - Technical depth
- ✅ **"What's our incident response plan?"** - Operational thinking
- ✅ **"How do we monitor for threats?"** - Proactive security

---

## 📋 **QUICK REFERENCE: COMMON SCENARIOS**

### **Security Selection by Use Case**
| Use Case | Primary Security | Secondary Security | Key Decision Factors |
|----------|-----------------|-------------------|---------------------|
| **Web Application** | HTTPS + MFA | Input validation | User experience + security |
| **Mobile App** | Biometric + JWT | Certificate pinning | Convenience + security |
| **API Service** | API keys + OAuth | Rate limiting | Performance + security |
| **Enterprise System** | SAML + RBAC | Audit logging | Compliance + security |
| **IoT Device** | Certificate-based | Secure boot | Scalability + security |
| **Financial System** | Multi-factor + encryption | Compliance monitoring | Regulatory + security |

### **Security Selection by Data Sensitivity**
| Data Sensitivity | Authentication | Authorization | Encryption | Monitoring |
|------------------|----------------|---------------|------------|------------|
| **Public Data** | Basic | None | None | Basic |
| **Internal Data** | Password | RBAC | In transit | Logging |
| **Confidential Data** | MFA | ABAC | At rest + transit | Alerting |
| **Highly Sensitive** | Multi-factor | PBAC | End-to-end | Real-time |
| **Regulated Data** | Compliance | Compliance | Compliance | Compliance |

---

## 🚀 **SECURITY PATTERNS**

### **Authentication Patterns**
- **Single Sign-On (SSO)**: Centralized authentication
- **Federation**: Cross-domain authentication
- **Delegation**: Third-party authentication
- **Stateless**: Token-based authentication

### **Authorization Patterns**
- **Role-Based**: Permission by role
- **Attribute-Based**: Permission by attributes
- **Policy-Based**: Permission by policies
- **Resource-Based**: Permission by resource

### **Security Architecture Patterns**
- **Defense in Depth**: Multiple security layers
- **Zero Trust**: Never trust, always verify
- **Security by Design**: Built-in security
- **Privacy by Design**: Built-in privacy

---

## ⚖️ **COMPLIANCE FRAMEWORKS**

### **Common Compliance Standards**
| Standard | Focus | Requirements | Implementation |
|----------|-------|--------------|----------------|
| **GDPR** | Privacy | Consent, encryption, rights | Privacy controls |
| **SOX** | Financial | Audit trails, access controls | Financial controls |
| **HIPAA** | Healthcare | Privacy, security | Healthcare controls |
| **PCI DSS** | Payment | Encryption, access controls | Payment controls |

### **Compliance Implementation**
- **Data Classification**: Classify data by sensitivity
- **Access Controls**: Implement appropriate controls
- **Audit Logging**: Log all access and changes
- **Monitoring**: Monitor for compliance violations
- **Incident Response**: Respond to security incidents

---

## 📊 **MONITORING & ALERTING**

### **Key Security Metrics**
- **Authentication Success Rate**: 95%+ success rate
- **Failed Login Attempts**: <5% failure rate
- **Authorization Denials**: Monitor for policy violations
- **Encryption Coverage**: 100% sensitive data encrypted
- **Security Incidents**: 0 critical incidents

### **Alerting Thresholds**
- **Failed Logins > 10/minute**: Potential brute force
- **Unauthorized Access Attempts**: Immediate alert
- **Encryption Failures**: Immediate alert
- **Compliance Violations**: Immediate alert
- **Security Incidents**: Immediate response

---

## 🎯 **50 SECURITY INTERVIEW QUESTIONS**

### **Authentication Questions**
1. **How would you design a secure authentication system?**
2. **What are the different types of MFA?**
3. **How does OAuth 2.0 work?**
4. **What are the security implications of JWT?**
5. **How do you handle password security?**

### **Authorization Questions**
6. **What's the difference between RBAC and ABAC?**
7. **How do you implement least privilege?**
8. **What are the challenges of distributed authorization?**
9. **How do you handle privilege escalation?**
10. **What's the role of policies in authorization?**

### **Cryptography Questions**
11. **What's the difference between symmetric and asymmetric encryption?**
12. **How do you choose encryption algorithms?**
13. **What are the best practices for key management?**
14. **How do you handle cryptographic vulnerabilities?**
15. **What's the role of hash functions in security?**

### **Network Security Questions**
16. **How does TLS/SSL work?**
17. **What are the security implications of different TLS versions?**
18. **How do you secure API communications?**
19. **What's the role of VPNs in security?**
20. **How do you handle network segmentation?**

### **Application Security Questions**
21. **How do you prevent SQL injection?**
22. **What are the OWASP Top 10 vulnerabilities?**
23. **How do you implement secure coding practices?**
24. **What's the role of input validation?**
25. **How do you handle session security?**

### **Security Architecture Questions**
26. **How do you design a zero trust architecture?**
27. **What's the role of defense in depth?**
28. **How do you implement security by design?**
29. **What are the challenges of cloud security?**
30. **How do you handle microservices security?**

### **Compliance Questions**
31. **How do you implement GDPR compliance?**
32. **What are the requirements for PCI DSS?**
33. **How do you handle audit logging?**
34. **What's the role of data classification?**
35. **How do you implement privacy by design?**

### **Incident Response Questions**
36. **How do you handle security incidents?**
37. **What's your incident response plan?**
38. **How do you detect security threats?**
39. **What's the role of threat intelligence?**
40. **How do you handle data breaches?**

### **Security Monitoring Questions**
41. **How do you implement security monitoring?**
42. **What metrics do you track for security?**
43. **How do you handle false positives?**
44. **What's the role of SIEM systems?**
45. **How do you implement automated response?**

### **Advanced Security Questions**
46. **How do you handle quantum-resistant cryptography?**
47. **What's the role of machine learning in security?**
48. **How do you implement secure DevOps?**
49. **What are the challenges of IoT security?**
50. **How do you handle supply chain security?**

---

## ❓ **FREQUENTLY ASKED QUESTIONS (FAQs)**

### **Common Misconceptions & Quick Answers**

#### **Q1: "Security is too expensive"**
**A: FALSE** - Security is an investment that prevents costly breaches:
- **Cost of Breach**: $3.86M average cost of data breach
- **Security Investment**: 1-5% of IT budget typically sufficient
- **ROI**: Security investments typically pay for themselves

#### **Q2: "Passwords are secure enough"**
**A: FALSE** - Passwords alone are insufficient:
- **Password Attacks**: 80% of breaches involve weak passwords
- **MFA Impact**: 99%+ reduction in account compromise
- **Best Practice**: Always use multi-factor authentication

#### **Q3: "Security slows down development"**
**A: FALSE** - Security by design is faster:
- **Early Integration**: Security built-in is faster than retrofitting
- **Automated Tools**: Security scanning and testing can be automated
- **DevSecOps**: Security integrated into CI/CD pipeline

#### **Q4: "We're too small to be attacked"**
**A: FALSE** - Small organizations are common targets:
- **Attack Statistics**: 43% of cyber attacks target small businesses
- **Automated Attacks**: Most attacks are automated and target everyone
- **Supply Chain**: Small organizations are entry points to larger targets

#### **Q5: "Security is IT's responsibility"**
**A: FALSE** - Security is everyone's responsibility:
- **Human Factor**: 95% of breaches involve human error
- **Business Impact**: Security affects business operations
- **Shared Responsibility**: Security requires organizational commitment

---

*Use this cheatsheet for quick reference during interviews. Remember: security is not optional, it's essential for any system design.*
