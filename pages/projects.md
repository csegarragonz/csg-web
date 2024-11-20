---
layout: default
permalink: /pages/projects
---

## Current Projects

The following summarises some of the projects that I have been working on.

### Faasm: A High-Performance Serverless Runtime with WebAssembly

[Faasm](https://github.com/faasm/faasm) is a high-performance stateful
serverless runtime that uses WebAssembly for function isolation. I have been
contributing to Faasm since 2020, and I am the main maintainer since 2022.

As part of my research, I have extended Faasm to long-running,
compute-intensive message passing and shared memory applications. By using
lightweight WASM execution environments, we can checkpoint and migrate or
elastically scale these applications at runtime. These changes in distribution
and scale allow us to improve application performance and resource usage when
deployed on shared cloud resources. These features are implemented in [Faabric](
https://github.com/faasm/faabric), a state and communication library for Faasm,
and described in the Granny project.

### SC2: Serverless Confidential Containers

SC2 is a system that aims to make confidential Virtual Machines (cVMs) usable
for serverless computing. This project originated during my internship at
IBM Research, where I collaborated with the [Confidential Containers](
https://github.com/confidential-containers) community. After my internship,
we published a workshop paper describing the limitations of the current
hardware/software stack. We are currently working on a full-system design
addressing these limitations.

### Sharsha: Anonymous And Composable Attestation For Confidential Serverless Workflows

Combining my interests in serverless runtimes and confidential computing, in
collaboration with Intel Labs, we explored the limitations of existing
attestation mechanisms for serverless workloads. The key observation is that
serverless decouples application code from the hardware it is executed on,
whereas attestation protocols do the exact opposite. We build an anonymous
and composable attestation framework for confidential serverless based on
Zero Knowledge Proofs (for anonymity) and Attribute Based Encryption (for
low-overhead composability). To illustrate the benefits of our framework,
we deploy it on top of a port of the Faasm runtime to a confidential setting
using Intel SGX, and SC2, therefore combining my previous two big projects.
