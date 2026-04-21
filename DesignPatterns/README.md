# Design Patterns, Principles & Architectural Methods

Reusable solutions. Learn vocabulary; avoid over-applying.

## SOLID Principles (`SOLID_Principles/`)
- **SRP** Single Responsibility — one reason to change.
- **OCP** Open/Closed — open to extension, closed to modification.
- **LSP** Liskov Substitution — subtype replaces super without surprises.
- **ISP** Interface Segregation — many small interfaces > one fat.
- **DIP** Dependency Inversion — depend on abstractions, not concretes.

## Clean Code Principles (`CleanCodePrinciples/`)
DRY, KISS, YAGNI, Law of Demeter, Composition over Inheritance, Tell-Don't-Ask, Fail-Fast, Boy Scout Rule.

## GoF Creational (`Creational/`)
Singleton, Factory Method, Abstract Factory, Builder, Prototype, Object Pool, Multiton, Lazy Init, Dependency Injection.

## GoF Structural (`Structural/`)
Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy, Marker, Twin.

## GoF Behavioral (`Behavioral/`)
Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor, Interpreter, Null Object, Specification.

## Concurrency Patterns (`Concurrency/`)
Active Object, Monitor, Half-Sync/Half-Async, Leader-Followers, Producer-Consumer, Thread Pool, Read-Write Lock, Reactor, Proactor, Immutable, Copy-On-Write, Barrier, Future/Promise, Fork-Join, CSP Channels, Actor Model.

## Architectural Patterns (`Architectural/`)
Layered, MVC, MVP, MVVM, Hexagonal (Ports & Adapters), Clean Architecture, Onion, Event-Driven, CQRS, Event Sourcing, Microservices, MicroKernel, Space-Based, SOA, Pipe-and-Filter, Pub-Sub, Blackboard, Broker.

## Enterprise Integration Patterns (`Enterprise_Integration/`)
From Hohpe & Woolf: Message Router, Translator, Aggregator, Content-Based Router, Splitter, Message Channel, Dead Letter, Idempotent Receiver, Saga, Claim Check, Process Manager.

## Cloud-Native / Distributed (`Cloud_Native/`)
Ambassador, Sidecar, Bulkhead, Circuit Breaker, Retry w/ Jitter, Throttling, Strangler Fig, Anti-Corruption Layer, BFF (Backends for Frontends), Gateway Aggregation, Outbox/Inbox, Cloud Saga, Cache-Aside, Compensating Transaction, Health Endpoint, Priority Queue, Queue-Based Load Leveling, Choreography, Orchestration.

## Anti-Patterns (`AntiPatterns/`)
God Object, Spaghetti, Golden Hammer, Lava Flow, Silver Bullet, Premature Optimization, Magic Numbers, Big Ball of Mud, YoYo, Cargo Cult, Copy-Paste.

## When to use which
| Need | Pattern |
|------|---------|
| Swap algorithm at runtime | Strategy |
| Notify many observers | Observer |
| Build object step-by-step | Builder |
| Wrap legacy | Adapter |
| Add behavior without subclass | Decorator |
| One-instance global | Singleton (use sparingly) |
| Decouple issuer from handler | Command + Chain of Responsibility |
| Retries + timeouts + fallback | Circuit Breaker + Bulkhead |
| Distributed transaction | Saga |
| Read-write split at model level | CQRS |
| Append-only history | Event Sourcing |
| Hide incompatible legacy | Anti-Corruption Layer |

## Rules
1. Name the pattern you use in comments/PRs — communication win.
2. Start concrete. Refactor to pattern when 3rd duplicate appears.
3. Patterns are not goals. Solving a problem is.
4. Reading *Design Patterns* (GoF) + *Patterns of Enterprise Application Architecture* (Fowler) + *Enterprise Integration Patterns* (Hohpe) covers 90%.
