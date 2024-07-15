# What is typeorm?

`ORM:`

- Stands for Object-relational mapping.
- It is a technique for converting data between a relational database and the heap of an object-oriented programming language.
- TypeORM is an `ORM` that can run in `NodeJS`, `Browser`, `Cordova`, `PhoneGap`, `Ionic`, `React Native`, `NativeScript`, `Expo`, and `Electron` platforms and can be used with `TypeScript` and `JavaScript` (ES2021).
- TypeORM supports both `Active Record` and Data `Mapper patterns`, unlike all other `JavaScript` `ORMs` currently in existence.

<br />

`Note:`

TypeORM is highly influenced by other ORMs, such as `Hibernate`, `Doctrine` and `Entity Framework`.

`Features:`

- Supports both DataMapper and ActiveRecord (your choice).
- Entities and columns.
- Database-specific column types.
- Entity manager.
- Repositories and custom repositories.
- Clean object-relational model.
- Associations (relations).
- Eager and lazy relations.
- Uni-directional, bi-directional, and self-referenced relations.
- Supports multiple inheritance patterns.
- Cascades.
- Indices.
- Transactions.
- Migrations and automatic migrations generation.
- Connection pooling.
- Replication.
- Using multiple database instances.
- Working with multiple database types.
- Cross-database and cross-schema queries.
- Elegant-syntax, flexible and powerful QueryBuilder.
- Left and inner joins.
- Proper pagination for queries using joins.
- Query caching.
- Streaming raw results.
- Logging.
- Listeners and subscribers (hooks).
- Supports closure table pattern.
- Schema declaration in models or separate configuration files.
- Supports MySQL / MariaDB / Postgres / CockroachDB / SQLite / Microsoft SQL Server / Oracle / SAP Hana / sql.js.
- Supports MongoDB NoSQL database.
- Works in NodeJS / Browser / Ionic / Cordova / React Native / NativeScript / Expo / Electron platforms.
- TypeScript and JavaScript support.
- ESM and CommonJS support.
- Produced code is performant, flexible, clean, and maintainable.
- Follows all possible best practices.
- CLI.

<br />

`Installation:`

```ts
// install typeorm
npm install typeorm --save

// additional dep
npm install reflect-metadata --save

// and import it somewhere in the global place of your app (for example in app.ts):
import "reflect-metadata"

// Install a database driver: postgreSQL
npm install pg --save
```
