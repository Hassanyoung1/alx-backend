import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
    });
client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
    }
);


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
    redis.print('Reply: OK');
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.error(error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
