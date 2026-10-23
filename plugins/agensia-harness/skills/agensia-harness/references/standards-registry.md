# Industry Overlay Registry & Execution Trace Model

P2A is industry-neutral at core; industry depth comes from overlay standards. Each overlay supplies: (a) domain data objects for the `know` boundary, (b) evidence/record types for `prove`, (c) reference processes to seed capture, (d) compliance constraints on harness levels.

## Registry

| Industry | Overlay | Steward | Contribution to P2A |
|---|---|---|---|
| Healthcare | Clinical data & workflow interoperability standards (regional) | national/sector bodies | Clinical data objects and terminologies; clinical actions capped HL2; licensed-professional decisions HL1 max |
| Banking | **BIAN** Service Landscape | BIAN | Service domains ≈ capabilities; business objects; control/reporting patterns |
| Insurance | **ACORD** Framework | ACORD | Data model, forms, claims/underwriting reference flows |
| Telecom | **eTOM / ODA** | TM Forum | Ready-made multi-level process taxonomy; Open APIs |
| Supply chain | **SCOR-DS** | ASCM | Plan-Source-Make-Deliver-Return hierarchy + metrics for Pod KPIs |
| Manufacturing | **ISA-95 / IEC 62264** | ISA/IEC | Automation pyramid: agents live at L3–L4, never write to L0–L2 control without HL2 checkpoint |
| IT service mgmt | **ITIL 4** | PeopleCert | Incident/change flows; change approval = natural HL2 checkpoint |
| Retail / CPG | **GS1** + APQC retail PCF | GS1 | GTIN/GLN identification; EPCIS traceability events map onto the Event element |
| HR | **HR Open Standards** | HR Open | Recruiting/employment schemas; personnel actions human-only |
| Public sector | National interoperability frameworks | various | Data exchange + records retention constraints |
| Cross-industry base | **APQC PCF** | APQC | The default process taxonomy (13 categories, 5-digit IDs) under every overlay |

## The P2A execution trace model (used in every industry)

Every unit of agent work exists in three linked forms:

| Trace element | What it is |
|---|---|
| **Definition** | Versioned design-time description of what *should* happen (process card + activity row) |
| **Request** | Instantiation: "run activity X on case Y", with task state machine `requested → accepted → in-progress → completed/failed/cancelled/escalated` |
| **Event** | Immutable record of what *actually* happened, linked back to Request and Definition |

Why it matters: Definition → Request → Event = provable execution. Every agent action traces to a versioned definition (what should happen), a request (what was asked), and an event (what happened). That is the evidence chain a harness needs at HL2+.

## Applying an overlay (replication recipe)

1. **Declare it** in the repo README (`overlay: bian-13`, `etom-23.5`, `apqc-pcf-7.4`…).
2. **Map data objects**: `standard_mapping` field per data object (e.g., `bian:CustomerOffer`, `gs1:EPCIS-event`).
3. **Seed processes** from the overlay's reference flows (eTOM and SCOR strongest).
4. **Constrain harness levels** per the overlay's regulatory posture — write into the harness spec's `policy_constraints` (e.g., "prescribing decisions: licensed clinician only → HL1 max").
5. **Adopt evidence types** for `prove` (the overlay's audit/provenance record types, traceability events, change records…).

Stages, HL0–HL4, file formats, the trace model, and the wizard never change per industry — only the overlay does.
