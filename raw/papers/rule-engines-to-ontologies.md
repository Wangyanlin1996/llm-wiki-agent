# From Rule Engines to Ontologies: An OWL 2 DL Approach for Domain-Specific Evaluation Information Systems

**Authors**: Borivoj Bogdanović, Siniša Nikolić

**Journal**: Computers (MDPI), published [[2026, 8, 20]]

**DOI**: 10.3390/computers15080544

**URL**: https://doi.org/10.3390/computers15080544

## Abstract

Domain-specific information systems often maintain their data model, rule base, and application infrastructure as separate artifacts, complicating maintenance and pre-deployment verification. This study investigates whether these artifacts can be unified in a verifiable ontology-to-code pipeline without changing the expected classifications. The proposed Model-Driven Architecture uses the Business Application Builder framework and a Web Ontology Language 2 Description Logic ontology to represent domain structure, classification rules, and generation metadata. HermiT verifies consistency, satisfiability, and subsumption under open-world semantics before code generation. The generator produces persistence, business-logic, data-transfer, and presentation layers, while the generated Java application evaluates stored records under closed-world semantics and resolves overlapping categories using ontology-declared priorities. In a Serbian research-evaluation case study, the generated system reproduced the M30 and M33 classifications of an established Jess implementation. An internal secondary experiment generated and executed a prenatal-diagnosis application; all six runtime classifications matched the HermiT entailments and expected outcomes. The public artifact independently reproduces the ontology-level experiments but excludes the proprietary generator and generated source code. The results support the feasibility of ontology-driven generation for static-classification systems, whereas arithmetic risk computation and temporal event processing remain better suited to complementary procedural technologies. No performance superiority is claimed.
