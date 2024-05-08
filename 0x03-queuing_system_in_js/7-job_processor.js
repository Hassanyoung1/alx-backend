const kue = require('kue');
const queue = kue.createQueue();

// Blacklisted phone numbers array
const blacklistedNumbers = ['4153518780', '4153518781'];

// sendNotification function
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  // Simulate notification sending delay
  setTimeout(() => {
    job.progress(100, 100);
    done();
  }, 1000);
}

// Process queue jobs
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

// Sample job creation
const jobData = {
  phoneNumber: '1234567890', // Replace with actual number
  message: 'This is a test message',
};

const job = queue.create('push_notification_code_2', jobData).save((err) => {
  if (err) {
    console.log(`Failed to create job: ${err}`);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', (errorMessage) => {
  console.log(`Notification job failed: ${errorMessage}`);
}).on('progress', (progress) => {
  console.log(`Job #${job.id} ${progress}% complete`);
});
