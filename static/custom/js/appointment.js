// Function to populate start time options


function submitForm(event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather form data
    const form = document.getElementById('appointment-form');
    const formData = new FormData(form);


    const jsonData = {};


    formData.forEach((value, key) => {
        jsonData[key] = value;
    });
    let hour = parseInt(jsonData.hour, 10);
    const min = jsonData.min;

    if (hour < 1 || hour > 12 || isNaN(hour)) {
        alert("Hour must be between 1 and 12.");
        return;
    }

    if (min < 0 || min > 59 || isNaN(min)) {
        alert("Minute must be between 0 and 59.");
        return;
    }

    const isPm = document.getElementById('amPmSwitch').checked;
    if (isPm && hour < 12) {
        hour += 12; // Convert to 24-hour format for PM
    } else if (!isPm && hour === 12) {
        hour = 0; // Convert 12 AM to 00
    }

    jsonData.startTime = `${hour.toString().padStart(2, '0')}:${min}`;
    delete jsonData.hour;
    delete jsonData.min;


    // Send the form data as JSON
    fetch('/addEvent', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
        .then(response => response.json())
        .then(data => {
            handleResponse(data)
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function handleResponse(data) {

    const startTime = data.startTime; // assuming format "HH:MM"
    const endTime = data.endTime; // assuming format "HH:MM"
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0'); // 月份从0开始，所以需要+1
    const day = String(today.getDate()).padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;

    // Convert to FullCalendar event format
    const event = {
        start: `${formattedDate}T${startTime}:00`, // adjust date format as needed
        end: `${formattedDate}T${endTime}:00` // adjust date format as needed
    };

    addEventToCalendar(event);
}


//EventListener
document.addEventListener('DOMContentLoaded', function () {
    const submitButton = document.getElementById('submit-button');
    submitButton.addEventListener('click', function (event) {
        submitForm(event);
    });
});

//Functions Call