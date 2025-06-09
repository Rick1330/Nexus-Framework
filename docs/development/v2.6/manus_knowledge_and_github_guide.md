# Manus Account Knowledge and GitHub Management Guide

## Overview

This document provides a comprehensive guide to the custom knowledge entries created for each specialized Manus account and the GitHub account management strategy for Nexus Framework v2.6 distributed development.

## Knowledge Directory Structure

Each Manus account has a dedicated knowledge directory containing specialized knowledge entries in the standard Manus format:
- **name**: Clear identifier for the knowledge entry
- **use_when**: Specific situations when this knowledge should be applied
- **content**: Detailed, actionable guidance formatted for easy reference

## Manus Account Knowledge Entries

### Manus-Architect
- **architectural_principles.md**: Core architectural principles for Nexus Framework v2.6
- **component_interface_patterns.md**: Design patterns for component interfaces and contracts
- **architectural_decision_records.md**: Standard format for documenting architectural decisions

### Manus-Backend
- **api_design_best_practices.md**: Best practices for designing robust, secure APIs
- **database_design_optimization.md**: Guidelines for database schema design and optimization
- **asynchronous_processing_patterns.md**: Patterns for implementing reliable asynchronous processing

### Manus-Frontend
- **react_component_patterns.md**: Design patterns for React components and state management
- **ui_ux_design_principles.md**: Principles for creating effective user interfaces and experiences
- **nextjs_performance_optimization.md**: Techniques for optimizing Next.js application performance

### Manus-DevOps
- **infrastructure_as_code_best_practices.md**: Best practices for implementing infrastructure as code
- **cicd_pipeline_design.md**: Guidelines for designing effective CI/CD pipelines
- **container_orchestration_best_practices.md**: Best practices for containerization and Kubernetes

### Manus-AI
- **llm_prompt_engineering_patterns.md**: Patterns for effective LLM prompt engineering
- **vector_database_optimization.md**: Techniques for optimizing vector databases for AI applications
- **agent_reasoning_system_design.md**: Design principles for agent reasoning systems

### Manus-QA
- **test_automation_strategy.md**: Strategic practices for implementing test automation
- **quality_metrics_and_kpis.md**: Comprehensive quality metrics and KPIs for monitoring

### Manus-Security
- **application_security_architecture.md**: Principles for implementing secure application architecture
- **security_testing_methodology.md**: Methodologies for comprehensive security testing

### Manus-PM
- **project_coordination_framework.md**: Framework for coordinating distributed development teams
- **multi_agent_project_management.md**: Practices for managing multi-agent projects effectively

## GitHub Account Management

The file `github_account_management.md` provides comprehensive guidance on:
- Account strategy options with recommendations
- Repository structure best practices
- Access control configurations
- Commit attribution and identity management
- Workflow recommendations
- Security considerations
- Tool integrations

The recommended approach is to use a single GitHub organization with team-based access control mirroring the Manus account roles, using a monorepo structure with clear component separation.

## Implementation Instructions

1. Add these knowledge entries to each Manus account's knowledge base using the standard import process
2. Configure GitHub organization and repository structure according to the recommendations
3. Establish team structures and access controls as outlined
4. Implement the recommended workflow and commit attribution practices
5. Document these practices in your central development documentation

## Next Steps

1. Review all knowledge entries to ensure alignment with your specific implementation needs
2. Customize any entries that require adaptation to your environment
3. Implement the GitHub organization structure as recommended
4. Onboard each Manus account with their specific knowledge entries
5. Establish regular reviews to update knowledge as the project evolves
