client.del(key, (err, reply) => {
  console.log(`Deleted existing hash: ${reply}`);
  // Now you can run your hset commands here to ensure they will add new fields
});
