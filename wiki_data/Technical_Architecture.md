# Technical Architecture

This page documents the technical architecture and infrastructure of Duke County MMORPG.

## System Overview

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Client    │◄────►│ Game Server  │◄────►│  Database   │
│  (Unity)    │      │   Cluster    │      │ (PostgreSQL)│
└─────────────┘      └──────────────┘      └─────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │   Auth       │
                     │   Service    │
                     └──────────────┘
```

## Client Architecture

### Technology Stack
- **Engine**: Unity 2022 LTS
- **Language**: C#
- **Networking**: Custom protocol over UDP
- **Graphics**: Universal Render Pipeline (URP)

### Client Components
- **Input Manager**: Handles player input and controls
- **Network Client**: Manages connection to game servers
- **World Renderer**: Renders game world and entities
- **UI System**: UGUI-based interface
- **Audio Manager**: 3D spatial audio system
- **Asset Bundler**: Dynamic content loading

### Performance Targets
- 60 FPS on recommended specs
- 30 FPS minimum on minimum specs
- < 2GB RAM usage
- Efficient LOD system for draw call reduction

## Server Architecture

### Technology Stack
- **Language**: Go (Golang)
- **Framework**: Custom game server framework
- **Protocol**: Binary protocol over UDP with TCP fallback
- **Database**: PostgreSQL with Redis cache

### Server Types

#### Login Server
- Handles authentication
- Account management
- Character selection
- Load balancing to game servers

#### Game Server
- Hosts 1000-2000 concurrent players
- Manages game world simulation
- Processes player actions
- Handles combat calculations
- NPC AI and pathfinding

#### Chat Server
- Handles all chat communication
- Global, local, guild channels
- Message filtering and moderation

#### Instance Server
- Manages dungeon and raid instances
- Isolated from main world servers
- Spin up/down dynamically

### Horizontal Scaling
- Multiple game server instances
- Players distributed across servers
- Cross-server features via message queue
- Seamless zone transfers

## Database Schema

### Core Tables
- `accounts` - User account information
- `characters` - Character data
- `inventory` - Item storage
- `guilds` - Guild information
- `world_state` - Persistent world data
- `quest_progress` - Player quest status

### Caching Strategy
- Redis for hot data (player sessions, inventory)
- PostgreSQL for persistent storage
- Write-through cache for consistency
- 15-minute cache TTL

## Network Protocol

### Packet Structure
```
[Header: 4 bytes] [Type: 2 bytes] [Length: 2 bytes] [Payload: N bytes]
```

### Key Packet Types
- **0x0001**: Movement update
- **0x0002**: Ability cast
- **0x0003**: Chat message
- **0x0004**: Entity spawn
- **0x0005**: Entity despawn
- **0x0010**: Inventory update
- **0x0020**: Combat event

### Security
- All packets encrypted with AES-256
- Session tokens rotated every 10 minutes
- Rate limiting per connection
- Anti-cheat validation on server

## Infrastructure

### Deployment
- **Cloud Provider**: AWS
- **Regions**: US-East, US-West, EU-West, Asia-Pacific
- **Container Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions

### Monitoring
- **Metrics**: Prometheus + Grafana
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Tracing**: Jaeger for distributed tracing
- **Alerting**: PagerDuty integration

### Disaster Recovery
- Daily database backups
- Cross-region replication
- 99.9% uptime SLA target
- Automatic failover for critical services

## Development Tools

### Version Control
- Git with Git LFS for binary assets
- Trunk-based development
- Feature flags for gradual rollouts

### Build Pipeline
1. Code commit triggers CI
2. Automated tests (unit, integration)
3. Build client and server binaries
4. Deploy to staging environment
5. QA testing
6. Production deployment

### Testing Strategy
- Unit tests for game logic
- Integration tests for server APIs
- Load testing with simulated players
- Chaos engineering for resilience

## Performance Optimization

### Client Optimizations
- Object pooling for frequently spawned entities
- Occlusion culling
- Level of Detail (LOD) system
- Texture atlasing
- Async asset loading

### Server Optimizations
- Spatial partitioning (quadtree)
- Interest management (only send nearby updates)
- Batch database writes
- Connection pooling
- Goroutine pools for concurrency

## Related Pages

- [[Game Design Document]]
- [[Deployment Guide]]
- [[API Documentation]]
