
# 🔍 Regex-Based Threat Hunting & Log Analysis Script

## 📌 Overview
This Python script demonstrates how **regular expressions** can be applied in **cybersecurity threat hunting** and **SOC investigations**. It analyzes text and log data to identify common **Indicators of Compromise (IOCs)** and performs basic **IP reputation analysis**.

## 🧠 Summary
- Detects **hexadecimal malware signatures** from text inputs  
- Identifies **device IDs** that match a specific pattern (`r15*`)  
- Extracts **IP address patterns** from log data  
- Flags IPs as **malicious or clean** based on a predefined list  
- Includes an **interactive investigation mode** with timestamps and SOC-style analyst guidance  

## 🎯 Purpose
The script simulates **real-world SOC log analysis and triage workflows**, making it useful for:
- Learning regex-based detection techniques  
- SOC analyst training and labs  
- Demonstrations and portfolio projects  
- Entry-level threat hunting automation

## 🔐 User Access & Device Authorization Script

## 📌 Overview
This Python script simulates a **basic access control mechanism** used in security environments to validate **user identity and authorized devices**. It demonstrates how login attempts can be verified against a predefined list of approved users and their assigned devices, with timestamped audit output.

## 🧠 Summary
- Maintains a list of **approved users mapped to authorized device IDs**
- Performs **case-insensitive username validation**
- Verifies whether a login attempt comes from an **approved device**
- Logs the **approval time** for authorized users
- Denies access for **unknown users or unauthorized devices**
- Includes an **interactive login flow** for user input testing

## 🎯 Purpose
The script models a simplified **authentication and device authorization workflow**, useful for:
- Understanding access control fundamentals  
- SOC and IAM training demonstrations  
- Security automation learning projects  
- Entry-level authentication logic simulations  



