import 'dotenv/config';

import pg from 'pg';
const client = new pg.Client({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});
await client.connect();
const { rows } = await client.query('select now()');
console.log('DB time:', rows[0]);
await client.end();
