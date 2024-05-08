const kue = require('kue');
const queue = kue.createQueue();

// Object containing job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message.'
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData)
  .save(err => {
    if (err) {
      console.error('Error creating job:', err);
    } else {
      console.log('Notification job created:', job.id);
    }
  });

// Event handlers for job completion and failure
job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});

// Process the queue
queue.process('push_notification_code', (job, done) => {
  // Simulating job processing
  setTimeout(() => {
    console.log('Processing job:', job.id);
    // Assuming job is successful
    done();
  }, 2000);
});

