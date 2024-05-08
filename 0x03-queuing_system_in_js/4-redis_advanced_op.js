const redis = require('redis');
const client = redis.createClient();

const key = 'HolbertonSchools';

client.on('connect', () => {
  console.log('Redis client connected to the server');

  client.del(key, (err, reply) => {
    console.log(`Deleted existing hash: ${reply}`);

    const schools = {
      Portland: 50,
      Seattle: 80,
      'New York': 20,
      Bogota: 20,
      Cali: 40,
      Paris: 2
    };

    for (const school in schools) {
      client.hset(key, school, schools[school], redis.print);
    }

    client.hgetall(key, (err, obj) => {
      console.log(obj);
      client.quit(); // It's a good practice to close the client when you're done
    });
  });
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
