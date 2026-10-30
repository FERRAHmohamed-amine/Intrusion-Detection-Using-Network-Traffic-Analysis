# Intrusion Detection & Prevention: Active Defense in an Open Cyber Range

[![Status](https://img.shields.io/badge/Status-Completed-success)]()
[![Institution](https://img.shields.io/badge/Institution-NSCS-blue)]()
[![Engine](https://img.shields.io/badge/Suricata-7.0-red)]()

An automated, near-zero-latency inline Intrusion Prevention System (IPS) built using **Suricata 7.0**, **Netfilter Queue (NFQUEUE)**, and **iptables** to transition security posture from passive logging to active, real-time threat mitigation.

Developed as part of an engineering project at the **National School of Cyber Security (NSCS)**.

---

## 👥 Authors
* **FERRAH Mohamed Amine**
* **Abed Mohamed Amine**
* **Magmoun Samy**
* **Ben Moussa Haoun**
* **Bouabdallah Abderrahmane**

---

## 🎯 Project Overview

Traditional Intrusion Detection Systems (IDS) are passive: they log threats after they occur, relying on manual human intervention which is often too slow to counter automated script attacks. 

This project implements an **Inline IPS Architecture** that sits transparently between an attacker and a victim machine, making autonomous, kernel-level decisions to drop malicious packets in real-time.

### Key Features
* **Transparent Inline Bridge Mode:** The defender sits logically/physically between endpoints; the attacker sees no extra hops.
* **Kernel-to-User-Space Handoff:** Utilizes Linux `iptables` and `NFQUEUE` to queue packets for inspection before issuing a definitive `ACCEPT` or `DROP` verdict.
* **Deep Packet Inspection (DPI):** Leverages Suricata 7.0 multi-threaded engine for high-performance, signature-based detection.

---

## 🏗️ Network Topology

```text
[ Attacker (Kali) ]  --->  [ Defender (IPS Mode / NFQUEUE) ]  --->  [ Victim PC (Protected) ]
      |                             |                                       |
  (Exploits)                 (Active Prevention)                        (Safe Traffic)
